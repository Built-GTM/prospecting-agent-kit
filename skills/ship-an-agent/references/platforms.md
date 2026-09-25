# Which platform you build on, and what changes

**Researched on 2026-09-25, from the vendors' own docs.** This is the fastest moving part of the whole process. Two of the dates below are products that were switched off inside a year of launch. Read the vendor's current page before you trust any specific claim here, and treat anything older than a few months as a rumour.

The seven parts, and their technical names: the job description (prompt), the onboarding binder (context pack), the playbook (skills), the keys (tools and connections), the deliverable (contract), the ride along (evals), the desk (deployment). The table and the frame behind them are in `SKILL.md`.

**The short version: the binder is yours, the deploy is the platform's.** Steps 1 to 12 are the same wherever you work. Three things change near the end: the keys, where the binder lives, and the desk.

## The formats are the portable part

This is not an argument from principle. It is what the docs say today.

The two file types this process produces, `SKILL.md` for each page of the playbook and `AGENTS.md` at the root of the folder, are read by Claude Code, Codex and Grok Build. The same file, in the same format, with no conversion and no export step.

| Tool | Where it looks for playbook files | Instruction file it reads |
|---|---|---|
| **Claude Code** | `skills/` and `.claude/skills/` in the folder it opens | `CLAUDE.md`, and `AGENTS.md` |
| **Codex** | `.agents/skills` in the project, or `~/.agents/skills` for every project | `AGENTS.md` at the repo root |
| **Grok Build** | `.grok/skills/` in the project, or `~/.grok/skills/` for every project | `AGENTS.md`, and it also reads `CLAUDE.md` and `.claude/` |

The `~` is your home folder, so the second path in each row makes a playbook available to every project you open rather than to one folder.

The binder is plain markdown and the deliverable is a list of rules, so neither has a format question to answer at all. The one piece of this kit that is a convention rather than a standard is **automatic** skill loading: Claude Code picks the files up on its own, and elsewhere you point the tool at the file or paste it at the step that needs it. The content does not change, only the loading.

## 1. Where you work while building

You need something that can read a folder of markdown and edit it with you.

| Tool | How to open the build folder | Notes |
|---|---|---|
| **Claude Code** | Desktop app, choose Code, open the folder | Loads `skills/*/SKILL.md` on its own |
| **Codex** | Open the folder as a workspace | Reads `AGENTS.md` at the repo root on its own |
| **Grok Build** | Open the folder as a project | Reads `AGENTS.md`, and `CLAUDE.md` and `.claude/` as well |
| **Cursor, Windsurf** | File, Open Folder, then the chat pane | Point it at `AGENTS.md` if it does not find it |
| **A terminal agent** (Gemini CLI and similar) | `cd` into the folder and start it there | |
| **A chat window with no file access** (ChatGPT, Grok, Claude.ai) | Paste, see below | Works, at the cost of repasting |

### Building from a chat window with no file access

You never need more than four things in the window at once. Paste in this order:

1. The job description, as the system prompt, custom instruction, or persona
2. The binder files, as one message, each under a heading with its filename
3. The one page of the playbook the current step needs
4. The actual input

Keep the binder in a Google Doc, a Sheet or a Notion page and paste the current version each session. When the binder changes, you repaste. That is the whole cost of working this way.

## 2. Where the finished agent runs: the desk

| Where | What you get | What it costs |
|---|---|---|
| **A managed agent** (Claude, and the equivalents other vendors ship) | One place to change the job description, the binder and the permissions. Sessions you can read back. Keys held once | You are on that platform |
| **An automation tool** (n8n, Make, Zapier) | Runs next to everything else you automate | The job description lives inside a node, so you re-teach it in every node you copy it into |
| **Your own code** | Total control | You own the hosting, the keys and the upgrades |
| **A chat window** | Zero setup, good for proving the method | Nobody else on the team gets it |

**The argument for managed, stated plainly:** when your offer changes, you want to edit one thing. Anything that copies the job description into several places turns a five minute change into an afternoon.

This kit's `deploy/` folder has one page per platform for this step and nothing else: `deploy/claude.md` for Claude Managed Agents, `deploy/grok-bot.md` for xAI Grok Bot, `deploy/codex.md` for OpenAI, which has three separate answers depending on who you are.

## The three steps that genuinely change

### The keys

Every platform holds credentials differently, and two of them hold them in a way that changes the design rather than the clicks.

- **Codex Cloud** encrypts secrets and decrypts them only for the setup script, then strips them before the agent phase runs, so the agent cannot echo a key it never had. An agent that needs a live credential at run time, rather than at install time, needs a different design on that platform. Read step 8 again before you assume a connection is available.
- **Grok Bot has no per agent vault at all.** Every Bot on an account shares one cloud computer, along with its browser sessions and its logins. Anything one Bot signs into, the others can reach. That is a reason to keep a Bot read only and to keep a person between it and any system of record.
- **Claude Managed Agents** hold credentials in a vault as `mcp_oauth`, `static_bearer` or `environment_variable`, scoped to the agent.

What survives the move in every case: the list of keys the agent needs, by name, and which of them a human has to approve. That list is step 8 output and it is platform neutral.

### The binder

A read only mounted binder, enforced by the platform, has no direct equal anywhere else.

- **Claude** mounts a memory store read only and enforces it, so the agent cannot edit its own facts.
- **On OpenAI**, the binder lives as files in the repo or in a connected drive. Workspace agent memory is a per user folder the agent writes to, which is not the same thing.
- **On xAI**, the Bot writes its own memory. That is the opposite of a binder you control, so keep the copy you trust somewhere the Bot cannot reach and re-sync it before a run.

The content is identical everywhere by definition, because it is what the agent knows about your business. There is one binder, and forking it per platform is how an agent ends up pitching a segment you stopped selling to.

### The desk

The biggest gap of the three. Schedules, run history, per run budgets and session traces are named differently on every platform, and some do not exist. The concepts survive the move, the clicks do not. Go to `deploy/` for the one page that covers yours.

## What the shutdowns teach

Two dates worth carrying, because they are the reason this process keeps the value in files.

- **The OpenAI Assistants API was shut off on 26 August 2026**, hard, with no read only mode. Anything built on `/v1/assistants` or `/v1/threads` stopped working that day. The replacement is the Responses API plus the Conversations API, which is an architecture change and not an endpoint swap: the object model is different, so code written against Assistants gets rewritten rather than repointed.
- **OpenAI Agent Builder shuts down on 30 November 2026**, under a year after it launched. If you find a tutorial using either product, it is out of date.

The lesson is not that one vendor is unreliable. It is that the visual builder layer is the least stable part of every vendor's stack, and the files are the stable part. A binder, a job description, a playbook and a checker written in markdown and plain Python outlived both products without being touched.

## What is portable, always

- The binder. Plain text, in whatever tool you like.
- The job description. Paste it wherever the platform takes instructions.
- The playbook. `SKILL.md` is read as is by Claude Code, Codex and Grok Build.
- The deliverable. It is a list of rules, not a feature.
- The ride along and its checker. A checker that is a plain script with no dependencies runs anywhere.
- This process.

## What is not

- Automatic skill loading, which is a Claude Code convention rather than a standard.
- The deploy screen, the memory mount, the credential vault and the session log.
- Any visual builder, on the evidence above.

Everything before those last three steps transfers unchanged. Do not let the platform choice block the build: steps 1 through 12 are the same wherever you work, and they are most of the work.
