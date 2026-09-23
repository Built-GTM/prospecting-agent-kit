<!-- Portable copy for ship-an-agent bundles. Source: the owner's _playbook/agent-spec.template.md. -->
# <Agent name>: spec

Status: draft | ready-to-deploy | live (agent id + version once live)
Owner: <builder name>
Last updated: YYYY-MM-DD

## 1. The job, in one breath
Who uses it, what it does for them, what "done" looks like.

## 2. Users and trigger
| | |
|---|---|
| Primary user | who types to it |
| Trigger | person (chat), event (webhook, new email, calendar), or schedule (cron) |
| Surface v1 | where they talk to it first (see access-and-connections.md, section 4) |
| Surface v2 | where it goes when it is proven |
| Single-user or multi-user | if multi-user: one vault + one memory store per user |

## 3. Jobs to be done
Numbered list of the verbs. Each verb must map to a tool, skill, or MCP server in section 6 (the viability gate).

| # | Job | Mapped to |
|---|---|---|
| 1 | | |

## 4. System prompt
Lives in `system-prompt.md`. Summarize here: role, operating principles, output contract, what it must never do. Keep the prompt about judgment. Procedures go in skills.

## 5. Skills
| Skill | Type (anthropic / custom / repo) | What it teaches | Source material |
|---|---|---|---|

Max 20 per agent. Each custom skill is a folder with `SKILL.md` in `skills/<skill-name>/`.

## 6. Tools and connections
| Capability | Kind | Permission | Credential (vault type + secrets file line name) |
|---|---|---|---|
| bash, read, write, edit, glob, grep | agent toolset | always_allow | none |
| web_search, web_fetch | agent toolset | always_allow | none (domain allow/block list if needed) |
| | MCP server | always_ask for writes | mcp_oauth / static_bearer |
| | env var API (curl from bash) | | environment_variable, allowed_hosts |
| | custom tool (my app answers) | n/a | held host-side |

## 7. Memory
| Store | Access | Scope | Layout | Seeded from |
|---|---|---|---|---|
| | read_only | shared across users | | |
| | read_write | per user | | |

What the agent should write back, when, and what it must never store (secrets, anything the user asks to forget).

## 8. Environment
cloud or self_hosted, networking (unrestricted or limited + allowed hosts), packages needed.

## 9. Kickoff shape
Conversational (`user.message`), outcome with rubric (`user.define_outcome`), or scheduled deployment (cron + initial events). Session budget cap in dollars.

## 10. Evals
5 to 10 real test prompts with what a pass looks like. Outcome rubric if used.

## 11. Guardrails
What needs a human yes. What it refuses. Data it must not expose.

## 12. Build checklist
- [ ] Spec approved by the builder
- [ ] Skills written and reviewed
- [ ] Memory seeded
- [ ] Credentials in vault (names only listed here)
- [ ] agent.yaml + environment.yaml committed to the deploy repo
- [ ] Smoke test session passes (can reach every connection)
- [ ] Evals pass
- [ ] Surface wired
