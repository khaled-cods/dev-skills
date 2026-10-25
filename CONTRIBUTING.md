# Contributing

Thanks for helping. A good skill is short, specific, and tested on real work.

## Add a skill

1. Create `skills/<name>/SKILL.md`. The name is lowercase, with hyphens (`my-skill`).
2. Start with frontmatter:

   ```
   ---
   name: my-skill
   description: One or two sentences. Say what it does AND when to use it, with the phrases a user would actually say.
   ---
   ```

3. Write the body as instructions to the assistant: steps, checks, what to avoid, and the output format.
4. Run `python3 scripts/validate.py` until it passes.
5. Add one row to the table in `README.md`.

## What makes a good skill

- **One job.** If the description needs "and also", make two skills.
- **Concrete.** "Check that every new branch handles empty input" beats "write robust code".
- **Tested.** Try it on at least three real tasks and fix where it went wrong.
- **Lean.** Cut anything the assistant would already do without being told.
- **Honest.** Say what to do when the information is missing or the task is out of scope.

## Pull requests

Keep them small, explain the problem a change solves, and show an example of the skill working. Be kind in reviews.
