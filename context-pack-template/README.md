# Context pack template

The knowledge half of the prospecting-research agent. The agent is the method (how to research, the honesty rules, the output). The pack is what your team knows: who you sell to, what you solve, when to reach out, and what proves it. One agent, many packs.

Built from the ICP Trigger Playbook (GTM Juice template). The brain dump, message builder, and campaign tracker tabs stay out: the agent doesn't write copy or track campaigns.

## Start here
`company.md` has a section called **Our own domains, for the customer check**. Fill it first. It is the difference between an agent that spots an existing customer and one that writes a confident pitch to someone who already pays you. On the build this kit came from, that one section caught three customers hiding in a list of eight hand-picked prospects.

## How to fill it
1. Copy this folder and rename it for your company.
2. Fill every `[ ]` field. Delete the guidance lines in italics when you're done.
3. One file per persona in `personas/`, one per problem in `problems/`. Copy `_template.md`, rename it (`vp-sales.md`, `prioritization-crisis.md`), delete the template.
4. Write in your customers' words, not your marketing copy. No evidence, no entry: an empty field beats a guess, because the agent will repeat whatever you write here as fact.
5. The owner approves changes before they load into the memory store. Reps never edit the live pack.

## What the agent uses each file for
| File | Playbook tab | Feeds |
|---|---|---|
| `company.md` | ICP Brain Dump (who we are, what we sell) | Sets "us" for every Why |
| `icp.md` | ICP Definition | Why them |
| `signals.md` | Signals, plus the trigger events on each Problem tab | Why now, the Because |
| `problems/<name>.md` | Problem 1 to 3, Current State Analysis | The Because, the angle |
| `personas/<role>.md` | Persona 1 to 3 | Why you |
| `proof.md` | Content Library, customer proof | Why us, the angle |

## Minimum to run (level 1)
- `company.md` complete, including the customer-check domains
- `icp.md` with disqualifiers filled
- 2 personas, 1 to 3 problems
- 3 signals, each mapped to a problem in the mapping table
- 1 proof point per problem

Every file here uses the same section headings as `example-pack/`, which is a finished pack that passed the eval gate. If you add or rename a section, check `system-prompt.md` and `skills/four-whys-research/SKILL.md` first: several sections are named directly in the agent's rules, and renaming one silently turns that rule off.

Playbook validation checks that still apply: 2+ personas, 3 problems in customer words, quantified impact, 3+ signals with a clear detection method, every signal mapped to a problem, 2+ customers per problem.
