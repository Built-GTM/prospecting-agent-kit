# ServiceTitan context pack

The six files the agent reads to know who "us" is. Everything company specific lives here, so the same agent serves a different company by swapping this folder.

## What is in here
| File | Holds |
|---|---|
| `company.md` | What ServiceTitan sells, its own domains for the customer check, its published value claims |
| `icp.md` | Who fits, the lookalike table from named customers, every disqualifier |
| `personas/` | owner-operator, general-manager-ops, office-csr-manager, platform-executive |
| `problems/` | missed-calls, tech-productivity, slow-cash, post-deal-integration |
| `signals.md` | Signals by tier with search recipes, freshness windows, known vendor domains, the signal to problem map, and the stacks |
| `proof.md` | Named customers in their own words, kept separate from company claims |

## How fields are labelled
Every field is marked **found** with the source link, or **inferred**. The agent treats them differently: a found fact can be stated, an inferred one is a hypothesis it says out loud. Nothing here is a guess pretending to be a fact.

This pack was built from ServiceTitan's public pages and free web search. The fields an owner would answer from the inside, such as real deal size, the competitors they actually meet, and which customers reps may name beyond the public page, are marked inferred and are the first five things a real owner should correct.

## Two things verified live, not inferred
- **The customer check.** `scheduler.servicetitan.com` and `static.servicetitan.com` load on a named customer's site, and a customer's own tenant sits at `<name>.myservicetitan.com`. A prospect site loading any of these is already a customer.
- **Two competitor signatures.** `clienthub.getjobber.com` (Jobber) and `book.housecallpro.com` (Housecall Pro), both confirmed against live URLs.

## The persona tie break
`personas/platform-executive.md` carries the rule that decides the hardest case in this vertical: when someone still holds an owner or founder title but the company was bought in a majority deal, the platform executive persona wins. The job changed even when the title did not.
