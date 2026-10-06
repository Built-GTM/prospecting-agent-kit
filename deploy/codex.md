# Deploy: OpenAI

**Re-researched 2026-10-05, after DevDay on 29 September.** The previous version of this page said OpenAI had no real managed agent equivalent. That is no longer true, and the correction is the most important thing on this page.

Two dates before you build anything. The **Assistants API was shut off on 26 August 2026**, hard, no read only mode. **Agent Builder shuts down on 30 November 2026.** If a tutorial uses either, it is out of date.

## The paths, now four

| Path | For | Where it runs |
|---|---|---|
| **Agents API** | the managed agent, the real equivalent | OpenAI hosted sandbox, your own VPC, or one of nine partner sandboxes |
| **Workspace Agents** | a Sales Operator, no code | ChatGPT Business, Enterprise, Edu |
| **Dots** | an always-on teammate | its own cloud computer |
| **Codex Cloud** | repo shaped work | an OpenAI container |

The Agents SDK still exists for anyone who wants to own the whole runtime. It is an engineering project. Do not start there.

## The Agents API, the thing that changed

Public beta. OpenAI describes it as a managed runtime over the Codex harness: **OpenAI handles sessions, orchestration, context compaction and recovery**, and you supply the tools and choose where it executes.

What it gives you:
- **Hosted shell containers.** `container_auto` provisions a managed Debian 12 environment with Python 3.11, Node.js 22, Java 17, Go 1.23 and Ruby 3.1, persistent storage at `/mnt/data`, and network access.
- **Three execution choices.** OpenAI hosted, your own private VPC, or nine partner sandboxes. Claude's equivalent is a cloud sandbox or self hosted, so this is a wider set.
- **Computer use.** The agent can navigate sites and operate applications through an OpenAI hosted browser.
- **MCP servers, subagents, durable session state.**
- **Server side compaction**, so a session can run for hours or days rather than hitting a context wall. One cited run went 5 million tokens and 150 tool calls without losing accuracy.

For this agent the fit is good. It needs web search and page reading, and the hosted container covers both.

**What this page does not know, and will not guess at:** how the Agents API holds credentials, whether it has a scheduling primitive like a cron deployment, and whether per run cost is visible. None of that was in the material read on 2026-10-05. Check the current docs before you depend on any of the three.

## Skills are now an explicit shared standard

This is the other change worth saying out loud. OpenAI and Anthropic have **converged on the same open standard**: a `SKILL.md` manifest with YAML frontmatter. Not a coincidence of formats, a stated convergence.

So `skills/four-whys-research/SKILL.md` in this kit moves across as it is. So does `AGENTS.md`. Nothing to convert.

## Workspace Agents, if you want no code

Still the closest thing to a Sales Operator's build, and the flow is the same shape as this kit's:

1. **Describe the job in the builder chat.** It drafts the workflow and instructions, you edit. Paste the objective and every anti job from `system-prompt.md`.
2. **Add connectors and pick the auth model.** The clearest vocabulary any vendor has produced: **"end user account"** means each person authenticates as themselves, **"agent owned account"** means a service account everyone shares. Your calendar is the first. A team drive is the second.
3. **Add skills.** Same `SKILL.md` standard. Type the budget line in by hand, because a builder that rewrites your instructions will drop a number.
4. **The binder** goes in a connected drive or as skill resources. Workspace agent memory is a per user folder the agent writes to, so it is **not** a read only mount. Same drift warning as the Grok build.
5. **Preview**, with action traces visible.
6. **Schedule**, with the Schedule button.

OpenAI has published a cookbook that builds a sales meeting prep agent this exact way: https://developers.openai.com/cookbook/articles/chatgpt-agents-sales-meeting-prep

Admin setup, because agents are off until an admin enables them: https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business

## Dots, the always-on one

Persistent agents on GPT-6 Astra. Each gets a cloud computer and a browser, carries context between conversations, handles several projects, and is reachable through ChatGPT, Slack, Teams and voice. Rolling out to Pro and Business Premium, with the first one included.

This is OpenAI's answer to the same idea as Grok Bot, so the same question applies: **a persistent teammate with its own computer is a different shape from a read only binder you control.** Good for work you would hand a person. Weaker for work that must be identical every time, which a prospecting brief is.

## Codex, if you work in a repo

Codex reads this kit's `AGENTS.md` already, plus skills from `.agents/skills` or `~/.agents/skills`. Nothing to convert.

Codex Cloud environments are worth knowing even if you do not use them, because the credential design is stricter than ours: **secrets are decrypted only for the setup script and stripped before the agent phase runs**, so the agent cannot echo them. Agent internet access is off by default with a per environment allowlist through a proxy.

- Skills: https://developers.openai.com/codex/skills
- Cloud environments: https://learn.chatgpt.com/docs/environments/cloud-environment

## What transfers unchanged

The binder, the job description, the anti jobs, the playbook, the deliverable and `check_brief.py`. On OpenAI the first decision is no longer whether a managed path exists. It is which of the four you are doing.
