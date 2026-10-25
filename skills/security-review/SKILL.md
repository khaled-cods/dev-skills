---
name: security-review
description: Check code and configuration for common security problems. Use when the user asks for a security review, audit, or "is this safe", or when code handles logins, user input, files, payments, secrets, databases, or public endpoints. Finds issues like injection, broken access control, exposed secrets, and unsafe defaults.
---

# Security review

Focus on problems that real attackers use. Rank by impact and ease of exploitation.

## Checklist

1. **Secrets**: API keys, passwords, tokens, or private keys in code, commits, logs, frontend bundles, or `.env` files that are committed. A secret in a public repository must be treated as leaked: rotate it.
2. **Access control** (most common serious flaw): is every sensitive action checked on the server? Can user A read or change user B's data by changing an ID? Are admin routes protected server-side, not only hidden in the UI?
3. **Injection**: SQL built by string concatenation, shell commands from user input, unsanitized HTML (XSS), template injection, path traversal (`../`). Use parameterized queries, escaping by the framework, and allowlists.
4. **Authentication**: passwords hashed with a slow algorithm (bcrypt, scrypt, argon2), never stored in plain text. Rate limits on login and code-sending endpoints. Sessions and tokens expire. Reset flows do not leak whether an account exists.
5. **Input and uploads**: validate type, size, and content on the server. Store uploads outside the web root, rename them, and check real file type.
6. **Database rules** (Supabase, Firebase, and similar): Row Level Security enabled on every table with policies tested as an anonymous user and as another user. Service keys never shipped to the browser.
7. **Transport and headers**: HTTPS everywhere, secure and `HttpOnly` cookies, a content security policy where feasible, a restrictive CORS list (never `*` with credentials).
8. **Dependencies**: known vulnerable versions, abandoned packages, install scripts from unknown sources. Run the ecosystem's audit tool.
9. **Errors and logging**: no stack traces or secrets shown to users or written to logs. Log security events (failed logins, permission denials).
10. **Money and state**: prices and totals calculated on the server, never trusted from the client. Check for double submit and race conditions.

## Output

For each finding give: **severity** (critical, high, medium, low), **where**, **how it can be exploited** in one or two sentences, and **the fix**. Order by severity. Say clearly what you did not check.

## Rules

- Only analyze code and systems the user owns or is authorized to test.
- Do not write working exploits or attack tools. Describe the weakness and the defense.
- If a real secret is found, never repeat it in full in your answer. Show the first few characters only.
