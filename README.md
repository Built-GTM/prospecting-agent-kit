# Prospecting agent kit

Build the research agent from the show, for your own company.

Give it a company URL and one LinkedIn profile. It hands back why that person should care right now: a verdict, the Because, the 4 Whys with their sources, and what it could not verify. It does the homework. You still do the prospecting. It never writes the email.

---

## Start in 10 minutes

### 1. Get the files
**No GitHub account needed.** You are reading this page on GitHub. Near the top of the page there is a green **Code** button. Click it, then click **Download ZIP**. Your browser drops a zip file into your Downloads folder. Unzip it (double-click it on a Mac, right-click it and choose **Extract All** on Windows), then move the unzipped folder into your Documents folder. That folder is the kit. Everything below happens inside it.

Or, if you use git, run this in a terminal window, from wherever you want the kit folder to land:
```
git clone https://github.com/Built-GTM/prospecting-agent-kit.git
```

### 2. Open it with a coding agent
A coding agent is a chat window that can read and write files on your computer. Open the kit folder in whichever one you already use. You do not install anything and you do not need to know how to code.

| You use | How to open it |
|---|---|
| Claude Code | Open the desktop app, choose **Code**, then open the kit folder you unzipped |
| Codex | Open the folder as a workspace. It reads `AGENTS.md` at the root on its own |
| Cursor or Windsurf | **File, Open Folder**, pick the kit folder, then type in the chat pane |
| Gemini CLI, or any terminal agent | In a terminal window type `cd `, drag the kit folder onto the window to fill in its path, press Return, then start your agent there |
| A chat window with no file access (Grok, ChatGPT, Claude.ai) | See **Using this without file access** below |

Everything in this kit is markdown plus one Python script. Markdown files end in `.md` and hold plain text, so you can open any of them in TextEdit, Notepad, or any editor. Nothing here is specific to one vendor.

### 3. Paste this, with your own website in it
Paste it into your agent's chat box, with the kit folder open. Replace `<your website>`, angle brackets and all, with your company's web address.
```
Read README.md and SETUP.md in this folder.

I want to build the prospecting research agent for my company: <your website>

Start by following skills/build-context-pack/SKILL.md: read my site and draft
my six context pack files into a new folder called my-pack/. Mark every field
as found with a source, or inferred. Then ask me the five owner questions.
```

The agent reads your website and drafts your onboarding binder (context pack) into a new folder named `my-pack/`. You do not create that folder; the agent makes it inside the kit folder. It marks what it found with a link and what it guessed, so you can see the difference. Then it asks you five questions only you can answer.

### 4. Fill in the gaps
Answer the five questions in the chat. They take about twenty minutes and they are the difference between a brief that sounds like you and one that sounds like everyone else. Names and your customers' own words beat adjectives:
- Your three best customers, and why they bought. Name the three companies, and give the reason each one gave, not the reason you wish they had given
- Who you never win, and why. A pattern, not one bad week: a segment, a competitor, a budget line
- What each buyer is measured on. The number their own boss asks them about
- What customers say before they buy. The complaint in the words they used, off a call or a support ticket
- Which customers you are allowed to name. The list a rep can put in an email without asking anyone first

Three or four sentences per question is enough. A blank is the only wrong answer.

### 5. Run your first brief
Paste this into the same chat, with a real company web address and a real LinkedIn profile address in place of the two angle bracket lines:
```
Using system-prompt.md as your instructions and my-pack/ as the context pack,
research this prospect:
Company: <a company URL>
Person: <their LinkedIn profile URL>
```

Ask the agent to save the brief as a file in the kit folder, and note the filename. Then score it. Asking the agent to run the check is the shorter path. To run it yourself, open a terminal window in the kit folder and type this, with that filename in place of the angle brackets:
```
python3 evals/check_brief.py <the file you saved the brief in>
```

That script checks the brief 34 ways against the deliverable (contract): every claim carries a link, the person was verified or flagged, no invented customers, no outreach copy, within the word caps. It has no opinion about your work.

---

## What is in the box
Every name below is a folder or a file inside the kit folder.

| Folder | What it is |
|---|---|
| `SETUP.md` | The full walkthrough, written for someone who does not code |
| `context-pack-template/` | The six blank binder files: company, icp, personas, problems, signals, proof |
| `example-pack/` | A finished binder for a real company, built entirely from public pages. Read this first to see what good looks like |
| `system-prompt.md` | The job description (prompt). Method only, no company facts, so it works for any company |
| `skills/build-context-pack/` | Turns your website into a first draft of your binder |
| `skills/four-whys-research/` | The playbook (skills) for each Why: which sources to trust, how to check a person is still in the role, when to stop |
| `evals/check_brief.py` | The ride along (evals). The deliverable checker, 34 rules |
| `skills/ship-an-agent/` | **The whole 26 step process**, from idea to a live agent: the deliverable, the split, the ride along, the desk (deployment), the handover. This is the method behind everything above |
| `deploy/` | One page per platform for the last step only: Claude, Grok Bot, OpenAI. You open it only if you want the agent running without you. Everything above this row is the same wherever you run it |

## Building something other than a prospecting agent

`skills/ship-an-agent/` is the process itself, and it is not specific to prospecting. It walks 26 steps in six phases, one at a time, running a gate out loud at each one and waiting for you before it moves.

Paste this into the chat, with the kit folder open, and describe the job in place of the angle brackets:

```
Read skills/ship-an-agent/SKILL.md and walk me through building an agent
that <the job you want done>.
```

It will ask where your files should live, make you write the deliverable before the job description, force real test cases before you call it done, and refuse to let you skip the ride along. That is the point. `references/process.md` inside it is the full 26 steps if you would rather read than be walked.

## Running it somewhere else: Codex, Grok, Cursor, anything

**The kit is tool agnostic by design.** Markdown binder files, one system prompt, three skill files and a Python script. There is no vendor lock in the content.

### What is portable, and what is not
| Piece | Portable? |
|---|---|
| `context-pack-template/`, `example-pack/`, your own `my-pack/` | Yes. Plain markdown. Paste it, upload it, or point any agent at the folder |
| `system-prompt.md` | Yes. Paste its contents into the box your tool calls the system prompt, the custom instruction, or the persona. It is the standing instruction the agent reads before every run |
| `evals/check_brief.py` | Yes. Plain Python 3, no dependencies. `python3 evals/check_brief.py <file>` |
| `skills/*/SKILL.md` | The content is portable, the auto loading is not. Claude Code picks these up on its own. Everywhere else, open the file in a text editor and paste its contents into the chat when you need that step |
| Deploying it so it runs on a schedule | This is the only part that changes. See `deploy/` |

### Deploying it, when you want it running on its own

Most readers never open `deploy/`. If you run briefs one at a time, by pasting a prospect into a chat and reading what comes back, you are finished at step 5 and this folder is not for you. Open it when you want the agent running without you: on a schedule, from Slack, or for a whole team. Then read the one page for your platform and ignore the other two.

| File | Platform |
|---|---|
| `deploy/claude.md` | Claude Managed Agents. The one the show was built on, and the only one here that has actually run |
| `deploy/grok-bot.md` | xAI Grok Bot. Includes a paste ready block that builds the whole Bot in one go |
| `deploy/codex.md` | OpenAI, which has three different answers depending on who you are |

**There is no Grok binder, and there will not be one.** Here is the test: you change your ICP, how many files do you edit? With one binder, one. Fork it per platform and the answer is two, and the day you forget is the day one of your agents pitches a segment you stopped selling to.

The binder is what the agent knows about your business. That is identical everywhere by definition. Only the deploy differs.

### Using this without file access
If your tool cannot read a local folder, it only ever needs four things. Paste each one into the chat window, in this order. To copy a file, open it in any text editor, select all, and copy:

1. `system-prompt.md` as the system prompt or custom instruction
2. Your six binder files, as one message, each under a heading with its filename
3. `skills/four-whys-research/SKILL.md` as a second message
4. Then the company URL and the person's LinkedIn URL

That is the whole agent. Everything else in this repo is there to help you build the binder and check the output.

### Building a different agent this way
`skills/ship-an-agent/references/platforms.md` carries the same guidance for any agent build, not only this one: where to work, where to run it, what is portable and what is not.

### A note on skills
A "skill" here is a playbook: a markdown file describing a procedure. Claude Code loads them automatically from `skills/`. Codex reads `AGENTS.md` at the root, which points at the same files. Any other tool: paste the one you need. The method does not change.

## The one idea worth stealing
**Method in the agent, knowledge in the binder.** The prompt never mentions your company, so the day you change what you sell, or who you sell to, you edit six markdown files and nothing else. That is what lets one agent serve a whole team, and what stops you rebuilding it every quarter.

## Two things deliberately left out
**The research lookup script.** It points at a paid data route that needs its own credential. The agent works without it, on web search and page reading alone.

**The ride along cases.** They named real people at real companies who never agreed to be examples. Build your own instead: a few easy accounts, a few messy ones, some edge cases, a couple of deliberate attacks, and one where the right answer is to refuse. `check_brief.py` shows you the shape.

## Where it came from
Built live on Build Better, a Sell Better production, 23 September 2026. Almost none of the thinking is original: the signal types, the one level deeper check, the persona lens and the prompt structure all came from guests on the Daily Sales Show. The credits are in the deck.
