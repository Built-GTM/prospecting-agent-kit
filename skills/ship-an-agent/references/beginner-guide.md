# Guiding a builder who doesn't code

Assume the builder has never opened a terminal, used GitHub, or held an API key. Most people building their first agent haven't. the owner is technical, but he asked for this default too, because the plain version is faster to follow for everyone.

## The split of work
**Claude does:** every terminal command, every file, every install, every deploy, every test run, every check that something worked.

**The builder does only what a person has to do:**
1. Sign in to accounts and click through web settings pages.
2. Copy a value from a web page into a line Claude already prepared.
3. Say an approval sentence ("go on #8", "approve the design").
4. Use the agent for a real task and say what happened.
5. Make the product decisions (who it's for, what it must never do, which tools to connect).

If a step needs anything else from them, rethink it: Claude probably can do it (for example, the Slack CLI can create and install an app after a one-time sign-in).

## How to explain a step
- **One thing at a time.** One action per numbered line. Name the site, the button, and the exact text.
- **Say what they'll see.** "A window opens asking you to approve permissions." Surprises make beginners stop.
- **End with the words to send back:** "Tell Claude: **key is in**."
- **Give time honestly** ("about 15 minutes, mostly Google's screens").
- **Explain a concept before naming it,** in one sentence, then use the name. "A vault is a locked box on the Claude platform that holds a password so the agent can use it without seeing it."
- **Check their work yourself,** then confirm in one line ("The key works. It can reach your agent.").
- **When something fails,** say what broke in plain words, what you already fixed, and the one thing they need to do, if anything.
- **Offer the shortcut when it exists** ("reply with @Show Topic Scout for now, the fix is coming").

## Secrets: the placeholder pattern
Never ask for a key, token, or password in chat. The value would sit in the conversation's history. Instead:
1. **Claude creates a private secrets file** with an empty, commented line for each value the build will need, before the builder needs it:
   ```yaml
   # Slack: api.slack.com/apps > your app > OAuth & Permissions > Bot User OAuth Token. Starts with xoxb-
   SLACK_BOT_TOKEN: 
   ```
   - the owner: `your credential store: <name>-config.md`, and add a row to `agent-access.md`.
   - Everyone else: `~/agent-secrets/<slug>.md`. It stays out of any repo and out of iCloud, Dropbox, and OneDrive folders. Tell them why in one sentence.
2. **The builder pastes** right after the colon, one space, no quotes, one line, and saves.
   - To open the file on a Mac: in Finder press **Cmd Shift G**, paste the folder path, press Enter, and open the file in TextEdit.
   - On Windows: paste the folder path into File Explorer's address bar.
3. **Claude reads it with a script that never prints the value,** checks the format (a prefix like `sk-ant-` or `xoxb-`) and makes one real call to prove it works. Then Claude moves the value to where it's used: a platform vault, the hosting tool's environment variables, or the no-code tool's credential screen.
4. **Values that show once** (webhook signing secrets, some API keys) get a bold warning: "It shows only once. Copy it right away."

The exception is n8n, Make, and Zapier: they store credentials in their own screens. Give click-by-click steps to paste the value there, and still keep a copy in the secrets file so Claude can test with it.

## Walkthrough library
Adapt these to the builder's accounts. Put the numbered clicks straight into the checklist items.

### W1. Claude Console account, workspace, spend limit (10 minutes)
1. Go to `platform.claude.com` and sign up or sign in.
2. Add a payment method when asked (Settings > Billing). Agent runs cost real money: a typical run is cents to a few dollars.
3. Settings > Workspaces > **Create workspace**. Name it `agents`. A workspace is a folder for agents with its own spend limit.
4. Settings > **Limits**, pick the `agents` workspace, set a monthly limit (start with $50 to $150), save.
- You'll know it worked when: the Limits page shows your number for that workspace.

### W2. An API key (5 minutes)
1. In `platform.claude.com`, click **API keys**, then **Create key**.
2. Pick the `agents` workspace. Name it for what uses it (`<slug>-local` for Claude's own use, `<slug>-slack` for a Slack helper). A key per use means you can turn one off without breaking the others, and costs show up separately.
3. Copy the key (starts with `sk-ant-`). It shows once.
4. Paste it into the line Claude prepared (see "Secrets"). Tell Claude: **key is in**.

### W3. Look at a session in the Console (5 minutes)
1. `platform.claude.com` > **Sessions** (under Managed Agents).
2. Click the newest one. Each row is something the agent did: read a file, searched, wrote the answer.
3. Scroll to the end to see the final answer and the cost.
- Why it matters: when something looks wrong in the output, this is where you and Claude find out why.

### W4. GitHub, only if they want version history (10 minutes)
1. Go to `github.com` and sign up (free).
2. Click **+** at the top right, then **New repository**. Name it `agents`. Choose **Private**. Click **Create repository**.
3. Tell Claude the repository name. Claude sets up the connection; if the GitHub CLI asks you to sign in, it opens a browser page with a code to confirm.

### W5. A Slack app (5 to 15 minutes)
**With the Slack CLI (Claude does most of it):**
1. Claude runs `slack login` and gives you a line starting with `/slackauthticket`.
2. In Slack, in the workspace where the bot should live, send that line as a message in any channel or DM.
3. Click **Approve** in the window that opens. Slack shows a short challenge code. Send it to Claude (it only finishes this sign-in, so it's safe to paste).
4. Check the workspace name Claude reports back is the one you meant.
5. Claude creates and installs the app. Then copy two values from the pages Claude links (the Bot User OAuth Token and the Signing Secret) into the prepared lines.

**Without the CLI:** `api.slack.com/apps` > **Create New App** > **From a manifest** > pick the workspace > paste the manifest Claude gives you > **Create** > **Install to Workspace** > **Allow**. Then copy the same two values.

To add an icon: the app's Basic Information page > Display Information > App icon (512 to 2000 pixels, square).

### W6. The platform webhook (5 minutes)
A webhook is how the Claude platform tells your helper "the agent finished a turn."
1. `platform.claude.com` > **Manage** > **Webhooks** > **Add**.
2. Paste the address Claude gives you.
3. Tick the events Claude names (usually `session.status_idled` and `session.status_terminated`). Save.
4. Copy the signing secret right away (starts with `whsec_`; it shows once) into the prepared line. Tell Claude: **webhook is in**.

### W7. The private test (15 to 20 minutes)
1. In Slack, create a private channel (`#<slug>-test`). Type `/invite @<bot name>`.
2. Post a real input the way a user would, mentioning the bot.
3. Answer in the thread the way a user would: without the mention, in normal words.
4. Try a second input in the same thread, and one full-length run (a file, if the agent makes one).
5. Tell Claude what happened at each step, even when nothing happened. Claude checks the logs and the session.

### W8. Hand it to real users (15 minutes)
1. Invite the bot to their channel, or tell them to DM it.
2. Post and pin a four-line how-to Claude writes: how to start, how to answer, how long it takes, what it never does.
3. For the first week, glance at the threads once a day and tell Claude "log feedback" when something is off.

## Plain-words glossary
| Word | Say it like this |
|---|---|
| Agent | The whole worker, saved: its job description (prompt), its playbook (skills), and which model it runs on. It's versioned, so you can go back. |
| Session | One run of the agent, like one shift at work. |
| Environment | The locked-down computer a session runs on, and which websites it may reach. |
| Memory store | Where the onboarding binder (context pack) sits: the reference folders the agent reads. |
| Skill | One page of the playbook: a how-to guide the agent follows for one part of the job. |
| Vault | Where the keys (tools and connections) are held: a locked box of passwords the agent can use without seeing them. |
| API key | The password that lets Claude's tools use your Claude account. |
| Webhook | A doorbell: one system rings another when something happens. |
| Relay or helper | The small piece in the middle that passes messages between Slack (or a form) and the agent. |
| Deploy | Give it a desk: put the latest version where people use it. |
| Dry run | Show what would change, without changing anything. |

## Things Claude checks for the builder (lessons from show-topic-scout)
Say these out loud when they come up, in one line each.
1. **Dry run before every change to the live agent.** Someone may have edited it in the Console. Report the difference and let the builder choose to keep or overwrite it. An overwrite is never silent.
2. **One API key per use** (Claude's local work, each surface), plus a workspace spend limit and a per-session budget.
3. **A helper that needs every secret at startup can't pass Slack's URL check** until the last secret exists. Say so up front, so an early error doesn't alarm anyone.
4. **People reply in threads without mentioning the bot.** A Slack helper must hear thread replies, not only mentions.
5. **A new link in the same thread is a new job.** Start a fresh session so nothing about the last person carries over.
6. **Agents write Markdown and Slack shows it raw** unless the helper sends a Markdown block or converts it.
7. **Rules in the job description can slip,** like "no dashes." Add a safety net in the helper for anything that must never reach users.
8. **Unconnected tools make runs slower and more expensive** (connectors added in the Console with no login fail at every start). Remove what isn't connected.
9. **The first real test finds what unit tests can't.** Always run W7 before inviting real users, and read the session traces after it.
10. **A choice the builder didn't ask for** (an advisor model, a paid tool) needs a sentence on cost and a test before it ships.
