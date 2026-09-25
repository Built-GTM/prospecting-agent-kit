# Deploy: Claude Managed Agents

This is the one the show was built on, so it is the best documented and the only one here that has actually run.

**Why it suits this agent:** the onboarding binder (context pack) mounts **read only** and the platform enforces it. Anti job 8 on the Grok build is a rule you hope holds. Here it is a property of the system. For an agent whose value is that its knowledge does not drift, that is the difference that matters.

## Before you start

This route is driven from a terminal on your own computer and from code. That is its honest shape, and it is worth knowing before you pick it. You do not have to write the agent's thinking, because the kit already holds it. You do have to run a few commands and fill in two short files.

What you need:

- **The kit folder**, downloaded and unzipped. `README.md` at the top of this kit has the two ways to get it.
- **Your binder filled in.** `SETUP.md` step 2 walks through it. Nothing here works on an empty binder.
- **A Claude Console account**, with billing on it and a monthly spend limit set. `SETUP.md` step 4 is the click by click version, and it applies here unchanged.
- **A terminal.** On a Mac that is the Terminal app. Every command on this page is typed there.

**Working inside the kit folder.** Every command below assumes the terminal is pointed at the unzipped kit folder. To point it there: type `cd `, with the space after it, then drag the kit folder from your file browser onto the terminal window, then press return.

## The five objects

In this order, and the order is the whole mental model.

| # | Object | Holds |
|---|---|---|
| 1 | **Agent** | The job description (prompt): model, system prompt, tools, MCP servers, skills. Versioned, so you can change it without breaking running sessions |
| 2 | **Environment** | Where it runs: a cloud sandbox or your own, preinstalled packages, network rules. Each session gets a fresh container |
| 3 | **Memory store** | The binder, read only |
| 4 | **Vault** | The keys (tools and connections). `mcp_oauth`, `static_bearer` or `environment_variable` |
| 5 | **Session** | One run, one brief, with an event stream you can read back |

Four words in that table that the table does not define:

- A **sandbox**, or container, is a computer created for one run and thrown away after it. Nothing a run does to it survives into the next run.
- An **MCP server** is a standard way of plugging an outside tool into an agent, so the agent can use it without anyone writing custom code for it.
- **Versioned** means each saved change keeps its own number. A run that started on version 3 finishes on version 3 even after you save version 4.
- An **event stream** is the ordered record of everything the agent did in one run: every search, every page, every decision. It is what you read when a brief comes back wrong.

`mcp_oauth`, `static_bearer` and `environment_variable` are the three shapes a credential can take. This research agent needs web search and page reading and nothing else, so unless you add a connector of your own, the vault stays empty. That is the correct state for it.

## The build

Two files you write, then one command.

**`agent.md` is the job description.** It is a markdown file with a block of settings at the top, fenced by a line of three dashes above and a line of three dashes below, and the system prompt as the body underneath. That body is `system-prompt.md` from this kit, copied in whole. The settings name the model, the tools, the skills and the memory store. Copy the field names from the quickstart rather than guessing them.

**`environment.yaml` is where it runs.** The sandbox and its network rules. The quickstart has a working one to copy.

Neither file ships in this kit, because both carry identifiers belonging to your own account. Create them in the kit folder, beside `system-prompt.md`.

Then install the command line tool and apply both:

```
brew install anthropics/tap/ant
ant apply agent.md environment.yaml
```

`brew` is Homebrew, the installer most Mac developers use. If it is not on your machine, the quickstart is the place to check what else is supported.

`ant apply` sends those two files to your Claude account and creates the agent and the environment there. The files stay on your computer. The platform now holds a copy it can run.

Both IDs land in `claude-lock.json`, a small file the tool writes beside yours so later commands know which agent and which environment they are talking about. Leave it alone and keep it with the other two.

Your binder goes up as a memory store and is attached to the agent read only. The quickstart shows the call that creates a store and loads files into it.

Then a session, referencing both, and you send it the company URL and the LinkedIn URL. A session is one run of the agent. You start one from code: pick your language on the quickstart page, copy its session example, and put the two URLs in as the first message.

Quickstart with working code in seven languages: https://platform.claude.com/docs/en/managed-agents/quickstart

## The desk (deployment)

A **scheduled deployment** is an agent, an environment, a cron expression with a timezone, and a first message. Optionally files, GitHub, memory stores and vaults.

A cron expression is the standard way of writing a repeating time, the notation a server administrator uses for something like "every weekday at 8am". The timezone sits next to it so the schedule follows your working day rather than the server's.

It is a third file you write, `deployment.md`, applied the same way as the other two:

```
ant apply deployment.md
```

Two things worth knowing that the other platforms do not have.

**A per run budget.** The deployment copies a cap onto every session it starts, so the cap bounds each run separately rather than being a cumulative ceiling. A session pauses with `budget_reached` when it hits its own cap. This is what makes "33 cents per prospect" an enforced number rather than an aspiration.

**Deployment runs.** Every trigger writes a run record, with a typed error when it fails: `environment_archived_error`, `session_rate_limited_error`. Filter for the failures with `--has-error`, a flag you add to the command that lists runs. Full history, not the last twenty.

Docs: https://platform.claude.com/docs/en/managed-agents/scheduled-deployments

## The ride along (evals)

The ride along is the set of test cases you run before anyone else touches the agent. A case is one company URL, one LinkedIn profile URL, and what you already know the right answer looks like. Build your own set: a few easy accounts, a few messy ones, an existing customer of yours, and one where the right answer is to refuse. The kit ships no cases on purpose, and `README.md` says why.

Run them in a sandbox with networking off and nothing in the world moves. Networking off is one of the network rules in `environment.yaml`, so it is a setting rather than a promise you are making to yourself. No other platform in this folder offers that.

Score the output the same way as anywhere. Save the brief into a plain text file ending in `.md`, then, in the terminal, from inside the kit folder:

```
python3 evals/check_brief.py <the file you saved the brief in>
```

Replace the part in angle brackets, brackets and all, with the name of the file you saved. The checker is plain Python 3 with nothing to install.

## What is genuinely Claude specific

Only the deploy. The binder, the job description, the playbook (skills), the deliverable (contract) and the ride along are markdown and one Python script, and they move unchanged. That is the point of the split.
