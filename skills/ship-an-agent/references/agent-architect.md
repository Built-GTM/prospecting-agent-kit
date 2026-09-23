<!-- Portable copy for ship-an-agent bundles. Source: the owner's _playbook/agent-architect.md. Re-copy when it changes. -->
# Agent architect: from plain language to a deployable managed agent

This is the method. Someone says "I want an agent that..." and you produce `agents/<slug>/spec.md` from `agent-spec.template.md`, along with a `system-prompt.md`, skill drafts, and memory seed content. Then you walk the build checklist.

## The five moves

### 1. Listen, then restate the job
Let them describe it fully. Restate it in one breath: who uses it, what it does, what done looks like, and what kicks it off (a person, an event, or a schedule). If "done" can't be checked, pin it down now. "A good prep doc" is not checkable. "A kit with a company brief, 10 likely questions each mapped to a story, and 5 questions to ask" is.

**Should this even be an agent?** Check four things: the task is multi-step and hard to specify upfront, the outcome is worth the cost, Claude is good at it, and errors can be caught. If any answer is no, suggest a skill in Claude or a single API call instead, and say why.

### 2. Split the work into prompt, skills, memory, tools
This is the core design decision. Use this sorting rule:

| Put it in... | When it is... | Example |
|---|---|---|
| **System prompt** | Identity, judgment, priorities, output contract, hard rules. True on every turn. | "You coach, you don't flatter. Never invent a number." |
| **Skill** | A repeatable procedure or body of know-how, only needed for some tasks. Loads on demand. | "How to research an interviewer", "How to run a mock interview" |
| **Memory store** | Facts that change or accumulate, and must survive across sessions. Per user or shared. | The user's story bank, past interview debriefs, preferences |
| **Session resource (file)** | Input for one run only. | This job description, this resume version |
| **Tool / MCP** | Anything that touches the outside world: read or write a system, fetch data. | Calendar, Gmail, web search, the Lab API |

Tests to apply:
- If the prompt goes past about 2 pages, procedures have leaked into it. Move them to skills.
- If a skill contains facts about one user, those facts belong in memory.
- If memory holds a procedure, it belongs in a skill.
- A skill for everything the agent does twice. A memory file for everything it learns once.

### 3. Map every verb to a capability (the viability gate)
Go through the jobs list one clause at a time. Each verb needs:
- a tool or MCP server that can do it ("draft a thank-you email" means Gmail MCP with a drafts tool, not just "email"),
- a credential for that connection (named in the spec, stored in a vault),
- a reachable host (environment networking),
- the data it depends on, mounted or in memory.

Any gap gets flagged in the spec as a blocker. Never write a spec you already know is missing a connection. Use `references/process.md` step 8 for what exists today.

### 4. Pick the surface and the kickoff
- **Surface:** where the user talks to it. v1 is usually the cheapest loop that proves the job (the Console session view, or Claude Code driving a session). v2 is where real users live (Slack, a web chat, a scheduled run). See `surfaces.md`.
- **Kickoff:** conversational, outcome with rubric (the harness iterates until the rubric passes), or scheduled deployment.
- **Budget:** set a dollar cap per session.

### 5. Write it, then prove it
1. Draft `spec.md`, `system-prompt.md`, `skills/*/SKILL.md`, `memory-seed/`.
2. Present the spec to the builder with assumptions marked and one batched question list.
3. After approval: generate `agent.yaml` + `environment.yaml` into the deploy repo, create the vault and memory stores, then run a smoke-test session ("confirm you can reach each connection, don't start the task").
4. Run the evals in section 10 of the spec. Iterate on the prompt and skills by **updating** the agent, which creates a new version. Never create a new agent for a tweak.

## Writing the system prompt
- Open with the role and the user it serves, in two or three sentences.
- State the operating principles as short declaratives, each with a reason. The model generalizes from reasons.
- Define the output contract: what artifacts, where they go (`/mnt/session/outputs/`), and in what format.
- List the hard rules: never send, never invent numbers, always ask before writing to an external system.
- Tell it how to use memory: check memory before starting, and write what it learned when it finishes.
- Don't paste procedures, examples libraries, or reference data. Those are skills.
- Default model `claude-opus-5`. Only move down when an eval shows a cheaper model holds quality.

## Writing a skill
Same format as Claude skills: `skills/<name>/SKILL.md` with frontmatter `name` and `description`. The description decides when it loads, so write it as trigger conditions. Keep the body procedural: steps, checklists, templates, a worked example. Scripts and reference files can sit next to it. Existing sources to mine: the builder skills bundled in `.claude/skills/`, any skills the builder already has, and the installed `anthropic-skills:*` set.

## Designing memory
- **One shared read-only store** for reference knowledge every user benefits from (frameworks, question libraries).
- **One read-write store per user** for their facts and history. Name it `<agent>-<user-slug>`.
- Lay it out as many small files by path (each under 100KB): `/profile/`, `/history/<date>-<thing>.md`, `/preferences.md`.
- Write `description` and `instructions` for the model: what's in the store and when to read or write it.
- Never store credentials. Redact versions if a secret or PII lands there by mistake.

## Output of a design session
In `agents/<slug>/`:
```
spec.md             filled template
system-prompt.md    the prompt, ready to paste into agent.yaml
skills/<name>/SKILL.md
memory-seed/        files to load into memory stores, laid out by path
evals/cases.md      test prompts + pass criteria
```
