# deploy/

**The binder is yours. The deploy is the platform's.**

Everything else in this kit is platform neutral on purpose. `context-pack-template/`, `system-prompt.md`, `skills/` and `evals/` are plain markdown and one Python script, and they do not change depending on where you run the agent.

This folder is the part that does change.

| File | Platform |
|---|---|
| `claude.md` | Claude Managed Agents |
| `grok-bot.md` | xAI Grok Bot |
| `codex.md` | OpenAI, which has three different answers |

## Why there is no "Grok binder"

There is exactly one binder, and forking it per platform is a bug rather than a feature.

Here is the test. You change your ICP. How many files do you edit? With one binder, one. With a Claude binder and a Grok binder, two, and the day you forget is the day one of your agents starts pitching a segment you stopped selling to.

The binder is what the agent knows about your business. That is identical everywhere by definition.

The one genuine platform difference at the binder level is a single extra anti job on Grok, because its filesystem is writable. One sentence does not justify a second copy of your ICP.

## The four steps that never change

1. Fill the binder.
2. Load the job description and the anti jobs.
3. Load the playbook, and type in the budget by hand.
4. Run the ride along before anyone else sees it.

Only the deploy differs, and only after those four.
