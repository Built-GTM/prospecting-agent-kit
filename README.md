# Prospecting agent kit

Build the research agent from the show, for your own company.

Give it a company URL and one LinkedIn profile. It hands back why that person should care right now: a verdict, the Because, the 4 Whys with their sources, and what it could not verify. It does the homework. You still do the prospecting. It never writes the email.

---

## Start in 10 minutes

### 1. Get the files
**No GitHub account needed.** Click the green **Code** button at the top of this page, then **Download ZIP**, then unzip it into your Documents folder.

Or, if you use git:
```
git clone https://github.com/Built-GTM/prospecting-agent-kit.git
```

### 2. Open it with a coding agent
Open that folder with whichever agent you already use. You do not install anything and you do not need to know how to code.

| You use | How to open it |
|---|---|
| Claude Code | Open the desktop app, choose **Code**, open the folder |
| Codex | Open the folder as a workspace. It reads `AGENTS.md` at the root on its own |
| Cursor or Windsurf | **File, Open Folder**, then use the chat pane |
| Gemini CLI, or any terminal agent | `cd` into the folder and start it there |
| A chat window with no file access (Grok, ChatGPT, Claude.ai) | See **Using this without file access** below |

Everything in this kit is markdown plus one Python script. Nothing here is specific to one vendor.

### 3. Paste this, with your own website in it
```
Read README.md and SETUP.md in this folder.

I want to build the prospecting research agent for my company: <your website>

Start by following skills/build-context-pack/SKILL.md: read my site and draft
my six context pack files into a new folder called my-pack/. Mark every field
as found with a source, or inferred. Then ask me the five owner questions.
```

The agent reads your website and drafts your pack. It marks what it found with a link and what it guessed, so you can see the difference. Then it asks you five questions only you can answer.

### 4. Fill in the gaps
Answer the five questions. They take about twenty minutes and they are the difference between a brief that sounds like you and one that sounds like everyone else:
- Your three best customers, and why they bought
- Who you never win, and why
- What each buyer is measured on
- What customers say before they buy
- Which customers you are allowed to name

### 5. Run your first brief
```
Using system-prompt.md as your instructions and my-pack/ as the context pack,
research this prospect:
Company: <a company URL>
Person: <their LinkedIn profile URL>
```

Then score it:
```
python3 evals/check_brief.py <the file you saved the brief in>
```

That script checks the brief 34 ways against the contract: every claim carries a link, the person was verified or flagged, no invented customers, no outreach copy, within the word caps. It has no opinion about your work.

---

## What is in the box
| Folder | What it is |
|---|---|
| `SETUP.md` | The full walkthrough, written for someone who does not code |
| `context-pack-template/` | The six blank files: company, icp, personas, problems, signals, proof |
| `example-pack/` | A finished pack for a real company, built entirely from public pages. Read this first to see what good looks like |
| `system-prompt.md` | The agent's instructions. Method only, no company facts, so it works for any company |
| `skills/build-context-pack/` | Turns your website into a first draft of your pack |
| `skills/four-whys-research/` | How to research each Why: which sources to trust, how to check a person is still in the role, when to stop |
| `evals/check_brief.py` | The contract checker, 34 rules |
| `skills/ship-an-agent/` | **The whole 26 step process**, from idea to a live agent: the contract, the split, the eval gate, the deploy, the handover. This is the method behind everything above |

## Building something other than a prospecting agent

`skills/ship-an-agent/` is the process itself, and it is not specific to prospecting. It walks 26 steps in six phases, one at a time, running a gate out loud at each one and waiting for you before it moves.

```
Read skills/ship-an-agent/SKILL.md and walk me through building an agent
that <the job you want done>.
```

It will ask where your files should live, make you write the contract before the prompt, force real test cases before you call it done, and refuse to let you skip the eval gate. That is the point. `references/process.md` inside it is the full 26 steps if you would rather read than be walked.

## Using this with Codex, Grok, Cursor or anything else

**The kit is already tool agnostic.** Six markdown files, one system prompt, three skill files and a Python script. There is no vendor lock in the content. Only the wording of the old instructions assumed one app, and that is now fixed.

### What is portable, and what is not
| Piece | Portable? |
|---|---|
| `context-pack-template/`, `example-pack/`, your own `my-pack/` | Yes. Plain markdown. Paste it, upload it, or point any agent at the folder |
| `system-prompt.md` | Yes. Paste it as the system prompt, custom instruction, or persona, whatever your tool calls it |
| `evals/check_brief.py` | Yes. Plain Python 3, no dependencies. `python3 evals/check_brief.py <file>` |
| `skills/*/SKILL.md` | The content is portable, the auto loading is not. Claude Code picks these up on its own. Everywhere else, paste the file's contents into the chat when you need that step |
| Deploying as a managed agent | Claude specific. Codex and other platforms have their own hosted agents. The pack and the prompt move across unchanged; only the deploy screen differs |

### Using this without file access
If your tool cannot read a local folder, it only ever needs four things. Paste them in this order:

1. `system-prompt.md` as the system prompt or custom instruction
2. Your six pack files, as one message, each under a heading with its filename
3. `skills/four-whys-research/SKILL.md` as a second message
4. Then the company URL and the person's LinkedIn URL

That is the whole agent. Everything else in this repo is there to help you build the pack and check the output.

### A note on skills
A "skill" here is just a markdown file describing a procedure. Claude Code loads them automatically from `skills/`. Codex reads `AGENTS.md` at the root, which points at the same files. Any other tool: paste the one you need. The method does not change.

## The one idea worth stealing
**Method in the agent, knowledge in the pack.** The prompt never mentions your company, so the day you change what you sell, or who you sell to, you edit six markdown files and nothing else. That is what lets one agent serve a whole team, and what stops you rebuilding it every quarter.

## Two things deliberately left out
**The research lookup script.** It points at a paid data route that needs its own credential. The agent works without it, on web search and page reading alone.

**The eval case set.** It named real people at real companies who never agreed to be examples. Build your own instead: a few easy accounts, a few messy ones, some edge cases, a couple of deliberate attacks, and one where the right answer is to refuse. `check_brief.py` shows you the shape.

## Where it came from
Built live on Build Better, a Sell Better production, 23 September 2026. Almost none of the thinking is original: the signal types, the one level deeper check, the persona lens and the prompt structure all came from guests on the Daily Sales Show. The credits are in the deck.
