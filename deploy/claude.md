# Deploy: Claude Managed Agents

This is the one the show was built on, so it is the best documented and the only one here that has actually run.

**Why it suits this agent:** the binder mounts **read only** and the platform enforces it. Anti job 8 on the Grok build is a rule you hope holds. Here it is a property of the system. For an agent whose value is that its knowledge does not drift, that is the difference that matters.

## The five objects

In this order, and the order is the whole mental model.

| # | Object | Holds |
|---|---|---|
| 1 | **Agent** | The job description: model, system prompt, tools, MCP servers, skills. Versioned, so you can change it without breaking running sessions |
| 2 | **Environment** | Where it runs: a cloud sandbox or your own, preinstalled packages, network rules. Each session gets a fresh container |
| 3 | **Memory store** | The binder, read only |
| 4 | **Vault** | The keys. `mcp_oauth`, `static_bearer` or `environment_variable` |
| 5 | **Session** | One run, one brief, with an event stream you can read back |

## The build

Install the CLI, then apply two files:

```
brew install anthropics/tap/ant
ant apply agent.md environment.yaml
```

`agent.md` is frontmatter plus your system prompt as the body. `environment.yaml` is the sandbox and its network rules. Both IDs land in `claude-lock.json`.

Then a session, referencing both, and you send it the company URL and the LinkedIn URL.

Quickstart with working code in seven languages: https://platform.claude.com/docs/en/managed-agents/quickstart

## The desk

A **scheduled deployment** is an agent, an environment, a cron expression with a timezone, and a first message. Optionally files, GitHub, memory stores and vaults.

```
ant apply deployment.md
```

Two things worth knowing that the other platforms do not have.

**A per run budget.** The deployment copies a cap onto every session it starts, so the cap bounds each run separately rather than being a cumulative ceiling. A session pauses with `budget_reached` when it hits its own cap. This is what makes "33 cents per prospect" an enforced number rather than an aspiration.

**Deployment runs.** Every trigger writes a run record, with a typed error when it fails: `environment_archived_error`, `session_rate_limited_error`. Filter for the failures with `--has-error`. Full history, not the last twenty.

Docs: https://platform.claude.com/docs/en/managed-agents/scheduled-deployments

## The ride along

Run your cases in a sandbox with networking off and nothing in the world moves. Score the output the same way as anywhere:

```
python3 evals/check_brief.py <the file you saved the brief in>
```

## What is genuinely Claude specific

Only the deploy. The binder, the job description, the playbook, the deliverable and the ride along are markdown and one Python script, and they move unchanged. That is the point of the split.
