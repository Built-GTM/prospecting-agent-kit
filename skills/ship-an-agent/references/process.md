# Ship a Solution, agent edition: the step-by-step

The one process for taking an idea to a live, evaluated, published managed agent, plus the content it produces. It merges the repo standard `your own staging folder` (spec, the 8 agent steps, the four-number eval gate, bundle, article, posts, partner pack) with the Managed Agents deployment layer (design, package, provision, platform eval, operate).

If this file and SHIP-A-SOLUTION disagree on the eval gate or the publishing stages, SHIP-A-SOLUTION wins. This file owns the Managed Agents steps.

**How to run it:** use the `ship-an-agent` skill (`skills/ship-an-agent/`). It guides one step at a time and tracks progress in `<slug>/BUILD-STATE.md`. This file stays the source of truth for what each step is. When this file changes, re-copy it to the skill's `references/process.md` (the bundled copy for people without this folder).

The principle: **the platform is the last mile.** Most of the work, and all of the risk, is settled in files before anything touches platform.claude.com.

**Three rules from the first full builds (show-topic-scout and agent-coach, Sep 2026):**
- **Every agent can be set up by someone else.** Builds start from an idea or from an existing agent on the same path; organization facts stay in a profile and memory seed; every agent ships a `SETUP.md` and bundles every skill needed to build it (`.claude/skills/`, including ship-an-agent) and to run it (`skills/`).
- **One live checklist from step 1.** A published page the builder and Claude both tick, with click-by-click steps for everything the builder does by hand (`.claude/skills/ship-an-agent/references/live-checklist.md`).
- **Assume the builder doesn't code, and doesn't have Vercel.** Claude runs every command. The builder signs in, clicks, pastes into prepared lines, approves, and tests. The surface helper is picked from what they already use: code, n8n, Make, Zapier, or none (`references/beginner-guide.md`, `references/surfaces.md`).

## The short version (the one we teach)
| Phase | Steps | The question it answers | Hard gate |
|---|---|---|---|
| **A. Define** | 1 to 6 | Is this a real problem, and is an agent the right answer? | A receipt exists. The output fits a checkable schema. |
| **B. Design** | 7 to 9 | What goes in the prompt, skills, memory, and tools, and can it reach everything? | The owner approves the spec. No missing connection. |
| **C. Prove** | 10 to 12 | Does it work on real inputs before any infrastructure exists? | Eval gate: four numbers, on a set sized to risk (20 / 40 / 60 cases) |
| **D. Deploy** | 13 to 19 | Does the live agent match the proven one, and can people reach it? | Smoke test. Platform eval matches. A real task done. |
| **E. Publish** | 20 to 23 | Can others use it, and what did we learn worth telling? | Verdict visible everywhere. The owner's yes before anything goes public. |
| **F. Operate** | 24 to 26 | Is it getting better without breaking? | Every change passes the gate |

Every step ends with a **Capture** note: what goes into the build log. That record is the article.

---

## Phase A: Define

### 1. Capture the idea
- **Do:** Write one paragraph: who has the problem, the one output, what triggers it. Open a build log entry. Publish the live checklist with the starter phases (define, brain, prove, accounts, platform, surface, operate).
- **Artifact:** `agents/_project/build-log.md` entry (status: started), checklist URL in `BUILD-STATE.md`
- **Gate:** none. Ideas are cheap.
- **Capture:** the moment the idea came up, word for word. Any article or LinkedIn angle goes to the content inbox, `your own content inbox`.

### 2. Write the Solution Spec (SHIP Stage 0)
- **Do:** Fill the fixed shape: Problem (the scar and its cost), Who has it, the Workflow (GIANT: Ground, Identify, Assign, Normalize, Tie back), Skills needed, Receipt, Eval bar.
- **Artifact:** section 1 of `agents/<slug>/spec.md`
- **Gate:** the problem is specific and a receipt exists. If it's generic or has no receipt, stop.
- **Capture:** the scar in one sentence. This becomes the article's opening.

### 3. Pick the tier: skill, API call, or managed agent
- **Do:** Run the four checks from `agent-architect.md`: multi-step, worth the cost, Claude is good at it, errors are catchable. Then sort: a **skill** the owner runs himself, a **single API call** in the site, or a **managed agent** (multi-step, tools, memory, long-running or scheduled).
- **Artifact:** tier decision plus the reason, in the spec
- **Gate:** anything that isn't a managed agent leaves this process and goes through standard SHIP-A-SOLUTION.
- **Capture:** why this tier. The "not everything should be an agent" story lives here.

### 4. Name the job and the one output (SHIP agent step 1)
- **Do:** Run `name-the-job`. One agent, one job.
- **Artifact:** job line plus output line in the spec
- **Gate:** if the output takes two lines to say, it's two agents. Split them.
- **Capture:** the split you made, if any.

### 5. Write the contract before the prompt (SHIP agent step 2)
- **Do:** Run `agent-contract`. Input, output schema, must-always, must-never.
- **Artifact:** contract section of the spec. It later becomes the outcome rubric and the eval schema.
- **Gate:** **hard stop.** If the output can't be expressed as a checkable schema, it isn't ready to be an agent. Go back to step 2.
- **Capture:** the must-nevers. They make the trust story.

### 6. Draw the Split (SHIP agent step 3)
- **Do:** Run `cut-the-drag`. Which steps the agent owns, which the human keeps, and exactly where the checkpoint sits.
- **Artifact:** Split table in the spec. Every human checkpoint becomes an `always_ask` permission on that tool.
- **Gate:** every write, send, or spend has a named checkpoint.
- **Capture:** where the human stays in the loop and why.

## Phase B: Design

### 7. Sort the brain: prompt, skills, memory, tools
- **Do:** Apply the sorting rule in `agent-architect.md`. Judgment and hard rules go in the system prompt. Procedures go in skills. Facts that accumulate go in memory. One-run inputs are file resources. Anything touching the outside world is a tool or MCP server.
- **Artifact:** spec sections 4 to 7
- **Gate:** the prompt fits in about 2 pages. No user facts in skills. No procedures in memory. No organization facts (company, team, product, show names, their lists) in the prompt or skills: they go in a profile and memory seed, so anyone can set the agent up for their own team.
- **Capture:** what went where and one decision that was hard.

### 8. Map every verb to a connection (the viability gate)
- **Do:** Walk the jobs list clause by clause against `references/process.md` step 8. Each verb needs a tool, a credential (by name and your secrets file source), a reachable host, and its data.
- **Artifact:** spec section 6, with blockers flagged
- **Gate:** zero unflagged gaps. Blockers get resolved or cut from v1.
- **Capture:** which connections were easy and which fought back.

### 9. Write the design files and get the spec approved
- **Do:** Draft `spec.md`, `system-prompt.md`, `skills/<name>/SKILL.md`, `memory-seed/` (with the profile), `evals/cases.md` (the first 10 real cases), and `SETUP.md` from the skill's `assets/SETUP.template.md`. Present to the owner with assumptions marked and one batched question list.
- **Artifact:** the full `agents/<slug>/` folder
- **Gate:** **The owner approves the spec.**
- **Capture:** the questions the owner answered and what changed.

## Phase C: Prove (still no platform)

### 10. Run it by hand as skills (SHIP agent step 4)
- **Do:** In Claude Code, load the skills and memory seed as local files and run the 10 real cases. Fix the prompt and skills here, where an iteration takes seconds.
- **Artifact:** one folder per run in `evals/runs/<date>-<case>/`, the fix queue in `evals/findings.md`, and revised skills
- **Gate:** the output is good on real inputs and the contract holds on every run.
- **Capture:** what broke on the first run. That's the most honest paragraph in the article.

### 11. Red-team it (SHIP agent step 4, continued)
- **Do:** Run `agent-red-team`. Try to make it break a must-never, invent a number, or act without its checkpoint.
- **Artifact:** red-team findings plus fixes
- **Gate:** no must-never breach survives.
- **Capture:** the best attack and the fix.

### 12. Build the eval set and pass the gate (SHIP agent step 5, SHIP Stage 2)
- **Do:** Run `eval-set-builder` and size the set to the risk (table below), keeping the SHIP band mix: 40% happy path, 25% messy, 20% edge, 10% adversarial, 5% abstain. Score the skill version. The set grows over time: every real production failure gets added as a new case.
- **Artifact:** eval config plus the first verdict in `evals/`
- **Gate:** **the four numbers:** zero must-never violations, 90%+ overall, no band under 75%, consistency 0.85+. A fail goes back to step 10.
- **Capture:** all four numbers, the weakest band, and the set size.

**Eval size by risk (decided 2026-09-14: 100 cases is too aggressive as a default):**
| Risk tier | When | Cases (happy / messy / edge / adversarial / abstain) | Consistency runs | Overall bar |
|---|---|---|---|---|
| **1. Prove** | The builder is the only user and the agent is read-only or draft-only | **20** (8 / 5 / 4 / 2 / 1) | 3 | 90% |
| **2. Share** | Other people use it, still read-only or draft-only | **40** (16 / 10 / 8 / 4 / 2) | 5 | 90% |
| **3. Act** | It writes to a system, sends, spends, or is partner-facing | **60** (24 / 15 / 12 / 6 / 3), plus one adversarial case per must-never | 5 | 95% |

The tier can only move up after the gate is re-run at the new size. The 10 manual cases from step 10 count toward the happy and messy bands. The repo's `SHIP-A-SOLUTION.md` still says 100 until it's updated by PR.

## Phase D: Deploy (the Managed Agents layer)

### 13. Package in the deploy repo
- **Do:** Copy the proven design into the repo layout (appendix A) on a branch. The system prompt goes into `agent.yaml`, skills sit under the agent, the eval set and seed files come along.
- **Artifact:** PR in the deploy repo
- **Gate:** PR reviewed. No secret in any file (grep before pushing).
- **Capture:** time from approved spec to PR.

### 14. Provision on the platform
- **Before:** the checklist's "accounts" items are done: Console workspace with a spend limit, an API key in the prepared secrets line, tools installed and the key checked by Claude.
- **Do:** In order, because later steps use earlier ids:
  1. Upload skills (Skills API), record skill ids
  2. Create memory stores (shared read-only, per user) and seed them
  3. Create the vault and add credentials from your secrets file without printing them. Capture MCP OAuth once.
  4. Create or reuse the environment
  5. `ant beta:agents create < agent.yaml` (first time only; after that always `update`). Every later change starts with a dry run; edits made in the Console show up there and need the builder's call before an overwrite.
- **Artifact:** `ids.json` (agent id + version, environment, stores, vault, skill ids)
- **Gate:** every resource created. The repo YAML matches what's on the platform.
- **Capture:** anything the docs didn't tell you.

### 15. Smoke test
- **Do:** One session with everything attached: "Confirm you can reach each connection and read memory. Do not start the task." Watch it in the Console session viewer.
- **Gate:** every connection answers and memory mounts.
- **Capture:** what failed on the first smoke test.

### 16. Re-run the eval on the platform and capture metrics
- **Do:** Run the same eval set as platform sessions, using an outcome rubric from the step 5 contract where it fits. Pull cost per task, tokens, and cache hit rate from session usage. For a migrated site route, run the old route on the same cases for the before number.
- **Artifact:** platform scorecard in `_project/metrics/<slug>.md`
- **Gate:** the four numbers pass again and hold up against the local verdict. For migrations: quality at least equal to the old route, with the cost difference explained.
- **Capture:** before and after numbers. This is the headline.

### 17. Wire the surface (SHIP agent step 6)
- **Do:** Ask where people will use it and which tools the builder already has, then pick the helper (`references/surfaces.md`): none (Console or Claude Code), a no-code workflow (n8n, Make, Zapier), or a code helper (Vercel, Cloudflare; the owner's default). Check the ten Slack helper rules before testing. Add the surface's items to the checklist. Run a private test (W7) and read the session traces before inviting real users.
- **Gate:** the builder completes a real task through it, and a real user does too.
- **Capture:** the first real task and how it went.

### 18. Chain it, if it composes (SHIP agent step 7)
- **Do:** Run `agent-seam` where this agent hands to or from another. Agents compose only where both sides have a contract.
- **Gate:** the handoff has a schema on both sides.
- **Capture:** the seam and what it unlocks.

### 19. Name the owner and set the review (SHIP agent step 8)
- **Do:** One owner, one context doc, one recurring review where the owner checks output and fixes drift.
- **Artifact:** owner plus cadence in `agents/<slug>/spec.md` and the repo README
- **Gate:** no orphan agents.

## Phase E: Publish (SHIP Stages 3 to 6)

### 20. Bundle and publish the tool (SHIP Stage 3)
- **Before publishing:** verify it's shareable (`references/sharing.md`): pick host, template, or bundle; confirm no organization facts in the prompt or skills; read `SETUP.md` as a stranger; the template applies into an empty workspace and passes one eval case there.
- **Do:** Write the playbook entry (problem, outcome, steps, WHY, PROOF, EPISODE_CHAT), the install plugin, and the ENABLEMENT entry. Put the cards on /tools, /school, /playbooks, and /builds if there is a real receipt, each showing its eval verdict. For a managed agent the "install" is its surface link. A skill-bundle version ships for people who live in Claude.
- **Gate:** pages render, install resolves, and the verdict is visible on every surface. **The owner's yes before anything goes public.**
- **Capture:** links.

### 21. Write the article (SHIP Stage 4)
- **Do:** Build it from the build log with `builtgtm-article-writer`. Verdict first, receipts from steps 12 and 16, the honest failure from step 10, no em dashes.
- **Artifact:** Ghost draft (not published)
- **Gate:** voice check passes. The owner approves publishing.

### 22. Five posts (SHIP Stage 5)
- **Do:** Five distinct angles (Lens, Build Log, Scar, Field, Signal) saved as Ideas in Ordinal. Not scheduled.
- **Gate:** The owner schedules.

### 23. Partner pack, if a partner, show, or sponsor is involved (SHIP Stage 6)
- **Do:** Run `builtgtm-partner-pack`. Partners link to the page and never get the file.
- **Gate:** the tagged short link resolves and attribution lands on the Ghost member.

## Phase F: Operate and improve

### 24. Close the build: log it and publish the new skills
- **Do:** Fill every build log field: time spent per phase, the four numbers, before and after metrics, lines of prompt code removed, what broke, content shipped. Then publish the new skills (`.claude/skills/ship-an-agent/references/publish-skills.md`): harvest every skill the build created or proved, the owner decides publish, private, or later for each, make the public twins through `builtgtm-skill-publisher` and its confidentiality gate, bundle them into a plugin, publish behind the free subscribe unlock with the eval verdict, and link the build's article and posts to the page.
- **Gate:** the entry is complete before the session ends. Every published skill installs (200), shows its verdict, and a test unlock tags the subscriber; nothing public without the owner's yes.

### 25. Change through the gate
- **Do:** Every change follows one path: edit in repo, PR, eval run, the owner approves, `ant beta:agents update`, which creates a new version. Rollback means pinning the previous version. A real production failure is added as case 101 and up, never as a new set.
- **Gate:** no version ships without an eval run.
- **Capture:** each version's change and score in the build log.

### 26. Let it improve, safely
- **Do:** Sessions write lessons to memory. A scheduled evolution agent reads transcripts, memory, and scores, then proposes skill or prompt changes as a PR, which goes through step 25.
- **Gate:** no agent edits its own config or a read-only store (voice, positioning, ICP).
- **Capture:** each accepted improvement and its score change. This is the "agents that get better" story.

---

## Appendix A: deploy repo layout (`<your deploy repo>`, private, cloned at `<your deploy repo>`)
```
shared/
  environments/cloud-default.environment.yaml
  memory-seed/voice/ positioning/ icp/        shared read-only stores
  skills/<name>/SKILL.md                      skills reused across agents
agents/<slug>/
  agent.yaml          name, model, system, tools, mcp_servers, skills (ids)
  system-prompt.md
  skills/<name>/SKILL.md
  memory-seed/
  evals/              cases, brief_eval config, scorecards
  ids.json            platform ids and versions (not secrets)
  README.md           credentials needed (names only), surface, owner, review cadence
scripts/
  upload-skills  seed-memory  make-vault  run-evals
```
The design folder in `<design folder>/<slug>/` copies in at step 13. After that the repo is the source of truth for anything deployable, and the spec stays the design record.

## Appendix B: Console vs CLI
The Console is for exploring, watching sessions, and capturing OAuth. The `ant` CLI plus repo YAML is for every lasting change. A change made in the Console that isn't written back to YAML is drift.

## Appendix C: who does what
| Phase | Claude Code | the owner |
|---|---|---|
| All | publishes and ticks the live checklist, writes click-by-click steps for every hand step | ticks their own steps, answers questions on the page |
| A, B | drafts spec, contract, split, design files | names the scar, answers batched questions, approves the spec |
| C | runs manual cases, red team, eval set | reviews the verdict |
| D | packages, provisions, smoke tests, measures, writes and deploys or exports the surface helper, checks every value the builder pastes | creates accounts and keys, pastes values into prepared lines, completes OAuth and Slack sign-in, runs the private test, uses it for a real task |
| E | drafts bundle, article, posts, partner pack | approves anything that goes public |
| F | writes the log, runs the change flow and evolution proposals | approves each version |
