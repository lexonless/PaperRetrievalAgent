const projectSlugInput = document.getElementById("project-slug-input");
const pdfDirInput = document.getElementById("pdf-dir-input");
const choosePdfDirButton = document.getElementById("choose-pdf-dir-button");
const queryInput = document.getElementById("query-input");
const submitButton = document.getElementById("submit-button");
const formMessage = document.getElementById("form-message");
const statusChip = document.getElementById("job-status");
const statusDetail = document.getElementById("status-detail");
const activityLog = document.getElementById("activity-log");
const jobMeta = document.getElementById("job-meta");
const resultContent = document.getElementById("result-content");

const LAST_JOB_STORAGE_KEY = "langgraph-web-last-job-id";
const QUERY_DRAFT_STORAGE_KEY = "langgraph-web-query-draft";
const PROJECT_SLUG_STORAGE_KEY = "langgraph-web-project-slug";
const PDF_DIR_STORAGE_KEY = "langgraph-web-pdf-dir";
const MAX_VISIBLE_EVENTS = 10;

let eventSource = null;
let pollTimer = null;
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

function setStatusDetail(message) {
  statusDetail.textContent = message || "The page will show stage updates here.";
}

function setBusy(isBusy) {
  submitButton.disabled = isBusy;
  projectSlugInput.disabled = isBusy;
  pdfDirInput.disabled = isBusy;
  queryInput.disabled = isBusy;
  choosePdfDirButton.disabled = isBusy;
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
  window.localStorage.setItem(LAST_JOB_STORAGE_KEY, jobId);
}

function forgetJob() {
  window.localStorage.removeItem(LAST_JOB_STORAGE_KEY);
}

function saveDrafts() {
  window.localStorage.setItem(PROJECT_SLUG_STORAGE_KEY, projectSlugInput.value);
  window.localStorage.setItem(PDF_DIR_STORAGE_KEY, pdfDirInput.value);
  window.localStorage.setItem(QUERY_DRAFT_STORAGE_KEY, queryInput.value);
}

function restoreDrafts() {
  const slug = window.localStorage.getItem(PROJECT_SLUG_STORAGE_KEY);
  const pdfDir = window.localStorage.getItem(PDF_DIR_STORAGE_KEY);
  const query = window.localStorage.getItem(QUERY_DRAFT_STORAGE_KEY);
  if (slug !== null) {
    projectSlugInput.value = slug;
  }
  if (pdfDir !== null) {
    pdfDirInput.value = pdfDir;
  }
  if (query !== null) {
    queryInput.value = query;
  }
}

function renderPlaceholder(message, className = "placeholder") {
  resultContent.innerHTML = `<p class="${className}">${message}</p>`;
}

function renderEvents(events) {
  currentEvents = Array.isArray(events) ? events.slice(-MAX_VISIBLE_EVENTS) : [];
  if (currentEvents.length === 0) {
    activityLog.innerHTML = '<li class="placeholder">Recent graph updates will appear here.</li>';
    return;
  }

  const items = currentEvents.slice().reverse();
  activityLog.innerHTML = items.map((event) => `
    <li data-event-index="${event.index}">
      <div class="activity-line">
        <strong>${toTitleCase(event.phase || "running")}</strong>
        <span class="activity-meta">${event.step || "graph"} | ${event.event_type || "update"}${event.timestamp ? ` | ${event.timestamp}` : ""}</span>
      </div>
      <p class="activity-summary">${event.summary || ""}</p>
    </li>
  `).join("");
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
  if (payload.project_slug) {
    details.push(`Project: ${payload.project_slug}`);
  }
  if (payload.stop_reason) {
    details.push(`Stop: ${payload.stop_reason}`);
  } else if (payload.finished_at) {
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
  setStatusDetail(payload.latest_message);
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
        setStatusDetail("");
        renderEvents([]);
        jobMeta.textContent = "";
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
      formMessage.textContent = "The graph is working on your project.";
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
    setStatusDetail("");
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
    formMessage.textContent = "The graph is working on your project.";
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

async function submitJob() {
  const projectSlug = projectSlugInput.value.trim();
  const query = queryInput.value.trim();
  const pdfDir = pdfDirInput.value.trim();

  if (!projectSlug) {
    formMessage.textContent = "Enter a project slug before starting.";
    return;
  }
  if (!query) {
    formMessage.textContent = "Enter a query before starting.";
    return;
  }

  saveDrafts();
  clearPollTimer();
  closeEventSource();
  forgetJob();
  setBusy(true);
  setStatus("queued", "queued");
  setStatusDetail("Waiting for the run to start.");
  renderEvents([]);
  updateMeta({ project_slug: projectSlug });
  renderPlaceholder("The final research note will appear here once the run finishes.");
  formMessage.textContent = "Submitting query.";

  try {
    const response = await fetch("/api/jobs", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        project_slug: projectSlug,
        query,
        pdf_dir: pdfDir,
      }),
    });

    if (!response.ok) {
      const payload = await response.json().catch(() => ({}));
      throw new Error(typeof payload.detail === "string" ? payload.detail : "Unable to create job.");
    }

    const payload = await response.json();
    rememberJob(payload.job_id);
    formMessage.textContent = "Query submitted.";
    connectEventStream(payload.job_id);
  } catch (error) {
    setBusy(false);
    setStatus("failed", "failed");
    setStatusDetail("");
    renderPlaceholder("The run could not be started.", "error-text");
    formMessage.textContent = error instanceof Error ? error.message : "Request failed.";
  }
}

function restoreLastJob() {
  const savedJobId = window.localStorage.getItem(LAST_JOB_STORAGE_KEY);
  if (!savedJobId) {
    return;
  }

  renderPlaceholder("Restoring the latest run.");
  formMessage.textContent = "Restoring previous state.";
  connectEventStream(savedJobId);
}

async function choosePdfDir() {
  choosePdfDirButton.disabled = true;
  formMessage.textContent = "Opening folder picker.";
  try {
    const response = await fetch("/api/select-pdf-dir", {
      method: "POST",
    });
    if (!response.ok) {
      const payload = await response.json().catch(() => ({}));
      throw new Error(typeof payload.detail === "string" ? payload.detail : "Unable to open folder picker.");
    }
    const payload = await response.json();
    if (payload.pdf_dir) {
      pdfDirInput.value = payload.pdf_dir;
      saveDrafts();
      formMessage.textContent = "Folder selected.";
    } else {
      formMessage.textContent = "Folder selection canceled.";
    }
  } catch (error) {
    formMessage.textContent = error instanceof Error ? error.message : "Folder selection failed.";
  } finally {
    if (!submitButton.disabled) {
      choosePdfDirButton.disabled = false;
    }
  }
}

submitButton.addEventListener("click", submitJob);
choosePdfDirButton.addEventListener("click", choosePdfDir);
projectSlugInput.addEventListener("input", saveDrafts);
pdfDirInput.addEventListener("input", saveDrafts);
queryInput.addEventListener("input", saveDrafts);
queryInput.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
    event.preventDefault();
    submitJob();
  }
});

restoreDrafts();
restoreLastJob();
