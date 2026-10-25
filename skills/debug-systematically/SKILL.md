---
name: debug-systematically
description: Find the root cause of a bug instead of guessing. Use when the user reports an error, crash, wrong output, flaky test, or "it doesn't work", especially when a first quick fix did not help. Reproduce, narrow down, form hypotheses, test one at a time, then fix and prevent.
---

# Debug systematically

Guessing fixes wastes time and hides the real bug. Follow the loop below.

## The loop

1. **Get the exact symptom.** Full error message and stack trace, the input that caused it, what was expected versus what happened, and what changed recently. If any of this is missing, ask for it or find it before touching code.
2. **Reproduce it.** Make the smallest command or test that fails every time. If you cannot reproduce it, the first job is to find out what differs (data, environment, timing, version).
3. **Read the error literally.** The top of the stack trace in the user's own code usually points at the line. Check the message for the actual value that was wrong.
4. **Narrow the search.** Bisect: cut the problem in half with logging, a debugger, or `git bisect` for regressions. Find the last place the data was still correct and the first place it was wrong.
5. **Write down 2 or 3 hypotheses** and what evidence would confirm or kill each one. Test the cheapest first. Change one thing at a time.
6. **Fix the cause, not the symptom.** Wrapping the crash in `try/except` or adding a `null` check that hides the problem is not a fix unless you can explain why the value is null.
7. **Prove the fix.** Run the reproduction again. Add a test that fails before the fix and passes after.
8. **Look for siblings.** Search for the same mistake elsewhere in the codebase.

## Common causes to check early

- Wrong assumption about the data shape or type (string vs number, `undefined` vs empty).
- Stale cache, stale build, wrong environment, wrong config file loaded, wrong branch.
- Async order: missing `await`, callback runs later than expected, race between two requests.
- Off-by-one and boundary values (empty list, one item, the maximum).
- Time zones, encodings, and locale (Arabic text, RTL, UTF-8).
- Version mismatch between a library and its docs.

## How to report

Explain in plain words: what was happening, why, what you changed, how you verified it. If you could not find the cause, say what you ruled out and what to try next. Never say "fixed" without having run the reproduction.
