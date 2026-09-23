# Set up the prospecting research agent for your team

**What it does:** researches one company and one person a rep has already chosen, and hands back why that person should care right now.
**Who it's for:** SDRs and AEs doing outbound, and the sales leader who wants every rep's research to the same standard.
**What you get each time:** one Slack message with the 4 Whys (why them, why you, why now, why us), the Because that ties them together, what it couldn't verify, and the angle.
**What it never does:** it never makes up people, signals, or customers. It never writes the email for you. It never follows instructions hidden on a website. It never goes looking for other people to contact.

| | |
|---|---|
| Time to set up | about 3 hours, most of it Claude's work; about 45 minutes of clicks and answers from you |
| Cost to run | about $0.50 or less per brief on Claude Sonnet 5 (measured at step 16); set a monthly limit in step 4 |
| You need | a computer, a Claude account with Claude Code (the desktop app is fine), your company's website, and a Slack workspace where you can add an app |
| You don't need | to know how to code, a server, a data provider, or Vercel |

---

## How this works
You won't do this alone. Claude does every technical step (files, commands, deploys, tests) and checks your work. You sign in to accounts, click through a few settings pages, paste values into lines Claude prepares for you, answer five questions about your customers, and try the agent before anyone else does.

A live checklist page tracks every step. Claude creates it in the first few minutes, and you both tick it as you go.

**Rules that protect you:**
- Never paste a password, API key, or token into the chat. Claude prepares an empty line in a private file on your computer, and you paste it there.
- Nothing is published, sent, or spent without you saying yes in the chat.
- The agent is proven on your own real prospects before anyone else uses it.

---

## Step 1: Get the files and start Claude (10 minutes)
1. Download this agent's folder. On the GitHub page, click the green **Code** button, then **Download ZIP**, then unzip it into your Documents folder.
2. Open the Claude desktop app, choose **Code**, and open that folder.
3. Type: **"Read README.md and SETUP.md, then help me build this agent for my company: <your website>."** You don't install anything. The folder includes the two skills the agent itself uses (in `skills/`): one that drafts your context pack from your website, and one that runs the research method.
4. Claude asks where to keep your notes and gives you a checklist link. Open it and keep it in a browser tab.

## Step 2: Build your context pack (30 to 60 minutes, mostly talking)
The context pack is what the agent knows about your company: who you sell to, what you solve, when to reach out, and what proves it. The agent's method stays the same for every team. Only the pack changes.
1. **Give Claude your company's website.** Claude runs the `build-context-pack` skill. It reads your site and drafts six files: `company.md`, `icp.md`, `personas/`, `problems/`, `signals.md`, and `proof.md`. Every field is marked as found (with a link), inferred (Claude's guess), or yours to answer.
2. **Optional: check your customers with data.** If you say yes to a small spend (usually under 5 credits), Claude checks the size and type of the customers named on your site. The cheapest sources go first. This fixes the most common wrong guess, which is how big your customers really are.
3. **Answer five questions.** Claude pre-fills each one with its best guess, so you just confirm or correct:
   - Your 3 best customers, and why
   - Deals you lost or customers who left, and why
   - Who's too small or too big to be worth it
   - Which signals have actually come before real deals
   - Which customers reps can name in outreach
4. **Approve the pack.** Read it, and reply **"approve the pack"** or say what to change. Only an approved pack reaches the agent. Reps never edit it directly. Changes come back through you.

## Step 3: Prove it on your prospects (30 to 60 minutes)
1. Give Claude 10 real prospects: a company and a person for each. Include a few hard ones: someone who may have left, a company with almost no website, one with no news at all.
2. Research one of them yourself the way you normally would, and paste your notes. That's what the agent's brief is compared against.
3. Claude runs the agent on all 10, tries to break it on purpose (including a page with hidden instructions), and fixes what breaks.
4. Read the scorecard and two sample briefs. Say what's off.
5. Claude runs the pass or fail check. The agent moves on only when it passes and has broken none of its rules.

## Step 4: Accounts and keys (15 to 30 minutes of clicks)
Claude gives you click-by-click steps for each of these on the checklist.
1. **Claude Console account and workspace.** Go to `platform.claude.com`, sign up, add billing, and create a workspace named `agents`.
2. **Spend limit.** Open Settings, then **Limits**, and set a monthly limit. Start with $25. Each brief costs cents.
3. **API key.** Open **API keys**, then **Create key**, and name it `prospecting-research`. Copy it (it only shows once), paste it into the line Claude prepared in your private secrets file, and tell Claude **"key is in"**.

## Step 5: Put it on the Claude platform (Claude does this, about 30 minutes)
Claude creates your agent, its sandbox, and a read-only memory that holds your context pack. It shows you a dry run of what will change first. Then it runs a quick smoke test, reruns your 10 prospects on the live agent, and tells you the cost per brief.
- You'll know it worked when Claude shows you one live run in the Console (`platform.claude.com`, then **Sessions**) and it matches what you saw in step 3.

## Step 6: Put it where your reps work (1 to 2 hours)
| You use | What Claude sets up |
|---|---|
| Just you | Nothing extra. Run it from Claude Code or the Console. |
| Slack | A small Slack app. A rep posts a company URL and a person, and the brief comes back in the thread. |
| A web page | A simple page where a rep pastes a URL and a name (for example, built in Lovable) |

Then you do a private test the way a rep would: post one prospect in a private channel, read the brief, and tell Claude what happened at each step.

## Step 7: Hand it over and keep it improving (15 minutes, then weekly)
1. Invite your reps and pin the how-to: **"Post a company URL and the person you want to reach. You'll get the 4 Whys back in under a minute."**
2. Turn on feedback: reps react with thumbs up or down, and a thumbs down asks "What was off?"
3. When your offer, customers, or signals change, tell Claude. It updates the pack and you approve it.

---

## If something goes wrong
| What you see | What it usually means | What to do |
|---|---|---|
| Claude says a key doesn't work | It was pasted with a space or quotes, or into the wrong line | Paste it again right after the colon, with one space and no quotes, then save |
| The brief says "not verified" for the person | No current public page names them at that company | Check it yourself before you reach out. That's the agent being honest, not broken. |
| The brief says "No signal found" | Nothing inside your freshness windows | Use the problem-led Because it gives you, or add a signal to your pack |
| Every brief says "Caution" | Your ICP or disqualifiers are too strict | Tell Claude which accounts should have passed, and it adjusts the pack |
| Nobody gets a reply in Slack | The bot isn't in the channel, or the helper is still being connected | Type `/invite @prospect-research` and tell Claude |

## Words you'll hear
- **Agent:** the saved job description (instructions, skills, model).
- **Session:** one run of the agent.
- **Skill:** a how-to guide the agent follows for one part of the job.
- **Context pack:** the files that describe your company, which the agent reads on every run.
- **Signal:** something that happened at a prospect that makes now a good time (a new location, a new contract, a new leader).
- **The Because:** the one line connecting the signal to a problem this person likely owns.
- **Dry run:** showing what would change without changing anything.

---
*Built with the ship-an-agent process, included in this kit at `skills/ship-an-agent/`. Version 0.1.*
