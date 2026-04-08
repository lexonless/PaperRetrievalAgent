# Paper Search Report

**Query:** LLM agent planning recent papers
**Generated At:** 2026-03-22T16:13:21

## Final Response

**Retrieval Strategy**
I interpreted "LLM agent planning" as research focusing on how Large Language Models act as autonomous agents to generate, execute, or optimize plans (task decomposition, multi-agent collaboration, tool use, and reasoning). I targeted papers from **2024 to 2025** to ensure relevance, looking for both theoretical frameworks and applied implementations. I merged results from arXiv and Crossref, prioritizing papers with strong abstracts or titles explicitly mentioning "planning" or "agent."

**Candidate Papers**

**1. A Plan Reuse Mechanism for LLM-Driven Agent**
*   **Source:** arXiv
*   **Year:** 2025
*   **Link:** http://arxiv.org/abs/2512.21309v2
*   **Relevance:** High. Addresses the latency issue in LLM planning by proposing `AgentReuse`, a mechanism to identify and reuse similar plans based on request semantics. It reports significant latency reduction (93.12%) and high accuracy in similarity evaluation.
*   **Notes:** Focuses on efficiency and optimization in personal assistant agents.

**2. Small LLMs Are Weak Tool Learners: A Multi-LLM Agent**
*   **Source:** arXiv
*   **Year:** 2024
*   **Link:** http://arxiv.org/abs/2401.07324v3
*   **Relevance:** High. Proposes decomposing agent capabilities into a "planner," "caller," and "summarizer" to overcome the limitations of small LLMs in task planning and tool use.
*   **Notes:** Offers a modular framework for improving planning performance in resource-constrained models.

**3. Large Language Model-Based Planning Agent with Generative Memory**
*   **Source:** Crossref (SSRN)
*   **Year:** 2024
*   **Link:** https://doi.org/10.2139/ssrn.4918035
*   **Relevance:** High. Title indicates a direct focus on planning agents. Integrates generative memory to strengthen performance in "textualized worlds."
*   **Notes:** Evidence is limited to title and metadata as the abstract was not available, but the title matches the query perfectly.

**4. Dream2Drive: A Large Language Model Powered Agent for Real World Multi-task Vehicle Motion Planning**
*   **Source:** IJCNN 2025
*   **Year:** 2025
*   **Link:** https://doi.org/10.1109/ijcnn64981.2025.11228910
*   **Relevance:** High. Applies LLM agent planning to a physical domain (vehicle motion planning), bridging the gap between textual reasoning and real-world control tasks.
*   **Notes:** Strong candidate for robotics/autonomous driving applications.

**5. Planning, Living and Judging: A Multi-agent LLM-based Framework for Cyclical Urban Planning**
*   **Source:** arXiv
*   **Year:** 2024
*   **Link:** http://arxiv.org/abs/2412.20505v1
*   **Relevance:** Moderate/High. Describes a multi-agent framework (CUP) for urban planning, featuring cyclical feedback loops where agents generate, simulate, and judge plans.
*   **Notes:** Focuses on complex, multi-step simulation and planning in a specific domain (urban regeneration).

**6. Too Helpful to Be Safe: User-Mediated Attacks on Planning and Web-Use Agents**
*   **Source:** arXiv
*   **Year:** 2026 (Preprint/Future date)
*   **Link:** http://arxiv.org/abs/2601.10758v1
*   **Relevance:** Moderate. While focused on security, it evaluates how trip-planning and web-use agents execute plans when under attack. Highlights the risk of over-execution in planning agents.
*   **Notes:** Important for understanding safety boundaries in autonomous planning.

**7. Research on Multi-agent Path Planning Algorithm Based on Large Language Model**
*   **Source:** ISSSR 2024
*   **Year:** 2024
*   **Link:** https://doi.org/10.1109/isssr61934.2024.00028
*   **Relevance:** Moderate. Investigates path planning algorithms enhanced by LLMs within a multi-agent context.
*   **Notes:** Likely relevant to robotics or logistics, though abstract details were sparse.

**8. Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code**
*   **Source:** arXiv
*   **Year:** 2025
*   **Link:** http://arxiv.org/abs/2508.08322v1
*   **Relevance:** Moderate. Discusses a multi-agent system for code generation that emphasizes planning via intent clarification and context injection.
*   **Notes:** Good practical case study for software engineering agents.

**Next Steps**
*   **Narrow by Domain:** If you are interested in a specific application (e.g., robotics, coding assistants, or pure reasoning), I can refine the search to those keywords.
*   **Focus on Mechanism:** If you prefer papers comparing specific planning algorithms (e.g., ReAct vs. Tree-of-Thoughts vs. Reflexion), I can search for those terms specifically.
*   **Adjust Time Range:** The current results include some 2025/2026 preprints; if you strictly prefer peer-reviewed conference papers from 2023-2024, let me know.

## Trace

### Message 1

- Source: `user`
- Type: `TextMessage`

```text
LLM agent planning recent papers
```

### Message 2

- Source: `paper_search_agent`
- Type: `ThoughtEvent`

```text
I'll search for recent papers on LLM agent planning. Let me query both arXiv and Crossref to get comprehensive coverage of recent work in this area.
```

### Message 3

- Source: `paper_search_agent`
- Type: `ToolCallRequestEvent`

```text
FunctionCall(id='call_5df10afa1d32450eb14daf3e', arguments='{"query":"LLM agent planning","max_results":"10"}', name='search_arxiv')
FunctionCall(id='call_91f80e80051f4cc29b12d344', arguments='{"query":"large language model agent planning","from_year":"2022","max_results":"10"}', name='search_crossref')
```

### Message 4

- Source: `paper_search_agent`
- Type: `ToolCallExecutionEvent`

```text
content="arXiv results for query: LLM agent planning\n\n[1]\nTitle: A Plan Reuse Mechanism for LLM-Driven Agent\nSource: arXiv\nAuthors: Guopeng Li, Ruiqi Wu, Haisheng Tan\nPublished: 2025-12-24T18:08:03Z\nURL: http://arxiv.org/abs/2512.21309v2\nSummary: Integrating large language models (LLMs) into personal assistants, like Xiao Ai and Blue Heart V, effectively enhances their ability to interact with humans, solve complex tasks, and manage IoT devices. Such assistants are also termed LLM-driven agents. Upon receiving user requests, the LLM-driven agent generates plans using an LLM, executes these plans through various tools, and then returns the response to the user. During this process, the latency for generating a plan with an LLM can reach tens of seconds, significantly degrading user experience. Real-world dataset analysis shows that about 30% of the requests received by LLM-driven agents are identical or similar, which allows the reuse of previously generated plans to reduce latency. However, it is difficult to accurately define the similarity between the request texts received by the LLM-driven agent through directly evaluating the original request texts. Moreover, the diverse expressions of natural language and the unstructured format of plan texts make implementing plan reuse challenging. To address these issues, we present and implement a plan reuse mechanism for LLM-driven agents called AgentReuse. AgentReuse leverages the similarities and differences among requests' semantics and uses intent classification to evaluate the similarities between requests and enable the reuse of plans. Experimental results based on a real-world dataset demonstrate that AgentReuse achieves a 93% effective plan reuse rate, an F1 score of 0.9718, and an accuracy of 0.9459 in evaluating request similarities, reducing latency by 93.12% compared with baselines without using the reuse mechanism.\n\n[2]\nTitle: Too Helpful to Be Safe: User-Mediated Attacks on Planning and Web-Use Agents\nSource: arXiv\nAuthors: Fengchao Chen, Tingmin Wu, Van Nguyen, Carsten Rudolph\nPublished: 2026-01-14T03:29:13Z\nURL: http://arxiv.org/abs/2601.10758v1\nSummary: Large Language Models (LLMs) have enabled agents to move beyond conversation toward end-to-end task execution and become more helpful. However, this helpfulness introduces new security risks stem less from direct interface abuse than from acting on user-provided content. Existing studies on agent security largely focus on model-internal vulnerabilities or adversarial access to agent interfaces, overlooking attacks that exploit users as unintended conduits. In this paper, we study user-mediated attacks, where benign users are tricked into relaying untrusted or attacker-controlled content to agents, and analyze how commercial LLM agents respond under such conditions. We conduct a systematic evaluation of 12 commercial agents in a sandboxed environment, covering 6 trip-planning agents and 6 web-use agents, and compare agent behavior across scenarios with no, soft, and hard user-requested safety checks. Our results show that agents are too helpful to be safe by default. Without explicit safety requests, trip-planning agents bypass safety constraints in over 92% of cases, converting unverified content into confident booking guidance. Web-use agents exhibit near-deterministic execution of risky actions, with 9 out of 17 supported tests reaching a 100% bypass rate. Even when users express soft or hard safety intent, constraint bypass remains substantial, reaching up to 54.7% and 7% for trip-planning agents, respectively. These findings reveal that the primary issue is not a lack of safety capability, but its prioritization. Agents invoke safety checks only conditionally when explicitly prompted, and otherwise default to goal-driven execution. Moreover, agents lack clear task boundaries and stopping rules, frequently over-executing workflows in ways that lead to unnecessary data disclosure and real-world harm.\n\n[3]\nTitle: Focus Agent: LLM-Powered Virtual Focus Group\nSource: arXiv\nAuthors: Taiyu Zhang, Xuesong Zhang, Robbe Cools, Adalberto L. Simeone\nPublished: 2024-09-03T13:56:14Z\nURL: http://arxiv.org/abs/2409.01907v1\nSummary: In the domain of Human-Computer Interaction, focus groups represent a widely utilised yet resource-intensive methodology, often demanding the expertise of skilled moderators and meticulous preparatory efforts. This study introduces the ``Focus Agent,'' a Large Language Model (LLM) powered framework that simulates both the focus group (for data collection) and acts as a moderator in a focus group setting with human participants. To assess the data quality derived from the Focus Agent, we ran five focus group sessions with a total of 23 human participants as well as deploying the Focus Agent to simulate these discussions with AI participants. Quantitative analysis indicates that Focus Agent can generate opinions similar to those of human participants. Furthermore, the research exposes some improvements associated with LLMs acting as moderators in focus group discussions that include human participants.\n\n[4]\nTitle: Individual Planning in Agent Populations: Exploiting Anonymity and Frame-Action Hypergraphs\nSource: arXiv\nAuthors: Ekhlas Sonu, Yingke Chen, Prashant Doshi\nPublished: 2015-03-24T22:26:50Z\nURL: http://arxiv.org/abs/1503.07220v2\nSummary: Interactive partially observable Markov decision processes (I-POMDP) provide a formal framework for planning for a self-interested agent in multiagent settings. An agent operating in a multiagent environment must deliberate about the actions that other agents may take and the effect these actions have on the environment and the rewards it receives. Traditional I-POMDPs model this dependence on the actions of other agents using joint action and model spaces. Therefore, the solution complexity grows exponentially with the number of agents thereby complicating scalability. In this paper, we model and extend anonymity and context-specific independence -- problem structures often present in agent populations -- for computational gain. We empirically demonstrate the efficiency from exploiting these problem structures by solving a new multiagent problem involving more than 1,000 agents.\n\n[5]\nTitle: Small LLMs Are Weak Tool Learners: A Multi-LLM Agent\nSource: arXiv\nAuthors: Weizhou Shen, Chenliang Li, Hongzhan Chen, Ming Yan, Xiaojun Quan\nPublished: 2024-01-14T16:17:07Z\nURL: http://arxiv.org/abs/2401.07324v3\nSummary: Large Language Model (LLM) agents significantly extend the capabilities of standalone LLMs, empowering them to interact with external tools (e.g., APIs, functions) and complete various tasks in a self-directed fashion. The challenge of tool use demands that LLMs not only understand user queries and generate answers accurately but also excel in task planning, tool invocation, and result summarization. While traditional works focus on training a single LLM with all these capabilities, performance limitations become apparent, particularly with smaller models. To overcome these challenges, we propose a novel approach that decomposes the aforementioned capabilities into a planner, caller, and summarizer. Each component is implemented by a single LLM that focuses on a specific capability and collaborates with others to accomplish the task. This modular framework facilitates individual updates and the potential use of smaller LLMs for building each capability. To effectively train this framework, we introduce a two-stage training paradigm. First, we fine-tune a backbone LLM on the entire dataset without discriminating sub-tasks, providing the model with a comprehensive understanding of the task. Second, the fine-tuned LLM is used to instantiate the planner, caller, and summarizer respectively, which are continually fine-tuned on respective sub-tasks. Evaluation across various tool-use benchmarks illustrates that our proposed multi-LLM framework surpasses the traditional single-LLM approach, highlighting its efficacy and advantages in tool learning.\n\n[6]\nTitle: Planning, Living and Judging: A Multi-agent LLM-based Framework for Cyclical Urban Planning\nSource: arXiv\nAuthors: Hang Ni, Yuzhi Wang, Hao Liu\nPublished: 2024-12-29T15:43:25Z\nURL: http://arxiv.org/abs/2412.20505v1\nSummary: Urban regeneration presents significant challenges within the context of urbanization, requiring adaptive approaches to tackle evolving needs. Leveraging advancements in large language models (LLMs), we propose Cyclical Urban Planning (CUP), a new paradigm that continuously generates, evaluates, and refines urban plans in a closed-loop. Specifically, our multi-agent LLM-based framework consists of three key components: (1) Planning, where LLM agents generate and refine urban plans based on contextual data; (2) Living, where agents simulate the behaviors and interactions of residents, modeling life in the urban environment; and (3) Judging, which involves evaluating plan effectiveness and providing iterative feedback for improvement. The cyclical process enables a dynamic and responsive planning approach. Experiments on the real-world dataset demonstrate the effectiveness of our framework as a continuous and adaptive planning process.\n\n[7]\nTitle: MedAide: Information Fusion and Anatomy of Medical Intents via LLM-based Agent Collaboration\nSource: arXiv\nAuthors: Dingkang Yang, Jinjie Wei, Mingcheng Li, Jiyao Liu, Lihao Liu\nPublished: 2024-10-16T13:10:27Z\nURL: http://arxiv.org/abs/2410.12532v3\nSummary: In healthcare intelligence, the ability to fuse heterogeneous, multi-intent information from diverse clinical sources is fundamental to building reliable decision-making systems. Large Language Model (LLM)-driven information interaction systems currently showing potential promise in the healthcare domain. Nevertheless, they often suffer from information redundancy and coupling when dealing with complex medical intents, leading to severe hallucinations and performance bottlenecks. To this end, we propose MedAide, an LLM-based medical multi-agent collaboration framework designed to enable intent-aware information fusion and coordinated reasoning across specialized healthcare domains. Specifically, we introduce a regularization-guided module that combines syntactic constraints with retrieval augmented generation to decompose complex queries into structured representations, facilitating fine-grained clinical information fusion and intent resolution. Additionally, a dynamic intent prototype matching module is proposed to utilize dynamic prototype representation with a semantic similarity matching mechanism to achieve adaptive recognition and updating of the agent's intent in multi-round healthcare dialogues. Ultimately, we design a rotation agent collaboration mechanism that introduces dynamic role rotation and decision-level information fusion across specialized medical agents. Extensive experiments are conducted on four medical benchmarks with composite intents. Experimental results from automated metrics and expert doctor evaluations show that MedAide outperforms current LLMs and improves their medical proficiency and strategic reasoning.\n\n[8]\nTitle: Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code\nSource: arXiv\nAuthors: Muhammad Haseeb\nPublished: 2025-08-09T14:45:53Z\nURL: http://arxiv.org/abs/2508.08322v1\nSummary: Large Language Models (LLMs) have shown promise in automating code generation and software engineering tasks, yet they often struggle with complex, multi-file projects due to context limitations and knowledge gaps. We propose a novel context engineering workflow that combines multiple AI components: an Intent Translator (GPT-5) for clarifying user requirements, an Elicit-powered semantic literature retrieval for injecting domain knowledge, NotebookLM-based document synthesis for contextual understanding, and a Claude Code multi-agent system for code generation and validation. Our integrated approach leverages intent clarification, retrieval-augmented generation, and specialized sub-agents orchestrated via Claude's agent framework. We demonstrate that this method significantly improves the accuracy and reliability of code assistants in real-world repositories, yielding higher single-shot success rates and better adherence to project context than baseline single-agent approaches. Qualitative results on a large Next.js codebase show the multi-agent system effectively plans, edits, and tests complex features with minimal human intervention. We compare our system with recent frameworks like CodePlan, MASAI, and HyperAgent, highlighting how targeted context injection and agent role decomposition lead to state-of-the-art performance. Finally, we discuss the implications for deploying LLM-based coding assistants in production, along with lessons learned on context management and future research directions.\n\n[9]\nTitle: HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN Planning\nSource: arXiv\nAuthors: Damien Pellier, Alexandre Albore, Humbert Fiorino, Rafael Bailon-Ruiz\nPublished: 2023-06-12T18:21:23Z\nURL: http://arxiv.org/abs/2306.07353v1\nSummary: Real world applications as in industry and robotics need modelling rich and diverse automated planning problems. Their resolution usually requires coordinated and concurrent action execution. In several cases, these problems are naturally decomposed in a hierarchical way and expressed by a Hierarchical Task Network (HTN) formalism. HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1 does not allow to represent planning problems with numerical and temporal constraints, which are essential for real world applications. We propose to fill the gap between HDDL and these operational needs and to extend HDDL by taking inspiration from PDDL 2.1 in order to express numerical and temporal expressions. This paper opens discussions on the semantics and the syntax needed for a future HDDL 2.1 extension.\n\n[10]\nTitle: Provenance-Based Assessment of Plans in Context\nSource: arXiv\nAuthors: Scott E. Friedman, Robert P. Goldman, Richard G. Freedman, Ugur Kuter, Christopher Geib\nPublished: 2020-11-03T15:13:54Z\nURL: http://arxiv.org/abs/2011.01774v1\nSummary: Many real-world planning domains involve diverse information sources, external entities, and variable-reliability agents, all of which may impact the confidence, risk, and sensitivity of plans. Humans reviewing a plan may lack context about these factors; however, this information is available during the domain generation, which means it can also be interwoven into the planner and its resulting plans. This paper presents a provenance-based approach to explaining automated plans. Our approach (1) extends the SHOP3 HTN planner to generate dependency information, (2) transforms the dependency information into an established PROV-O representation, and (3) uses graph propagation and TMS-inspired algorithms to support dynamic and counter-factual assessment of information flow, confidence, and support. We qualified our approach's explanatory scope with respect to explanation targets from the automated planning literature and the information analysis literature, and we demonstrate its ability to assess a plan's pertinence, sensitivity, risk, assumption support, diversity, and relative confidence." name='search_arxiv' call_id='call_5df10afa1d32450eb14daf3e' is_error=False
content="Crossref results for query: large language model agent planning\n\n[1]\nTitle: Large Language Model-Based Planning Agent with Generative Memory Strengthens Performance in Textualized World\nSource: Crossref / Crossref\nAuthors: JY L, Wenning Hao, kai Cheng, Dawei Jin\nPublished: 2024\nURL: https://doi.org/10.2139/ssrn.4918035\nDOI: 10.2139/ssrn.4918035\nSummary: No abstract/summary available.\n\n[2]\nTitle: Dream2Drive: A Large Language Model Powered Agent for Real World Multi-task Vehicle Motion Planning\nSource: Crossref / 2025 International Joint Conference on Neural Networks (IJCNN)\nAuthors: Hongru Wang, Jun Wang\nPublished: 2025-6-30\nURL: https://doi.org/10.1109/ijcnn64981.2025.11228910\nDOI: 10.1109/ijcnn64981.2025.11228910\nSummary: No abstract/summary available.\n\n[3]\nTitle: Research on Multi-agent Path Planning Algorithm Based on Large Language Model\nSource: Crossref / 2024 10th International Symposium on System Security, Safety, and Reliability (ISSSR)\nAuthors: Liu Lian, Cui Peng\nPublished: 2024-3-16\nURL: https://doi.org/10.1109/isssr61934.2024.00028\nDOI: 10.1109/isssr61934.2024.00028\nSummary: No abstract/summary available.\n\n[4]\nTitle: Llm-Mtmp: A Large Language Model-Based Multi-Agent Task and Motion Planning Framework for Power Inspection Robots\nSource: Crossref / Crossref\nAuthors: Zongyuan Wang, Xin Zhou, Jianliang Mao, Chuanlin Zhang, Chenggang Cui\nPublished: 2025\nURL: https://doi.org/10.2139/ssrn.5362568\nDOI: 10.2139/ssrn.5362568\nSummary: No abstract/summary available.\n\n[5]\nTitle: Advancements in Multi-Agent Large Language Model Systems for Next-Generation AI\nSource: Crossref / Advances in Computational Intelligence and Robotics\nAuthors: Rajeshwari Sissodia, Vinay Dwivedi, TaraChand Verma\nPublished: 2025-7-25\nURL: https://doi.org/10.4018/979-8-3373-1419-8.ch001\nDOI: 10.4018/979-8-3373-1419-8.ch001\nSummary: <jats:p>The integration of Multi-Agent Systems (MAS) with Large Language Models (LLMs) represents a significant advancement in the field of artificial intelligence, enabling the development of intelligent, autonomous systems capable of solving complex tasks and enhancing decision-making. MAS, composed of multiple interacting agents with autonomous decision-making abilities, and LLMs, which leverage vast amounts of textual data to understand and generate human-like language, can work synergistically to create more robust AI systems. This chapter explores the fundamentals of MAS and LLMs, their individual and combined strengths, and their potential to address complex challenges in various fields, such as robotics, healthcare, and business. We discuss key features of both MAS and LLMs, including agent collaboration, reinforcement learning, and contextual understanding in language models. The chapter also examines the integration of these two domains, highlighting their potential for collaborative problem-solving, decision support, and knowledge extraction.</jats:p>\n\n[6]\nTitle: PlanFitting: Personalized Exercise Planning with Large Language Model-driven Conversational Agent\nSource: Crossref / Proceedings of the 7th ACM Conference on Conversational User Interfaces\nAuthors: Donghoon Shin, Gary Hsieh, Young-Ho Kim\nPublished: 2025-7-8\nURL: https://doi.org/10.1145/3719160.3736607\nDOI: 10.1145/3719160.3736607\nSummary: No abstract/summary available.\n\n[7]\nTitle: Industry Chain Agent: Large Language Model-Based Agent for Intelligent Generation of Industry Chain Graph\nSource: Crossref / Crossref\nAuthors: Mengjia Du, Guojun Wang, Qingsong Ruan\nPublished: 2025\nURL: https://doi.org/10.2139/ssrn.5242786\nDOI: 10.2139/ssrn.5242786\nSummary: No abstract/summary available.\n\n[8]\nTitle: Emergent Cooperative Dynamics and Causal Treatment Effects in Large Language Model Multi-Agent Ecosystems\nSource: Crossref / Crossref\nAuthors: Vikas Ramachandra\nPublished: 2026-3-20\nURL: https://doi.org/10.22541/au.177403077.70686468/v1\nDOI: 10.22541/au.177403077.70686468/v1\nSummary: No abstract/summary available.\n\n[9]\nTitle: Controlling Large Language Model Hallucination Based on Agent AI with LangGraph\nSource: Crossref / Crossref\nAuthors: Jialin Wang, Zhihua Duan\nPublished: 2025-1-13\nURL: https://doi.org/10.33774/coe-2025-xkwl5\nDOI: 10.33774/coe-2025-xkwl5\nSummary: <jats:p>As Large Language Models (LLMs) become integral to Natural Language Processing (NLP) applications, their tendency to generate hallucinations — outputs misaligned with input data or real-world facts — presents a significant challenge. This paper introduces a novel approach leveraging Agent AI within the LangGraph system to systematically detect and mitigate LLM hallucinations. The framework categorizes hallucinations into three distinct types: Hallucination Knowledge Positive (HK+), Hallucination Knowledge Negative (HK-), and normal responses. HK+ represents errors where the model has relevant knowledge but provides incorrect answers, while HK- denotes hallucinations arising from insufficient knowledge. Normal responses are accurate outputs requiring no intervention. The proposed method employs corrective Retrieval-Augmented Generation (RAG) to address HK- cases by supplementing missing knowledge. For HK+, a human-in-the-loop mechanism is activated to rectify errors and ensure accuracy. Normal responses proceed without additional processing. This structured approach improves the precision and reliability of LLMs across diverse application scenarios. By integrating Agent AI for dynamic classification and targeted intervention, the LangGraph system significantly reduces hallucination rates, offering a robust solution for enhancing LLM performance in real-world deployments. This research provides new perspectives and methodologies for advancing LLM stability and dependability.</jats:p>\n\n[10]\nTitle: Advancements in Multi-Agent Large Language Model Systems for Next-Generation AI\nSource: Crossref / Advances in Computational Intelligence and Robotics\nAuthors: Abinaya Gopalakrishnan, G. Ramya, T. Preethiya, R. Nithya Paranthaman, S. Ashwini\nPublished: 2025-7-25\nURL: https://doi.org/10.4018/979-8-3373-1419-8.ch002\nDOI: 10.4018/979-8-3373-1419-8.ch002\nSummary: <jats:p>Large Language Models (LLMs) have enabled AI research. Their easier design of new ways to handle challenges across a wide range of applications has increased this discipline's influence. Multi-agent LLM systems in diagnostics and healthcare can revolutionize clinical decision-making, precision medicine, and patient care. This chapter examines multi-agent LLMs' medical concepts, designs, and applications.Multi-agent systems can scale, modularize, and specialize and integrate several medical specializations and contextual knowledge. This chapters covers the technical implementation of these systems, including advanced Large Language Models, quality control measures, guardrails, self-reflection, integration with EHRs, and explainable AI for decision transparency. We discuss possible benefits with future directions, like integrating IoT devices and creating advanced natural language interfaces.</jats:p>" name='search_crossref' call_id='call_91f80e80051f4cc29b12d344' is_error=False
```

### Message 5

- Source: `paper_search_agent`
- Type: `TextMessage`

```text
**Retrieval Strategy**
I interpreted "LLM agent planning" as research focusing on how Large Language Models act as autonomous agents to generate, execute, or optimize plans (task decomposition, multi-agent collaboration, tool use, and reasoning). I targeted papers from **2024 to 2025** to ensure relevance, looking for both theoretical frameworks and applied implementations. I merged results from arXiv and Crossref, prioritizing papers with strong abstracts or titles explicitly mentioning "planning" or "agent."

**Candidate Papers**

**1. A Plan Reuse Mechanism for LLM-Driven Agent**
*   **Source:** arXiv
*   **Year:** 2025
*   **Link:** http://arxiv.org/abs/2512.21309v2
*   **Relevance:** High. Addresses the latency issue in LLM planning by proposing `AgentReuse`, a mechanism to identify and reuse similar plans based on request semantics. It reports significant latency reduction (93.12%) and high accuracy in similarity evaluation.
*   **Notes:** Focuses on efficiency and optimization in personal assistant agents.

**2. Small LLMs Are Weak Tool Learners: A Multi-LLM Agent**
*   **Source:** arXiv
*   **Year:** 2024
*   **Link:** http://arxiv.org/abs/2401.07324v3
*   **Relevance:** High. Proposes decomposing agent capabilities into a "planner," "caller," and "summarizer" to overcome the limitations of small LLMs in task planning and tool use.
*   **Notes:** Offers a modular framework for improving planning performance in resource-constrained models.

**3. Large Language Model-Based Planning Agent with Generative Memory**
*   **Source:** Crossref (SSRN)
*   **Year:** 2024
*   **Link:** https://doi.org/10.2139/ssrn.4918035
*   **Relevance:** High. Title indicates a direct focus on planning agents. Integrates generative memory to strengthen performance in "textualized worlds."
*   **Notes:** Evidence is limited to title and metadata as the abstract was not available, but the title matches the query perfectly.

**4. Dream2Drive: A Large Language Model Powered Agent for Real World Multi-task Vehicle Motion Planning**
*   **Source:** IJCNN 2025
*   **Year:** 2025
*   **Link:** https://doi.org/10.1109/ijcnn64981.2025.11228910
*   **Relevance:** High. Applies LLM agent planning to a physical domain (vehicle motion planning), bridging the gap between textual reasoning and real-world control tasks.
*   **Notes:** Strong candidate for robotics/autonomous driving applications.

**5. Planning, Living and Judging: A Multi-agent LLM-based Framework for Cyclical Urban Planning**
*   **Source:** arXiv
*   **Year:** 2024
*   **Link:** http://arxiv.org/abs/2412.20505v1
*   **Relevance:** Moderate/High. Describes a multi-agent framework (CUP) for urban planning, featuring cyclical feedback loops where agents generate, simulate, and judge plans.
*   **Notes:** Focuses on complex, multi-step simulation and planning in a specific domain (urban regeneration).

**6. Too Helpful to Be Safe: User-Mediated Attacks on Planning and Web-Use Agents**
*   **Source:** arXiv
*   **Year:** 2026 (Preprint/Future date)
*   **Link:** http://arxiv.org/abs/2601.10758v1
*   **Relevance:** Moderate. While focused on security, it evaluates how trip-planning and web-use agents execute plans when under attack. Highlights the risk of over-execution in planning agents.
*   **Notes:** Important for understanding safety boundaries in autonomous planning.

**7. Research on Multi-agent Path Planning Algorithm Based on Large Language Model**
*   **Source:** ISSSR 2024
*   **Year:** 2024
*   **Link:** https://doi.org/10.1109/isssr61934.2024.00028
*   **Relevance:** Moderate. Investigates path planning algorithms enhanced by LLMs within a multi-agent context.
*   **Notes:** Likely relevant to robotics or logistics, though abstract details were sparse.

**8. Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code**
*   **Source:** arXiv
*   **Year:** 2025
*   **Link:** http://arxiv.org/abs/2508.08322v1
*   **Relevance:** Moderate. Discusses a multi-agent system for code generation that emphasizes planning via intent clarification and context injection.
*   **Notes:** Good practical case study for software engineering agents.

**Next Steps**
*   **Narrow by Domain:** If you are interested in a specific application (e.g., robotics, coding assistants, or pure reasoning), I can refine the search to those keywords.
*   **Focus on Mechanism:** If you prefer papers comparing specific planning algorithms (e.g., ReAct vs. Tree-of-Thoughts vs. Reflexion), I can search for those terms specifically.
*   **Adjust Time Range:** The current results include some 2025/2026 preprints; if you strictly prefer peer-reviewed conference papers from 2023-2024, let me know.
```
