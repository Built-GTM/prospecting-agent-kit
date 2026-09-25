# Where people use the agent (step 17), for any builder

A managed agent has no screen of its own. Something has to start a session, pass messages in, and bring answers back. That something is the **helper** (or relay). Most builders don't have Vercel or a developer. Pick the helper from what they already use.

## Ask first (a `questions` item on the checklist)
1. **Where will people use it?** Slack, Microsoft Teams, a web form, email, on a schedule with nobody typing, or just you.
2. **Which of these do you already have?** Vercel, Cloudflare, n8n (cloud or self-hosted), Make, Zapier, none.
3. **Who changes the helper later?** Someone who codes, or someone who'd rather drag boxes.

## Pick the helper
| People use it in | Already have | Recommend | Builder effort | Notes |
|---|---|---|---|---|
| Just the builder | anything | **Claude Code or the Console**, no helper | none | Claude starts sessions and downloads outputs. Good for v1 of every agent. |
| A schedule (a morning digest, a weekly report) | n8n, Make, or Zapier | **The no-code tool:** a timer starts a session, waits, sends the result by email or Slack | 30 to 60 min | The easiest real surface. Nobody types, so no thread tracking is needed. |
| Slack | n8n or Make | **The no-code tool:** two workflows (below) | 1 to 2 hours | The builder imports what Claude writes and pastes credentials into the tool's own screens. |
| Slack | Vercel or Cloudflare, or nothing and open to a free account | **A small code helper** Claude writes, tests, and deploys | 1 hour of clicks | Most robust: signature checks, tests, version history. the owner's default (`surfaces/<slug>-slack` in the deploy repo). |
| Slack | Zapier only | Zapier for one-shot requests; move to n8n or code for back-and-forth threads | 1 hour | Zapier can do it, but keeping a thread tied to a session gets fiddly. |
| A web form | n8n, Make, or Zapier | **The tool's form trigger:** the form starts a session, the result is emailed back | 30 to 60 min | No login to build. Good for people outside the team. |
| A web chat on their own site | Vercel | A code helper (Anthropic's managed-agents quickstarts) | 2+ hours | Keep the API key on the server, never in the browser. |
| Microsoft Teams | any | Same pattern as Slack, with a Teams bot | 2+ hours | Teams bot registration takes more clicks than Slack. |
| People's own Claude (claude.ai, Cowork) | their own Claude plan | **Ship the skills as a skill bundle** instead of a managed agent | small | Runs in their Claude with their connectors. Nobody hosts anything. |

Record the choice and why in the decisions log, then add that surface's items to the checklist.

## What every Slack helper must do (whatever it's built with)
Learned the hard way on show-topic-scout. Check each one before the private test.
1. **Verify requests.** Slack signs every request with the signing secret, and the Claude platform signs webhooks with the `whsec_` secret. Reject anything unsigned. (In no-code tools: the Slack trigger handles Slack's check. Add an HMAC check step for the platform webhook.)
2. **Answer Slack's URL check** (`url_verification`) and reply within 3 seconds. Do the slow work after replying, or Slack retries and you get duplicates. Ignore retries (`X-Slack-Retry-Num` header).
3. **Hear mentions, DMs, and thread replies.** Subscribe to `app_mention`, `message.im`, `message.channels`, `message.groups`. Scopes: `app_mentions:read`, `chat:write`, `files:write`, `im:history`, `im:read`, `channels:history`, `groups:history`. Ignore messages from bots, including itself.
4. **Map one thread to one session,** and a new input link in the thread to a fresh session. Store `thread -> session id` (a data table in n8n, a data store in Make, a key-value store or session titles in code).
5. **Create sessions with everything attached:** agent id, environment id, memory store (read-only), vault ids, and a budget (for example $5).
6. **On the webhook** (`session.status_idled`): fetch the session's events, post only the agent's last message of that turn, and upload any output files created in that turn to the thread.
7. **Post Markdown properly:** a Slack `markdown` block, or convert `**bold**` to `*bold*` and `[text](url)` to `<url|text>`.
8. **Safety net for must-nevers that are about text** (no dashes, no email addresses): clean the message before posting.
9. **Tell the thread when something stops:** budget reached, repeated errors, or an approval the helper can't give.
10. **Stay quiet in threads the bot isn't part of.**

## Slack with n8n (two workflows)
Claude writes both workflows as importable JSON files, and the builder imports them (in n8n: **Workflows** > **...** > **Import from File**). Node names change between n8n versions, so Claude checks the current n8n docs before writing them and says which version it targeted.

**Credentials the builder creates in n8n** (Settings > **Credentials** > **Add credential**):
- **Header Auth** named `Claude API`: name `x-api-key`, value is the surface API key.
- **Slack API** with the bot token.
- The Slack signing secret and the `whsec_` secret go wherever the workflow's check step reads them (a credential or an n8n variable), never typed into a node's text.

**Workflow 1: Slack in**
1. **Slack Trigger** (events: app mention, message in channels, message in private channels, direct message). Copy its production URL into the Slack app's Event Subscriptions.
2. **Filter:** drop bot messages, retries, and channel messages that aren't thread replies.
3. **Data table lookup:** find the session for `channel + thread_ts`.
4. **If there's no session** (or the message has a different input link): **HTTP Request** `POST https://api.anthropic.com/v1/sessions` with headers `anthropic-version: 2023-06-01` and `anthropic-beta: managed-agents-2026-04-01` (check the current beta name) and the body Claude provides. Save the returned id to the data table. Post "On it" in the thread.
5. **Otherwise:** **HTTP Request** `POST /v1/sessions/<id>/events` with a `user.message`. Post "Got it."

**Workflow 2: Agent out**
1. **Webhook** node (POST). Its production URL is what the builder registers in W6.
2. **Crypto** node (HMAC SHA256, base64) over `webhook-id.webhook-timestamp.body` with the decoded `whsec_` secret, then an **If** that stops when it doesn't match `webhook-signature`.
3. **HTTP Request:** get the session, then its events (`agent.message`, `session.status_idle`).
4. **Code** node: take the last agent message of the latest turn, convert Markdown for Slack, clean must-never text.
5. **Slack** node: post in the thread. Then list the session's files, download new ones, and upload them to the thread.

Test each workflow with n8n's **Execute workflow** before turning it on (**Active**).

## Slack with Make
Same two scenarios: **Slack > Watch events** (instant) and **Webhooks > Custom webhook** as the triggers, **HTTP > Make a request** for the Claude API (the key goes in a keychain or connection, not the URL), a **Data store** for thread to session, and **Tools > Set variable** plus `sha256(...)` with a key for the signature check. Claude writes the blueprint and verifies module names against current Make docs. The builder imports it: **Scenarios** > **...** > **Import blueprint**.

## Scheduled agent with any no-code tool
1. **Schedule trigger** (for example weekdays at 7am).
2. **HTTP Request:** create a session with the day's input in the first message.
3. **Wait** for the webhook (or poll the session every minute until `idle`, 30 minutes max).
4. **HTTP Request:** fetch the last agent message and files.
5. **Send** by email or Slack.

## A code helper (Vercel, Cloudflare)
Claude writes it in the deploy repo with unit tests, deploys it, and sets its environment variables from the secrets file. The builder only makes a free hosting account (Vercel: sign up with GitHub at `vercel.com`, then tell Claude) and does W5 to W8. Reference implementation: the owner's `managed-agents/surfaces/show-topic-scout-slack` (Slack events, webhook, thread mapping, new link in a thread, Markdown block, dash safety net, 35 tests).

## The weekly coach and feedback loop, with or without Vercel
Every agent can get the agent coach (weekly improvement proposals, `agent-coach` in the owner's deploy repo). It needs four pieces. Pick one option per row from what the builder already has.

| Piece | Code host (Vercel, Cloudflare, Supabase) | GitHub only | No-code (n8n or Make) |
|---|---|---|---|
| Store feedback (thumbs up or down, reason) | A small route plus a Postgres table (the owner: your own site `/api/agents/feedback`) | Not a good fit: GitHub can't receive Slack events | A data table (n8n) or data store (Make), or an Airtable or Google Sheet |
| Weekly gathering job (Monday) | A cron route (Vercel cron, Cloudflare Cron Triggers, Supabase scheduled function) | A scheduled GitHub Actions workflow running the gathering script from the agent repo, with the Claude key in repository secrets | A schedule trigger plus HTTP and Code steps; the trimming is the fiddly part |
| The report and approvals | A private page with Approve, Reject, Give feedback (the owner: Lab `/private/agents/coach`) | One GitHub issue per agent per week, a checkbox per proposal; a tick approves, a comment is feedback | A Notion or Airtable database, one row per proposal, with a Decision column (Approve, Reject, Feedback) the workflow reads |
| Apply approved changes | The job writes approved memory facts; Claude Code opens PRs for the rest | A second workflow on issue edits writes memory facts; Claude Code handles PRs | The workflow writes memory facts through the Claude API; Claude Code handles PRs |

Rules that hold on every option: the coach session has no network and no key that can change an agent; only a person's Approve on a proposal id moves anything; the approve rate is the ongoing ride along (evals), so revisit the coach when it stays under 50 percent for 3 weeks. Builders without a code host usually do best with **GitHub only** for the weekly loop plus **n8n or Make** for Slack feedback.
