# Closing a build: publish the new skills

Every agent build produces skills that work beyond the agent: a way to read a post, a report checker, a feedback loop, a better way to write a contract. Publishing the proven ones turns each build into free tools people unlock with an email, which grows the subscriber list and sends traffic to the skills page. It runs once, at the close of every build (step 24), after the agent has passed its gates.

**The rule that shapes it:** people link to the page, they never get the file. Installs sit behind the free subscribe unlock, which is both the audience capture and the update channel. A copied SKILL.md skips both and goes stale the moment the skill changes.

## 1. Harvest (Claude)
List every skill this build created or changed, in one table:

| Skill | Where it lives | What it does, in one line | Method or org facts? | Proof it works | Plugin it fits |
|---|---|---|---|---|---|

Include:
- the agent's own skills (`skills/<name>/`) and their scripts
- anything built for the builder's side (a checker, a template, an import script)
- changes to existing public skills that the build proved (for example a better step in `agent-contract`)

"Proof" is a receipt from this build: the eval gate, a platform run, a real user task. No proof means it isn't a candidate yet.

## 2. Decide (the builder)
Put a question on the checklist for each skill, with a recommendation:
- **Publish:** the method is general and this build proved it.
- **Keep private:** it only makes sense with this organization's facts, or it exposes something that shouldn't be public.
- **Later:** promising, but needs more real use first. Record what would make it ready.

Nothing moves to publish without the builder's explicit yes (`say`: "publish the skills").

## 3. Make the public twin (Claude)
For each skill marked Publish, run the skill publisher (the owner: `builtgtm-skill-publisher` in `<your notes folder>/<your org>/skills/published/`):
1. Binding inventory: every connector, field, framework name, ID, tuned threshold, internal name, and taxonomy, tagged KEEP, ABSTRACT, or STRIP. Show the report first.
2. Transform into the public shape: what it does, what you'll need, **Customize this for yourself**, the method, where the numbers come from, make it yours.
3. **Confidentiality gate (hard stop):** no real customer, account, or person names, no real dollar figures, no schema-leaking field names, IDs, tokens, internal paths, or thresholds described as tuned on private data. When unsure, strip it.
4. Write to a staging folder of your own. The private original is never edited.

Guest names, account names, and anyone who hasn't agreed to be named stay out, even when the article names the organization.

## 4. Bundle into a plugin (Claude)
Group by the problem the reader has, not by the build that made them. Add or update the entry in `public-skills/plugins.json` (slug, name, tagline, problem, audience, connectors, skills). Examples from the owner's builds:
- **Agent Builder Kit:** `ship-an-agent` plus the step skills (`name-the-job`, `agent-contract`, `cut-the-drag`, `agent-red-team`, `agent-surface`, `agent-seam`).
- **Agent Coach:** the four coach skills plus the feedback kit.
- **Podcast Guest Scout:** `post-reader`, `guest-research`, `show-fit`, `brief-builder`.

## 5. Publish (Claude, only after the builder's yes)
1. Push the public twins to the distribution repo (the owner: `heath-gtm/Skill-Builder`, with `HEATH_GTM_PAT`).
2. Put the cards on the site, each showing its eval verdict (SHIP-A-SOLUTION Stage 3): the tools page in its collection with install and download behind the free subscribe unlock, and a builds card when there's a real receipt.
3. Link everything to the page, never the file: the agent's `SETUP.md` ("the skills in this folder are also free at <page>"), the build article, and each post from it.
4. If the build is tied to a show, sponsor, or partner, run the partner pack (tagged short link, copy at three lengths, paste-ready card) so their audience's unlocks are attributed.

## 6. Gate (Claude checks, the builder confirms)
- The install URL returns 200 for every published skill.
- Each card renders with its eval verdict visible.
- A test unlock (the builder's own email) adds the subscriber with the right source label.
- The confidentiality gate passed on every twin.
- Zero em dashes or en dashes on every page and file.

## 7. Capture
In the build log: which skills were published, private, or later (and why), the page links, and after 7 days the unlocks per skill. That number decides which skills get an article or a post next.

## For builders outside your brand
Same steps, their own channels: publish the twins to their own public GitHub repo or skill marketplace, link a page (a README, a Notion page, a site) instead of the raw file, and use their own subscribe or signup form if they have one. Steps 1 to 3 (harvest, decide, confidentiality gate) never change.
