# Sharing an agent: host it, template it, or bundle it

A managed agent lives inside one Anthropic workspace. There is no way to hand someone the agent object itself. Sharing the managed agent means shipping the files that make it, in one of three shapes. All three come from the same deploy repo, because the skills are the same in each.

| | **Host it** | **Template it** | **Bundle it** |
|---|---|---|---|
| What they get | A link to your running agent (a Slack app, a web page) | A repo they deploy into their own workspace | A skill bundle installed in their own Claude |
| Who pays | You | Them | Their Claude plan |
| Their data and logins | In your workspace (your responsibility) | In theirs | In their Claude |
| Updates | Everyone at once | They pull updates | The plugin updates |
| Best for | People who only want the result | Builders who want to own it | The widest reach, least setup |

"Give this to others to build with" means **template it**, usually alongside **bundle it**. the owner's longer write-up: `<design folder>/_playbook/sharing-and-distribution.md`.

**These three shapes are not the whole answer any more.** Step 20 of the process doc requires the four deliverables, every build, no exceptions: Claude Code directions (`deploy/claude.md`), Codex directions (`deploy/codex.md`), build your own Grok Bot (`deploy/grok-bot.md`), and a published Bot on the marketplace that anyone can install. Publishing is now the default, not an optional extra, and the published Bot is the front door most people walk through. Hosting, templating and bundling are how the three written routes get delivered to whoever graduates from that front door. The onboarding binder is never one of the four: the Bot writes each installer their own on its first run, so nobody inherits someone else's facts.

## Built shareable from step 7, verified at step 20
Every build keeps organization facts out of the job description (prompt) and the playbook (skills) from step 7, and drafts `SETUP.md` at step 9 (`assets/SETUP.template.md`). So at step 20 this checklist is a verification, not a rewrite. Walk it, one checklist item per line:

1. **Scan for organization facts.** Grep the job description and every `SKILL.md` for the company, show, product, team, and people names, plus any lists that belong to them (series, pricing, ICP, catalogs). Each hit is a fact, not a method.
2. **Move facts into the binder (context pack).** Put them in a profile file (for example `memory-seed/profile.md`) and reference files with the same structure but example content. The job description and the playbook say "read the profile" instead of naming things.
3. **Replace what must stay in the job description with placeholders** (`{{ORG_NAME}}`, `{{AUDIENCE}}`), filled by the setup step.
4. **Keep secrets out.** Credentials are names only, with the placeholder pattern from `beginner-guide.md`.
5. **Ship a ride along (evals) they can rerun.** `evals/cases.md` with the case shapes and one worked example; they add their own real inputs.
6. **`SETUP.md` reads right to a stranger:** what it does, cost per run, time to set up, every {{...}} filled, and step 1 says to open the folder in Claude Code and ask to set it up with the ship-an-agent skill.
7. **Bundle every playbook file.** The builder's side goes in `.claude/skills/` (see "What every template bundles"); the agent's own skills stay in `skills/`. Anthropic prebuilt skills the agent uses (for example `docx`) are referenced by id, not copied. Open the template folder in a fresh Claude Code session and confirm `ship-an-agent` loads and its routing finds each builder skill in the folder.
8. **Include the setup checklist** (a filled `checklist.html` without their ids) and surface options (`surfaces.md`: code helper, n8n or Make, or none).
9. **Gate:** a fresh read of the job description and the playbook finds no organization facts, the template applies cleanly into an empty workspace, and one ride along case passes there.

Template repo layout:
```
<agent>-template/
  .claude/skills/        the builder's skills: ship-an-agent and the step skills below
  README.md              one screen: what it is, then "follow SETUP.md"
  SETUP.md               the step-by-step setup guide for a non-coder
  agent.md               the job description, with placeholders or "read the profile"
  environment.yaml
  memory_store.yaml
  skills/<name>/SKILL.md
  memory-seed/           the binder: profile.md and reference templates, plus import scripts where they help
  evals/cases.md
  setup/checklist.html   and surface files (Slack manifest, n8n workflows)
```

## What every template bundles
| Where | Skill | Used at |
|---|---|---|
| `.claude/skills/ship-an-agent/` | the guide itself, with `references/` (process, live checklist, beginner guide, surfaces, sharing, agent-architect) and `assets/` (checklist, SETUP, spec, and build state templates) | every step |
| `.claude/skills/name-the-job/` | one agent, one job, one output | step 4 |
| `.claude/skills/agent-contract/` | input, output schema, must-always, must-never | step 5 |
| `.claude/skills/cut-the-drag/` | what the agent owns and where the human steps in | step 6 |
| `.claude/skills/agent-red-team/` | trying to break it on purpose | step 11 |
| `.claude/skills/agent-surface/` | where people use it | steps 17, 19 |
| `.claude/skills/agent-seam/` | handing off to or from another agent (only if it chains) | step 18 |
| `skills/<name>/` | the agent's own skills, with their scripts | runs on the platform |
| by id in `agent.md` | Anthropic prebuilt skills (for example `docx`) | runs on the platform |

Step 12 (the ride along set) has no separate skill: the process doc sizes it by risk, and the agent's `evals/cases.md` holds the cases. Add the weekly coach bundle (`agent-coach` plus `shared/feedback-kit/`) when the template includes the feedback loop.

Sources: `ship-an-agent` from this kit; any step skills you have from `your own staging folder` (public versions).

**Worked example (your brand):** Show Topic Scout becomes "Podcast Guest Scout". Its four skills are already generic methods; the the show show profile, topic map, and episode catalog become binder templates with an import script for any podcast feed; the job description stops naming the show and reads `show-profile.md`. The agent coach and the feedback kit are generic already: they read each agent's deliverable, change log, and feedback.

## Starting from an existing agent (the same path as an idea)
Anyone setting up an agent that already exists follows the normal 26 steps; the difference is that steps 3 to 9 start from the agent's files. A copied agent still has to be proven for this team.

| Step | Starting from an existing agent |
|---|---|
| 1 Capture | Name the agent and version; restate what it does for this team; follow its SETUP.md if it has one. |
| 2 Solution Spec | Still required: the builder's own scar and receipt. An existing agent is not proof the problem exists here. |
| 3 to 6 | Read the agent's tier, job, deliverable, and split. Change only what this team needs; record each change. The must-nevers can be added to, never removed. |
| 7 to 9 | Fill the binder, the profile and memory seed, with this team's facts (import scripts where the agent has them). Approval covers the filled profile and any changes. |
| 10 to 12 | Rerun the agent's ride along cases with this team's real inputs. The gate size follows this team's risk, not the original builder's. |
| 13 to 19 | As normal, with the accounts, surface, and checklist walkthroughs. |
| 20 to 26 | As normal. Contributing fixes back to the original is optional and needs the builder's yes. |
