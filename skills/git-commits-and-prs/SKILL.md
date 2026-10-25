---
name: git-commits-and-prs
description: Write clear git commit messages, split work into clean commits, and write pull request descriptions. Use when the user asks to commit, write a commit message, summarize changes, open a PR, or clean up git history.
---

# Git commits and pull requests

History is documentation. A reviewer should understand what changed and why without reading every line.

## Commits

- **One logical change per commit.** If the message needs "and", split it. Do not mix a refactor, a bug fix, and formatting.
- **Check before committing**: run `git status` and `git diff --staged`. Make sure no secrets, `.env` files, build output, or large binaries are staged.
- **Message format**:

```
type(scope): short summary in the imperative, under 72 characters

Why this change was needed, in a sentence or two. What was wrong or
missing before, and any decision a reader might question.
```

- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `ci`.
- Use the imperative ("add retry", not "added retry"). The body explains **why**, since the diff already shows **what**.
- Reference an issue when there is one (`Fixes #42`).

## Pull request description

```
## What
One or two sentences on the change.

## Why
The problem or goal. Link the issue.

## How
Key decisions and anything non-obvious. Mention what you did not do.

## Testing
What you ran and what you saw. Steps to try it by hand.

## Notes for reviewers
Where to look first, risks, follow-ups.
```

- Keep PRs small enough to review in one sitting. If a PR touches more than one concern, suggest splitting it.
- Add screenshots for UI changes.

## Safety rules

- Never force-push to a shared branch, rewrite published history, or run `git reset --hard` / `git clean -fd` without the user's explicit approval.
- Commit and push only when asked.
- If a commit contained a secret, tell the user to **rotate the secret** immediately. Removing it from history is not enough.
