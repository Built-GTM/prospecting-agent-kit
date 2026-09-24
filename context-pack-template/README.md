# Context pack template

The knowledge half of the agent. The agent is the method: how to research, the honesty rules, the shape of the output. The pack is what your team knows: who you sell to, what you solve, when to reach out, and what proves it.

**One agent, many packs.** The method never mentions your company, so the day you change what you sell, or who you sell to, you edit six files and nothing else.

## Start here
`company.md` has a section called **Our own domains, for the customer check**. Fill it first. It is the difference between an agent that spots an existing customer and one that writes a confident pitch to someone who already pays you. On the build this kit came from, that one section caught three customers hiding in a list of eight hand-picked prospects.

## The six files
| File | What it answers | Which Why it feeds |
|---|---|---|
| `company.md` | Who we are, what we sell, and which domains mean someone already runs us | Sets "us" for every Why |
| `icp.md` | Which companies are worth a rep's time, and who disqualifies | Why them |
| `personas/<role>.md` | What each buyer is measured on and afraid of. One file per buyer | Why you |
| `problems/<name>.md` | What breaks, what it costs, and why they live with it. One file per problem | The Because, and the angle |
| `signals.md` | What counts as "now", how to search for it, and what it implies | Why now |
| `proof.md` | Who you may name, and what result you may claim | Why us |

## How to fill it
1. Copy this folder and rename it for your company.
2. Fill every `[ ]` field. Delete the guidance lines when you are done.
3. Copy `_template.md` once per persona and once per problem, and rename it (`vp-sales.md`, `missed-calls.md`). Delete the template copy afterwards.
4. Write in your customers' words, not your marketing copy.
5. **No evidence, no entry.** An empty field beats a guess, because the agent repeats whatever you write here as fact.
6. One owner approves changes before they go live. Reps never edit the running pack.

## Enough to run
- `company.md` complete, including the customer-check domains
- `icp.md` with the disqualifiers filled
- 2 personas and 2 problems
- 3 signals, each mapped to a problem in the mapping table
- 1 proof point per problem

That is a working pack. Everything past it makes the briefs better, not possible.

## Before you rename a section
Every file here uses the same headings as `example-pack/`, which is a finished pack that passed the eval gate. Several of those headings are named directly in `system-prompt.md` and in `skills/four-whys-research/SKILL.md`. Renaming one does not break loudly, it just quietly switches off the rule that reads it. If you need a different shape, change the agent's rules in the same commit.

## A quality bar worth keeping
Two or more personas. Problems written in the customer's words, with the cost quantified. Three or more signals, each with a real way to detect it and each mapped to a problem. Two or more customers you may name per problem.
