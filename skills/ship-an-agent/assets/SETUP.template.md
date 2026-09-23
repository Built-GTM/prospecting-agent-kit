# Set up {{AGENT_NAME}} for your team

<!-- ship-an-agent: every agent ships this file as SETUP.md in its folder. Claude fills the {{...}} parts at step 9 and keeps it current through step 20. Written for someone who has never coded. Zero em dashes or en dashes. -->

**What it does:** {{ONE_SENTENCE_JOB}}
**Who it's for:** {{WHO_USES_IT}}
**What you get each time:** {{THE_ONE_OUTPUT}}
**What it never does:** {{MUST_NEVERS_IN_PLAIN_WORDS}}

| | |
|---|---|
| Time to set up | about {{SETUP_HOURS}} hours, most of it Claude's work; about {{YOUR_MINUTES}} minutes of clicks from you |
| Cost to run | about {{COST_PER_RUN}} per run on {{MODEL}}; set a monthly limit in step 4 |
| You need | a computer, a Claude account with Claude Code (desktop app is fine), and {{EXTRA_ACCOUNTS}} |
| You don't need | to know how to code, a server, or Vercel |

---

## How this works
You won't do this alone. Claude does every technical step (files, commands, deploys, tests) and checks your work. You sign in to accounts, click through a few settings pages, paste values into lines Claude prepares for you, answer questions about your team, and try the agent before anyone else does.

A live checklist page tracks every step. Claude creates it in the first few minutes; you both tick it as you go.

**Rules that protect you:**
- Never paste a password, API key, or token into the chat. Claude prepares an empty line in a private file on your computer; you paste there.
- Nothing is published, sent, or spent without you saying yes in the chat.
- The agent is proven on your own real examples before anyone else uses it.

---

## Step 1: Get the files and start Claude (10 minutes)
1. Download this agent's folder: {{HOW_TO_GET_FILES}} (for a GitHub repo: the green **Code** button, then **Download ZIP**, then unzip it into your Documents folder).
2. Open the Claude desktop app, choose **Code**, and open that folder.
3. Type: **"Set up this agent for my team using the ship-an-agent skill."** You don't install anything: the folder already includes every skill Claude needs to walk you through the build (in `.claude/skills/`) and every skill the agent itself uses (in `skills/`). Claude Code picks them up when you open the folder.
4. Claude asks where to keep your notes and gives you a checklist link. Open it and keep it in a browser tab.

## Step 2: Make it yours (30 to 60 minutes, mostly talking)
Claude asks you a few questions and fills in your team's details. It will not change the agent's safety rules; it can only add to them.
1. **Show Claude the problem on your team.** Share one real example ({{EXAMPLE_OF_A_REAL_INPUT}}). This proves the agent is worth setting up for you.
2. **Fill your profile.** Claude creates `memory-seed/{{PROFILE_FILE}}` and asks you for: {{PROFILE_FIELDS}}. Point it at anything it can read (a website, a spreadsheet export, past examples) and it fills in the rest for you to check.
3. **Approve the setup.** Claude shows a one-page summary of what the agent will do for your team. Reply **"approve the design"** or say what to change.

## Step 3: Prove it on your examples (30 to 60 minutes)
1. Send Claude {{N_EXAMPLES}} real inputs from your team, one at a time or together.
2. Claude runs the agent on each one, tries to break it on purpose, and fixes what breaks.
3. Read the scorecard and two sample outputs Claude shows you. Say what's off.
4. Claude runs the pass or fail check. The agent moves on only when it passes and has broken none of its rules.

## Step 4: Accounts and keys (15 to 30 minutes of clicks)
Claude gives you click-by-click steps for each of these on the checklist.
1. **Claude Console account and workspace.** Go to `platform.claude.com`, sign up, add billing, create a workspace named `agents`.
2. **Spend limit.** Settings, then **Limits**, set a monthly limit (start with {{SUGGESTED_LIMIT}}).
3. **API key.** **API keys**, then **Create key**, name it `{{SLUG}}`. Copy it (it shows once) and paste it into the line Claude prepared in your private secrets file. Tell Claude **"key is in"**.
{{EXTRA_ACCOUNT_STEPS}}

## Step 5: Put it on the Claude platform (Claude does this, about 30 minutes)
Claude creates your agent, its sandbox, its memory, and any locked credential boxes (vaults), always showing a dry run of what will change first. Then it runs a quick smoke test and reruns your examples on the live agent, and tells you the cost per run.
- You'll know it worked when: Claude shows you one live run in the Console (`platform.claude.com`, **Sessions**) and it matches what you saw in step 3.

## Step 6: Put it where your team works (1 to 2 hours)
Claude asks where people will use it and what tools you already have, then picks the simplest option:
| You use | What Claude sets up |
|---|---|
| Just you | Nothing extra: run it from Claude Code or the Console |
| {{SURFACE_OPTIONS}} |

Then you do a private test the way a real user would ({{PRIVATE_TEST}}), and tell Claude what happened at each step.

## Step 7: Hand it over and keep it improving (15 minutes, then weekly)
1. Invite your team and pin the short how-to Claude writes: {{HOW_TO_USE_IN_ONE_LINE}}.
2. Turn on feedback: people react with thumbs up or down; a thumbs down asks "What was off?".
3. Optional: the weekly agent coach reads each week's use and proposes improvements. Nothing changes without your approval.

---

## If something goes wrong
| What you see | What it usually means | What to do |
|---|---|---|
| Claude says a key doesn't work | It was pasted with a space or quotes, or into the wrong line | Paste it again right after the colon, one space, no quotes, and save |
| The agent says it can't read something | That site blocks automated reading | Paste the text instead; the agent asks for it |
| Nobody gets a reply in Slack | The bot isn't in the channel, or the helper is still being connected | Type `/invite @{{BOT_NAME}}` and tell Claude |
| Costs are higher than expected | Longer runs or a stronger model | Ask Claude to show cost per run and suggest a cheaper setup |
{{AGENT_SPECIFIC_TROUBLESHOOTING}}

## Words you'll hear
- **Agent:** the saved job description (instructions, skills, model).
- **Session:** one run of the agent.
- **Skill:** a how-to guide the agent follows for one part of the job.
- **Memory:** reference files the agent reads, like your profile.
- **Vault:** a locked box of passwords the agent uses without seeing them.
- **Dry run:** showing what would change without changing anything.

---
*Built with the ship-an-agent process. Version {{VERSION}}, {{DATE}}.*
