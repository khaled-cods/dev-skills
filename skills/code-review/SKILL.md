---
name: code-review
description: Review code changes like a senior engineer. Use when the user asks to review a diff, pull request, file, or function, or says "check my code". Finds real bugs and risks first, ranks findings by severity, and skips style nitpicks a linter would catch.
---

# Code review

Review for what can actually go wrong, in this order. Stop padding the review with opinions.

## How to review

1. **Understand the intent first.** Read the PR description, commit message, or ask what the change should do. A review without intent only finds style issues.
2. **Read the whole change before commenting.** A problem on line 10 is often solved on line 80.
3. **Trace the unhappy paths.** For every new branch, ask: what if the input is empty, null, huge, duplicated, or in the wrong order? What if the network call fails or runs twice?
4. **Check what the change touches, not only what it changes.** Search for other callers of any function whose behavior changed.

## What to look for (highest value first)

1. **Correctness**: wrong condition, off-by-one, wrong variable, missing `await`, mutated shared state, wrong default.
2. **Data loss and security**: unvalidated input, injection, missing auth check, secrets in code, destructive operation without a guard.
3. **Failure handling**: swallowed errors, no timeout, no retry limit, partial writes with no rollback.
4. **Concurrency**: race conditions, double submit, non-idempotent handlers.
5. **Tests**: does a test fail without this change? Are error paths covered?
6. **Maintainability**: only when it will hurt the next person (hidden coupling, misleading names, copy-paste that will drift).

Skip formatting, import order, and anything a linter or formatter enforces.

## Output format

Start with a one-line verdict: **Ready**, **Ready with small fixes**, or **Needs changes**.

Then list findings, most severe first. Each finding has:

- **Severity**: `blocker` (will break or is unsafe), `should-fix`, or `suggestion`.
- **Where**: file and line.
- **Problem**: what goes wrong, with a concrete input that triggers it.
- **Fix**: the smallest change that solves it, with code when short.

End with what is good about the change when something deserves it. Be specific, never generic praise.

## Rules

- Never claim a bug without a concrete scenario. If unsure, say "I could not confirm this" and name what to check.
- Do not rewrite the author's approach to match your taste. Suggest a change only when yours is clearly safer or simpler.
- If the change is too large to review well, say so and suggest how to split it.
