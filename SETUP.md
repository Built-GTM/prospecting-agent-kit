# Set up the prospecting research agent for your team

**What it does:** researches one company and one person a rep has already chosen, and hands back why that person should care right now.
**Who it's for:** SDRs and AEs doing outbound, and the sales leader who wants every rep's research to the same standard.
**What you get each time:** the deliverable (contract), the same shape every run. One Slack message with the 4 Whys (why them, why you, why now, why us), the Because that ties them together, what it couldn't verify, and the angle.
**What it never does:** it never makes up people, signals, or customers. It never writes the email for you. It never follows instructions hidden on a website. It never goes looking for other people to contact.

| | |
|---|---|
| Time to set up | about 3 hours, most of it Claude's work; about 45 minutes of clicks and answers from you |
| Cost to run | about $0.50 or less per brief on Claude Sonnet 5, measured on real runs rather than estimated; set a monthly limit in step 4 |
| You need | a computer, a Claude account with Claude Code (the desktop app is fine), your company's website, and a Slack workspace where you can add an app (this usually needs admin rights, so check before you start) |
| You don't need | to know how to code, a server, a data provider, or Vercel |

---

## How this works
You won't do this alone. Claude does every technical step (files, commands, deploys, tests) and checks your work. You sign in to accounts, click through a few settings pages, paste values into lines Claude prepares for you, answer five questions about your customers, and try the agent before anyone else does.

A live checklist page tracks every step. Claude creates it in the first few minutes and posts the link in the chat, and you both tick it as you go.

**Rules that protect you:**
- Never paste a password, API key, or token into the chat. Claude prepares an empty line in a private file on your computer and tells you that file's name, and you paste it there.
- Nothing is published, sent, or spent without you saying yes in the chat.
- The agent is proven on your own real prospects before anyone else uses it.

---

## Step 1: Get the files and start Claude (10 minutes)
1. Download this agent's folder. You are reading this on GitHub. Near the top of the page there is a green **Code** button. Click it, click **Download ZIP**, then unzip the file your browser saved (double-click it on a Mac, right-click it and choose **Extract All** on Windows) and move the unzipped folder into your Documents folder.
2. Open that folder with whichever coding agent you use: a coding agent is a chat window that can read and write files on your computer. Claude Code (desktop app, choose **Code**, then open the folder), Codex, Cursor, Windsurf, or a terminal agent. The kit is markdown (plain text files ending in `.md`) plus one Python script, so nothing here is tied to one vendor. If your tool cannot open a local folder, see "Using this without file access" in `README.md`.
3. Type this into the agent's chat box, with your company's web address in place of `<your website>`, angle brackets and all: **"Read README.md and SETUP.md, then help me build this agent for my company: <your website>."** You don't install anything. The folder includes the two playbooks (skills) the agent itself uses (in `skills/`): one that drafts your onboarding binder (context pack) from your website, and one that runs the research method.
4. Claude asks where to keep your notes and posts a checklist link in the chat. Click it to open it in your browser and leave that tab open.

## Step 2: Build your context pack (30 to 60 minutes, mostly talking)
The binder is what the agent knows about your company: who you sell to, what you solve, when to reach out, and what proves it. The agent's method stays the same for every team. Only the binder changes.
1. **Give Claude your company's website.** Paste the web address into the chat. Claude runs the `build-context-pack` playbook. It reads your site and drafts six files, in a folder it creates for you: `company.md`, `icp.md`, `personas/`, `problems/`, `signals.md`, and `proof.md`. The two with a slash are folders, one file per persona and per problem. Every field is marked as found (with a link), inferred (Claude's guess), or yours to answer.
2. **Optional: check your customers with data.** If you say yes to a small spend (usually under 5 credits), Claude checks the size and type of the customers named on your site. The cheapest sources go first. This fixes the most common wrong guess, which is how big your customers really are.
3. **Answer five questions,** in the chat. Claude pre-fills each one with its best guess, so you confirm or correct it. A good answer names names and uses your customers' own words, not adjectives:
   - Your 3 best customers, and why: the three company names, and the reason each one gave for buying
   - Deals you lost or customers who left, and why: the pattern you keep seeing, not one bad week
   - Who's too small or too big to be worth it: a headcount, a revenue band, or a situation you can point at
   - Which signals have actually come before real deals: what happened at the account in the weeks before they talked to you
   - Which customers reps can name in outreach: the list a rep can put in an email without asking anyone first
4. **Approve the binder.** Read the six files, then reply in the chat with **"approve the pack"** or say what to change. Only an approved binder reaches the agent. Reps never edit it directly. Changes come back through you.

## Step 3: Prove it on your prospects (30 to 60 minutes)
1. Give Claude 10 real prospects: paste a company web address and a person's LinkedIn address for each. Include a few hard ones: someone who may have left, a company with almost no website, one with no news at all.
2. Research one of them yourself the way you normally would, and paste your notes into the chat. That's what the agent's brief is compared against.
3. Claude runs the agent on all 10, tries to break it on purpose (including a page with hidden instructions), and fixes what breaks.
4. Read the scorecard and two sample briefs. Say what's off.
5. Claude runs the ride along (evals), the pass or fail check. The agent moves on only when it passes and has broken none of its rules.

## Step 4: Accounts and keys (15 to 30 minutes of clicks)
These are the keys (tools and connections): without them the agent can describe the job but not do it. Claude gives you click-by-click steps for each of these on the checklist.
1. **Claude Console account and workspace.** In your web browser, go to `platform.claude.com`, sign up, add billing, and create a workspace named `agents`.
2. **Spend limit.** In that Console, open Settings, then **Limits**, and set a monthly limit. Start with $25. Each brief costs cents.
3. **API key.** In the same Console, open **API keys**, then **Create key**, and name it `prospecting-research`. Copy it; it only shows once. Claude has already made a private file on your computer with an empty line waiting for the key, and told you where that file is. Open that file in any text editor, paste the key after the colon, save the file, and tell Claude **"key is in"**. The key never goes in the chat.

## Step 5: Put it on the Claude platform (Claude does this, about 30 minutes)
**The desk (deployment).** Claude creates your agent, its sandbox, and a read-only memory that holds your binder. It shows you a dry run of what will change first. Then it runs a quick smoke test, reruns your 10 prospects on the live agent, and tells you the cost per brief.
- You'll know it worked when Claude shows you one live run in the Console (`platform.claude.com`, then **Sessions**) and it matches what you saw in step 3.

## Step 6: Put it where your reps work (1 to 2 hours)
| You use | What Claude sets up |
|---|---|
| Only you | Nothing extra. Run it from Claude Code or the Console. |
| Slack | A small Slack app. A rep posts a company URL and a person, and the brief comes back in the thread. |
| A web page | A simple page where a rep pastes a URL and a name (for example, built in Lovable) |

Then you do a private test the way a rep would: post one prospect in a channel only you can see, read the brief, and tell Claude what happened at each step.

## Step 7: Hand it over and keep it improving (15 minutes, then weekly)
1. Invite your reps and pin the how-to: **"Post a company URL and the person you want to reach. You'll get the 4 Whys back in under a minute."**
2. Turn on feedback: reps react with thumbs up or down, and a thumbs down asks "What was off?"
3. When your offer, customers, or signals change, tell Claude. It updates the binder and you approve it.

---

## If something goes wrong
| What you see | What it usually means | What to do |
|---|---|---|
| Claude says a key doesn't work | It was pasted with a space or quotes, or into the wrong line | Open the secrets file again, paste the key right after the colon, with one space and no quotes, then save |
| The brief says "not verified" for the person | No current public page names them at that company | Check it yourself before you reach out. That's the agent being honest, not broken. |
| The brief says "No signal found" | Nothing inside your freshness windows | Use the problem-led Because it gives you, or add a signal to your binder |
| Every brief says "Caution" | Your ICP or disqualifiers are too strict | Tell Claude which accounts should have passed, and it adjusts the binder |
| Nobody gets a reply in Slack | The bot isn't in the channel, or the helper is still being connected | Type `/invite @prospect-research` in that Slack channel's message box, then tell Claude |

## Words you'll hear
- **Agent:** the whole worker, saved. Its job description (prompt), its playbook, its keys, and the model it runs on.
- **Session:** one run of the agent.
- **Skill:** the playbook. A how-to guide the agent follows for one part of the job.
- **Context pack:** the onboarding binder. The files that describe your company, which the agent reads on every run.
- **Signal:** something that happened at a prospect that makes now a good time (a new location, a new contract, a new leader).
- **The Because:** the one line connecting the signal to a problem this person likely owns.
- **Dry run:** showing what would change without changing anything.

---
*Built with the ship-an-agent process, included in this kit at `skills/ship-an-agent/`. Version 0.1.*
