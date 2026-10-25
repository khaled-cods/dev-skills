<div align="center">

# dev-skills

**Eight practical skills that make an AI coding assistant work like a careful senior engineer.**
Code review, debugging, tests, commits, refactoring, API design, security, and clear explanations for beginners.

[Website](https://khaled-cods.github.io/dev-skills/) · [Install](#install) · [The skills](#the-skills) · [Contribute](CONTRIBUTING.md)

![license](https://img.shields.io/badge/license-MIT-2F4BFF) ![skills](https://img.shields.io/badge/skills-8-0E1B2C) ![format](https://img.shields.io/badge/format-SKILL.md-FFD23F)

</div>

---

## What is a skill?

A skill is a folder with one `SKILL.md` file: a short description of **when to use it** and a set of **instructions** the assistant follows. The assistant reads only the description until your request matches, so skills cost almost nothing when idle and make answers consistently better when they apply.

These skills are plain Markdown. Read them, edit them, copy the parts you like.

## The skills

| Skill | Use it when you say | What you get |
|---|---|---|
| [`code-review`](skills/code-review/SKILL.md) | "review this PR / my code" | Findings ranked by severity, each with a concrete failing case and the smallest fix. No style nitpicks. |
| [`debug-systematically`](skills/debug-systematically/SKILL.md) | "it crashes", "wrong output", "flaky test" | Reproduce, narrow down, test hypotheses one at a time, fix the cause, add a regression test. |
| [`write-tests`](skills/write-tests/SKILL.md) | "write tests for this" | Tests for behavior, boundaries, invalid input and failures. Readable and independent. |
| [`git-commits-and-prs`](skills/git-commits-and-prs/SKILL.md) | "commit this", "write the PR" | Small logical commits, clear messages, PR descriptions that reviewers can use. Safety rules for force-push and secrets. |
| [`refactor-safely`](skills/refactor-safely/SKILL.md) | "clean this up", "split this function" | Behavior locked by tests first, then small verified steps. |
| [`api-design`](skills/api-design/SKILL.md) | "design the endpoints", "is this API OK" | Consistent URLs, status codes, errors, pagination, idempotency, versioning, ownership checks. |
| [`security-review`](skills/security-review/SKILL.md) | "is this safe", "audit this" | Secrets, access control, injection, auth, uploads, database rules. Ranked, with fixes. |
| [`explain-code-simply`](skills/explain-code-simply/SKILL.md) | "what does this do", "I don't understand" | Beginner-friendly explanations with one small example. Works in Arabic as well as English. |

## Install

### Claude Code

```bash
git clone https://github.com/khaled-cods/dev-skills.git
cd dev-skills
bash scripts/install.sh              # all skills, into ~/.claude/skills
bash scripts/install.sh code-review  # or only the ones you want
```

For one project only, copy a folder into that project's `.claude/skills/` instead.

### Claude app (claude.ai)

Zip a skill folder (for example `skills/code-review`) so that `SKILL.md` is inside the folder, then upload it in **Settings → Capabilities → Skills**.

### Other assistants

The skills are ordinary Markdown. Paste the body of any `SKILL.md` into your assistant's custom instructions or rules file.

## Try it

After installing, ask normally. The right skill loads from your request:

```
Review the changes in this branch.
Why does this test fail only on CI?
Write tests for utils/price.py, including bad input.
Explain this error to me like I am new to Python.
```

## Quality bar

- Every skill has a single clear job and a description that says when it applies.
- Instructions are specific and checkable, not generic advice.
- `python3 scripts/validate.py` checks the format, and CI runs it on every push.

## Contributing

New skills and fixes are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md): keep a skill focused, test it on real tasks, and run the validator.

## License

[MIT](LICENSE). Use it, change it, share it.
