# Deploy: OpenAI

**There is no single answer here.** OpenAI has three, aimed at different people, and picking the wrong one is the main way this goes badly.

Two dates that matter before you build anything: the **Assistants API was shut off on 26 August 2026**, hard, with no read only mode. And **Agent Builder shuts down on 30 November 2026**. If you find a tutorial using either, it is out of date.

| Path | For | Runs |
|---|---|---|
| **Workspace Agents** | a Sales Operator. Start here | ChatGPT Business, Enterprise, Edu |
| **Codex Cloud** | a developer, repo shaped work | OpenAI container |
| **Agents SDK** | an engineer who wants control | your infrastructure, your sandbox vendor |

## Workspace Agents, the one you probably want

Closest thing to the show's build, and the flow is almost the same shape.

1. **Describe the job in the builder chat.** It drafts a workflow and instructions, and you edit them. Paste the objective and all the anti jobs from `system-prompt.md`.
2. **Add connectors, and choose the auth model.** This is the best piece of vocabulary any vendor has produced: **"end user account"** means each person authenticates as themselves, **"agent owned account"** means a service account everyone shares. Your calendar is the first. Your team's shared drive is the second. Get this wrong and you have either an agent nobody can use or one that sees more than it should.
3. **Add skills.** Workspace agent skills use the same open source `SKILL.md` standard this kit already uses, so `skills/four-whys-research/SKILL.md` goes across as is. Remember to type the budget line in.
4. **The binder** goes in a connected drive, or as skill resources. Memory here is a persistent per user folder the agent writes to, so it is **not** the read only mount Claude gives you. Same drift warning as the Grok build.
5. **Preview, or Try in ChatGPT**, with action traces and reasoning visible.
6. **Schedule**, with the Schedule button.

OpenAI has published a cookbook that builds a **sales meeting prep agent** this exact way, step by step. It is the closest thing to an official walkthrough of the method in this kit, on a platform we did not build it for: https://developers.openai.com/cookbook/articles/chatgpt-agents-sales-meeting-prep

Admin setup, because agents are off until an admin enables them: https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business

## Codex, if you work in a repo

Codex reads `AGENTS.md` at the root of this kit already, plus skills from `.agents/skills` or `~/.agents/skills`. Nothing to convert.

Codex Cloud environments are worth knowing about even if you do not use them, because their credential design is stricter than ours: **secrets are decrypted only for the setup script and stripped before the agent phase runs**, so the agent cannot echo them. Agent internet access is off by default with a per environment allowlist through a proxy.

- Skills: https://developers.openai.com/codex/skills
- Cloud environments: https://learn.chatgpt.com/docs/environments/cloud-environment

## Agents SDK, if you want to own the runtime

Bring your own sandbox. Built in support for Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop and Vercel, plus configurable memory and filesystem tools. You host it, you keep the conversation history, you choose the runtime.

This is a real answer and an engineering project. Do not start here.

https://openai.github.io/openai-agents-python/

## What transfers unchanged

The binder, the job description, the anti jobs, the playbook, the deliverable and `check_brief.py`. Only the deploy differs, and on OpenAI the first decision is which of the three deploys you are even doing.
