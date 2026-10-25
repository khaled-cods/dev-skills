---
name: write-tests
description: Write useful automated tests that catch real bugs. Use when the user asks for tests, unit tests, test coverage, or wants to test a function, API, or component. Chooses what to test, covers edge cases and failures, and keeps tests readable and independent.
---

# Write tests

A good test fails when the behavior breaks and passes when only the implementation changes. Aim for confidence, not a coverage number.

## Before writing

1. Find the project's existing test framework and style (pytest, unittest, Jest, Vitest, Go `testing`, JUnit). Match it. Do not add a new framework without asking.
2. Read the code under test and list its **behaviors**: what it promises for given inputs.
3. Decide the level: pure functions get unit tests, code with a database or network gets integration tests with the dependency faked or run for real, user flows get a few end-to-end tests.

## What to cover

For each behavior, write tests for:

- **The normal case** with realistic data.
- **Boundaries**: empty, one item, maximum size, zero, negative, exact limit.
- **Invalid input**: wrong type, missing field, malformed text. The test asserts the specific error.
- **Failure of dependencies**: the network times out, the database rejects, the file is missing.
- **State and order**: calling twice, calling out of order, concurrent calls where relevant.
- **Regression**: the exact input from any bug being fixed.

## How to write them

- One behavior per test. Name it as a sentence: `test_rejects_expired_token`, `it("returns 404 for unknown order")`.
- Structure: arrange the data, act once, assert the outcome.
- Assert on observable results (return values, stored data, responses), not on private helpers or call counts, unless the call is the behavior.
- Keep tests independent: no shared mutable state, no required order, clean up anything created.
- Fake only what you must (network, clock, randomness). Never mock the thing under test.
- No logic (loops, conditionals) in tests. Use table-driven or parametrized cases instead.
- Make failures readable: the assertion message should show expected versus actual.

## Finishing

Run the tests. Confirm at least one fails if you break the code on purpose (change a condition and see a test fail). If a test cannot fail, delete it or fix it. Report what is covered and what is not.
