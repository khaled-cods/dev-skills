---
name: refactor-safely
description: Improve the structure of existing code without changing its behavior. Use when the user asks to refactor, clean up, simplify, split a large function or file, remove duplication, or make code easier to maintain.
---

# Refactor safely

Refactoring changes structure, never behavior. If behavior changes, it is not a refactor.

## Steps

1. **Define the goal.** What hurts today: duplication, a function too long to read, confusing names, tight coupling? Refactor toward that, nothing more.
2. **Lock the behavior first.** Run the existing tests. If there are none, write a few tests that record what the code does now (characterization tests), including its odd outputs. Without a safety net, go in smaller steps and say so.
3. **Take small steps, test after each.** One move at a time: rename, extract function, inline, move, split. Run tests after every step. If a step breaks something, undo it and take a smaller one.
4. **Keep refactors separate from features and fixes.** Different commits, ideally different PRs. If you find a bug on the way, note it and fix it separately.
5. **Stop at the goal.** Do not rewrite the whole module because you can.

## Useful moves

- **Extract function**: give a block of code a name that says what it does.
- **Rename**: make names say what the thing is, not how it is made.
- **Replace magic values** with named constants.
- **Remove duplication** only when the copies really change together. Two similar pieces that evolve separately should stay separate.
- **Flatten nesting** with early returns.
- **Split by responsibility**: a function that fetches, validates, and formats becomes three.
- **Delete dead code** after confirming nothing uses it (search the whole repo, including config and tests).

## Do not

- Change public function signatures, file formats, or API responses without listing every caller and updating it.
- Reformat whole files that hide the real change in the diff.
- Add abstractions for imagined future needs.

## Report

Say what the structure was, what it is now, and how you know behavior is the same (which tests passed).
