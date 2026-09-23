# Prospecting agent kit

Everything you need to build the research agent from the show, for your own company.

The agent takes a company URL and one LinkedIn profile, and hands back why that person should care right now: a verdict, the Because, the 4 Whys with sources, and what it could not verify. It does the homework. The rep still does the prospecting. It never writes the email.

## Start here
1. `SETUP.md`. Written for someone who does not code.
2. `context-pack-template/`. The six files you fill in for your own company. This is the only part that is about you.
3. `skills/build-context-pack/SKILL.md`. Point this at your own website and it drafts those six files for you, then asks you five questions to close the gaps.

## What is in the box
| Folder | What it is |
|---|---|
| `system-prompt.md` | The agent's instructions. Method only, no company facts, so it works for any company |
| `skills/four-whys-research/` | How to research each Why: which sources to trust, how to check a person is still in the role, when to stop |
| `skills/build-context-pack/` | Setup time. Turns your website into a first draft of your pack |
| `context-pack-template/` | The six blank files: company, icp, personas, problems, signals, proof |
| `example-pack/` | A finished pack for ServiceTitan, built entirely from their public pages. Read this to see what good looks like |
| `evals/check_brief.py` | The contract checker. Run it on a brief and it scores it 34 ways |

## The one idea worth stealing
Method in the agent, knowledge in the pack. The prompt never mentions your company, so the day you change what you sell, or who you sell to, you edit six markdown files and nothing else. That is what lets one agent serve a whole team, and what stops you rebuilding it every quarter.

## What is not in here
The research lookup script points at a paid data route that needs its own credential, so it is left out. The agent works without it on web search and page reading alone.

The eval case set is not included either. It names real people at real companies who never agreed to be examples. Build your own from the shape in `check_brief.py`: some easy accounts, some messy ones, some edge cases, a couple of deliberate attacks, and one where the right answer is to refuse.
