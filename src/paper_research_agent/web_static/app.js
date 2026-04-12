const queryInput = document.getElementById("query-input");
const submitButton = document.getElementById("submit-button");
const formMessage = document.getElementById("form-message");
const statusChip = document.getElementById("job-status");
const statusDetail = document.getElementById("status-detail");
const resultContent = document.getElementById("result-content");
const jobMeta = document.getElementById("job-meta");
const activityLog = document.getElementById("activity-log");
const LAST_JOB_STORAGE_KEY = "paper-agent-last-job-id";
const QUERY_DRAFT_STORAGE_KEY = "paper-agent-query-draft";
const MAX_VISIBLE_EVENTS = 10;

let activeJobId = null;
let pollTimer = null;
let eventSource = null;
let reconnectAttempts = 0;
let currentEvents = [];

function toTitleCase(value) {
  return String(value || "idle")
    .split(/[_\s-]+/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function setStatus(phase, status = phase) {
  const normalizedPhase = String(phase || status || "idle").toLowerCase();
  const normalizedStatus = String(status || phase || "idle").toLowerCase();
  const label = normalizedStatus === "succeeded" || normalizedPhase === "completed"
    ? "Done"
    : toTitleCase(normalizedPhase);
  statusChip.textContent = label;
  statusChip.className = `status-chip ${normalizedPhase}`;
}

function setStatusDetail(agent, latestMessage) {
  const parts = [];
  if (agent) {
    parts.push(`Agent: ${agent}`);
  }
  if (latestMessage) {
    parts.push(latestMessage);
  }
  statusDetail.textContent = parts.join(" | ") || "The page will show stage updates here.";
}

function setBusy(isBusy) {
  submitButton.disabled = isBusy;
  queryInput.disabled = isBusy;
}

function clearPollTimer() {
  if (pollTimer !== null) {
    window.clearTimeout(pollTimer);
    pollTimer = null;
  }
}

function closeEventSource() {
  if (eventSource !== null) {
    eventSource.close();
    eventSource = null;
  }
}

function rememberJob(jobId) {
  activeJobId = jobId;
  window.localStorage.setItem(LAST_JOB_STORAGE_KEY, jobId);
}

function forgetJob() {
  activeJobId = null;
  window.localStorage.removeItem(LAST_JOB_STORAGE_KEY);
}

function saveQueryDraft(value) {
  window.localStorage.setItem(QUERY_DRAFT_STORAGE_KEY, value);
}

function restoreQueryDraft() {
  const savedDraft = window.localStorage.getItem(QUERY_DRAFT_STORAGE_KEY);
  if (savedDraft !== null) {
    queryInput.value = savedDraft;
  }
}

function renderPlaceholder(message, className = "placeholder") {
  resultContent.innerHTML = `<p class="${className}">${message}</p>`;
}

function renderEvents(events) {
  currentEvents = Array.isArray(events) ? events.slice(-MAX_VISIBLE_EVENTS) : [];
  if (currentEvents.length === 0) {
    activityLog.innerHTML = '<li class="placeholder">Recent progress updates will appear here.</li>';
    return;
  }

  const items = currentEvents.slice().reverse();
  activityLog.innerHTML = items.map((event) => {
    const phase = toTitleCase(event.phase || "running");
    const agent = event.agent || "System";
    const timestamp = event.timestamp || "";
    const summary = event.summary || "";
    return `
      <li data-event-index="${event.index}">
        <div class="activity-line">
          <strong>${phase}</strong>
          <span class="activity-meta">${agent}${timestamp ? ` | ${timestamp}` : ""}</span>
        </div>
        <p class="activity-summary">${summary}</p>
      </li>
    `;
  }).join("");
}

function appendEvent(event) {
  if (!event || currentEvents.some((item) => item.index === event.index)) {
    return;
  }
  currentEvents = [...currentEvents, event].slice(-MAX_VISIBLE_EVENTS);
  renderEvents(currentEvents);
}

function updateMeta(payload) {
  const details = [];
  if (payload.finished_at) {
    details.push(`Finished: ${payload.finished_at}`);
  } else if (payload.started_at) {
    details.push(`Started: ${payload.started_at}`);
  } else if (payload.created_at) {
    details.push(`Created: ${payload.created_at}`);
  }
  jobMeta.textContent = details.join(" | ");
}

function applySnapshot(payload) {
  rememberJob(payload.job_id);
  setStatus(payload.phase || payload.status, payload.status);
  setStatusDetail(payload.current_agent, payload.latest_message);
  updateMeta(payload);
  renderEvents(payload.events || []);
}

async function pollJob(jobId) {
  try {
    const response = await fetch(`/api/jobs/${jobId}`);
    if (!response.ok) {
      if (response.status === 404) {
        closeEventSource();
        forgetJob();
        setBusy(false);
        setStatus("idle", "idle");
        setStatusDetail("", "");
        jobMeta.textContent = "";
        renderEvents([]);
        renderPlaceholder("The previous run is no longer available.");
        formMessage.textContent = "";
        return;
      }
      throw new Error("Failed to fetch job status.");
    }

    const payload = await response.json();
    applySnapshot(payload);

    if (payload.status === "queued" || payload.status === "running") {
      setBusy(true);
      formMessage.textContent = "The agent system is working on your query.";
      pollTimer = window.setTimeout(() => pollJob(jobId), 1500);
      return;
    }

    setBusy(false);
    formMessage.textContent = "";

    if (payload.status === "succeeded") {
      resultContent.innerHTML = payload.result_html;
      closeEventSource();
      return;
    }

    closeEventSource();
    renderPlaceholder(payload.error || "The run failed.", "error-text");
  } catch (error) {
    setBusy(false);
    setStatus("failed", "failed");
    setStatusDetail("", "");
    renderPlaceholder("The front end lost contact with the server.", "error-text");
    formMessage.textContent = error instanceof Error ? error.message : "Request failed.";
  }
}

function connectEventStream(jobId) {
  closeEventSource();
  clearPollTimer();
  reconnectAttempts = 0;
  eventSource = new EventSource(`/api/jobs/${jobId}/events`);

  eventSource.addEventListener("snapshot", (event) => {
    const payload = JSON.parse(event.data);
    applySnapshot(payload);
    if (payload.status === "succeeded") {
      resultContent.innerHTML = payload.result_html;
      setBusy(false);
      formMessage.textContent = "";
      closeEventSource();
    } else if (payload.status === "failed") {
      renderPlaceholder(payload.error || "The run failed.", "error-text");
      setBusy(false);
      formMessage.textContent = payload.error || "";
      closeEventSource();
    }
  });

  eventSource.addEventListener("progress", (event) => {
    const payload = JSON.parse(event.data);
    applySnapshot(payload);
    setBusy(true);
    formMessage.textContent = "The agent system is working on your query.";
  });

  eventSource.addEventListener("event", (event) => {
    appendEvent(JSON.parse(event.data));
  });

  eventSource.addEventListener("complete", (event) => {
    const payload = JSON.parse(event.data);
    applySnapshot(payload);
    resultContent.innerHTML = payload.result_html;
    setBusy(false);
    formMessage.textContent = "";
    closeEventSource();
  });

  eventSource.addEventListener("error", async (event) => {
    if (event.data) {
      const payload = JSON.parse(event.data);
      applySnapshot(payload);
      renderPlaceholder(payload.error || "The run failed.", "error-text");
      setBusy(false);
      formMessage.textContent = payload.error || "";
      closeEventSource();
      return;
    }

    reconnectAttempts += 1;
    if (reconnectAttempts >= 3) {
      closeEventSource();
      await pollJob(jobId);
    }
  });
}

async function submitQuery() {
  const query = queryInput.value.trim();
  if (!query) {
    formMessage.textContent = "Enter a query before starting.";
    return;
  }

  clearPollTimer();
  closeEventSource();
  forgetJob();
  setBusy(true);
  setStatus("queued", "queued");
  setStatusDetail("", "Waiting for the run to start.");
  updateMeta({ query });
  renderEvents([]);
  renderPlaceholder("The final notes will appear here once the run finishes.");
  formMessage.textContent = "Submitting query.";

  try {
    const response = await fetch("/api/jobs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
    });

    if (!response.ok) {
      const payload = await response.json().catch(() => ({}));
      const detail = typeof payload.detail === "string" ? payload.detail : "Unable to create job.";
      throw new Error(detail);
    }

    const payload = await response.json();
    rememberJob(payload.job_id);
    formMessage.textContent = "Query submitted.";
    connectEventStream(payload.job_id);
  } catch (error) {
    setBusy(false);
    setStatus("failed", "failed");
    setStatusDetail("", "");
    renderPlaceholder("The run could not be started.", "error-text");
    formMessage.textContent = error instanceof Error ? error.message : "Request failed.";
  }
}

function restoreLastJob() {
  const savedJobId = window.localStorage.getItem(LAST_JOB_STORAGE_KEY);
  if (!savedJobId) {
    return;
  }

  clearPollTimer();
  renderPlaceholder("Restoring the latest run.");
  formMessage.textContent = "Restoring previous state.";
  connectEventStream(savedJobId);
}

submitButton.addEventListener("click", submitQuery);
queryInput.addEventListener("input", () => {
  saveQueryDraft(queryInput.value);
});
queryInput.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
    event.preventDefault();
    submitQuery();
  }
});

restoreQueryDraft();
restoreLastJob();
