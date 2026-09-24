# Which platform you build on, and what changes

Nothing in this process is tied to one vendor. The method, the pack, the contract and the eval gate are the same everywhere. Only two steps differ: where you *work* while building, and where the finished agent *runs*.

Decide both at "Before anything else: where things go", and write them at the top of `BUILD-STATE.md`.

## 1. Where you work while building

You need something that can read a folder of markdown and edit it with you.

| Tool | How to open the build folder | Notes |
|---|---|---|
| **Claude Code** | Desktop app, choose Code, open the folder | Loads `skills/*/SKILL.md` on its own |
| **Codex** | Open the folder as a workspace | Reads `AGENTS.md` at the repo root on its own |
| **Cursor, Windsurf** | File, Open Folder, then the chat pane | Point it at `AGENTS.md` if it does not find it |
| **A terminal agent** (Gemini CLI and similar) | `cd` into the folder and start it there | |
| **A chat window with no file access** (Grok, ChatGPT, Claude.ai) | Paste, see below | Works, just slower |

**Only Claude Code auto-loads skill files.** Everywhere else, paste the contents of the relevant `SKILL.md` into the chat at the step that needs it. The method does not change, only the loading.

### Building from a chat window with no file access
You never need more than four things in the window at once. Paste in this order:

1. The system prompt, as the system prompt, custom instruction, or persona
2. The context pack files, as one message, each under a heading with its filename
3. The one skill the current step needs
4. The actual input

Keep the pack in a Google Doc, a Sheet or a Notion page and paste the current version each session. When the pack changes, you repaste. That is the whole cost of working this way.

## 2. Where the finished agent runs

This is the deploy step, and it is the only genuinely platform-specific part.

| Where | What you get | What it costs |
|---|---|---|
| **A managed agent** (Claude, and the equivalents other platforms ship) | One place to change the prompt, the pack and the permissions. Sessions you can read back. Credentials held once | You are on that platform |
| **An automation tool** (n8n, Make, Zapier) | Runs next to everything else you automate | The prompt lives inside a node, so you re-teach it in every node you copy it into |
| **Your own code** | Total control | You own the hosting, the keys and the upgrades |
| **A chat window** | Zero setup, good for proving the method | Nobody else on the team gets it |

**The argument for managed, stated plainly:** when your offer changes, you want to edit one thing. Anything that copies the prompt into several places turns a five minute change into an afternoon.

## What is portable, always
- The context pack. Plain text, in whatever tool you like.
- The system prompt. Paste it wherever the platform takes instructions.
- The contract. It is a list of rules, not a feature.
- The eval set and the checker. If your checker is a plain script with no dependencies, it runs anywhere.
- This process.

## What is not
- Skill auto-loading, which is a Claude Code convention.
- The deploy screen, the memory store, the credential vault and the session log. Every platform names these differently or lacks them. The concepts survive the move, the clicks do not.

Do not let the platform choice block the build. Steps 1 through 12 are the same wherever you work, and they are most of the work.
