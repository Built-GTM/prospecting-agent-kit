# Deploy: OpenAI

**There is no single answer here.** OpenAI has three, aimed at different people, and picking the wrong one is the main way this goes badly.

Two dates that matter before you build anything: the **Assistants API was shut off on 26 August 2026**, hard, with no read only mode. And **Agent Builder shuts down on 30 November 2026**. If you find a tutorial using either, it is out of date.

| Path | For | Runs |
|---|---|---|
| **Workspace Agents** | a Sales Operator. Start here | ChatGPT Business, Enterprise, Edu |
| **Codex Cloud** | a developer, repo shaped work | OpenAI container |
| **Agents SDK** | an engineer who wants control | your infrastructure, your sandbox vendor |

"Runs" is where the agent lives once it is built. Workspace Agents live inside your company's ChatGPT plan, so what you need is that plan and an administrator willing to switch agents on. Codex Cloud lives on a computer OpenAI creates for each job. The Agents SDK lives wherever you put it, which means you are hosting software and keeping it running.

**Before any of the three: fill the binder.** The onboarding binder (context pack) is the set of markdown files that tell the agent about your business. `context-pack-template/` in this kit holds the blank ones, `example-pack/` holds a finished set for a real company, and `SETUP.md` step 2 walks through filling your own. The job description (prompt) is `system-prompt.md`, also in this kit. Both are plain markdown, and both move to any of the three paths unchanged.

## Workspace Agents, the one you probably want

Closest thing to the show's build, and the flow is almost the same shape.

**Start by checking that agents are switched on.** An administrator has to enable them for the whole workspace, and until that happens the builder does not appear for anyone, including you. The admin setup page is linked at the end of this section. If you are not the administrator, that link is the thing to send them.

1. **Describe the job in the builder chat.** You talk to the builder the way you talk to ChatGPT, and it drafts a workflow and instructions for you to edit. Paste the objective and all the anti jobs from `system-prompt.md`: the `# Objective` section at the top of the file, and the whole `# Rules` section. Open the file in any text editor, copy those two sections whole, and paste them in as they are. Do not summarise them. The wording is the product.
2. **Add connectors, and choose the auth model.** A connector is a link between the agent and another account your company already uses, set up once. This is the best piece of vocabulary any vendor has produced: **"end user account"** means each person authenticates as themselves, **"agent owned account"** means a service account everyone shares. Your calendar is the first. Your team's shared drive is the second. Get this wrong and you have either an agent nobody can use or one that sees more than it should.
3. **Add skills.** Workspace agent skills use the same open source `SKILL.md` standard this kit already uses, so `skills/four-whys-research/SKILL.md` goes across as is. Hand the builder that file where it asks for skills. Nothing needs converting first. Then type the budget line into the instructions as well:

   > Budget: about 15 searches or page reads per brief. Stop sooner once you have one good reason. A strong signal beats a dossier.

   It is already in the skill file. Say it twice anyway. The builder rewrites your instructions as you go, and a number is the easiest thing in them to lose.
4. **The binder** goes in a connected drive, or as skill resources. Skill resources are files you attach next to a `SKILL.md` so the agent gets them whenever it uses that skill. Memory here is a persistent per user folder the agent writes to, so it is **not** the read only mount Claude gives you. Same drift warning as the Grok build: keep the copy you trust somewhere the agent cannot reach, and re-copy it in, rather than letting the agent's own copy accumulate edits nobody made on purpose.
5. **Preview, or Try in ChatGPT**, with action traces and reasoning visible. An action trace is the list of what the agent actually did, in order. It is what you read when a brief comes back wrong, and it is the difference between fixing the instructions and guessing at them.
6. **Schedule**, with the Schedule button. That is the desk (deployment): the agent running on a timer, without a person starting it.

Before anyone else uses it, run the ride along (evals). A case is one company URL, one LinkedIn profile URL, and what you already know the right answer looks like. The kit ships no cases on purpose, and `README.md` says why. Save a brief to a file and score it with `evals/check_brief.py`, which runs in a terminal on your own computer rather than anywhere on the platform.

OpenAI has published a cookbook that builds a **sales meeting prep agent** this exact way, step by step. It is the closest thing to an official walkthrough of the method in this kit, on a platform we did not build it for: https://developers.openai.com/cookbook/articles/chatgpt-agents-sales-meeting-prep

Admin setup, because agents are off until an admin enables them: https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business

## Codex, if you work in a repo

Codex reads `AGENTS.md` at the root of this kit already, plus skills from `.agents/skills` or `~/.agents/skills`. Nothing to convert. The root of the kit is the top level of the unzipped folder, the level that holds `README.md`. The `~` is your home folder, so `~/.agents/skills` sits in your own account rather than in the kit, and anything you put there is available to every project you open.

Codex Cloud environments are worth knowing about even if you do not use them, because their credential design is stricter than ours: **secrets are decrypted only for the setup script and stripped before the agent phase runs**, so the agent cannot echo them. In plain terms, a run happens in two parts. The first part installs what the job needs and is allowed to see your keys. The second part is the agent doing the work, and by then the keys are off the machine. Agent internet access is off by default with a per environment allowlist through a proxy, which means the agent reaches only the addresses you named in advance. For this agent, which lives on web search and page reading, that allowlist is the setting you will spend your time on.

- Skills: https://developers.openai.com/codex/skills
- Cloud environments: https://learn.chatgpt.com/docs/environments/cloud-environment

## Agents SDK, if you want to own the runtime

Bring your own sandbox, meaning you pick the service that creates the throwaway computer each run happens on. Built in support for Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop and Vercel, plus configurable memory and filesystem tools. You host it, you keep the conversation history, you choose the runtime.

This is a real answer and an engineering project. Do not start here.

https://openai.github.io/openai-agents-python/

## What transfers unchanged

The binder, the job description, the anti jobs, the playbook (skills), the deliverable (contract) and `check_brief.py`. Only the deploy differs, and on OpenAI the first decision is which of the three deploys you are even doing.
