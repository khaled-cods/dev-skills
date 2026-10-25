---
name: api-design
description: Design or review HTTP/REST APIs and their data contracts. Use when the user is creating endpoints, choosing URLs, status codes, request and response shapes, pagination, error formats, auth, or versioning, or asks whether an API is well designed.
---

# API design

An API is a contract that is hard to change later. Make it boring, consistent, and predictable.

## Resources and URLs

- Use nouns for resources and HTTP methods for actions: `GET /orders`, `POST /orders`, `GET /orders/42`, `PATCH /orders/42`, `DELETE /orders/42`.
- Plural, lowercase, hyphenated names. Nest only one level (`/orders/42/items`).
- For actions that are not CRUD, use a sub-resource or verb endpoint deliberately (`POST /orders/42/cancel`).

## Methods and status codes

- `GET` safe and cacheable, never changes data. `PUT` replaces, `PATCH` updates part, `POST` creates or triggers. `DELETE` is idempotent.
- `200` OK, `201` created (with `Location`), `204` no content.
- `400` malformed request, `401` not authenticated, `403` not allowed, `404` not found, `409` conflict, `422` valid shape but invalid data, `429` rate limited.
- `5xx` only for server faults. Never return `200` with an error inside.

## Request and response shape

- Consistent naming (pick `snake_case` or `camelCase` and keep it). ISO 8601 UTC timestamps. Money as integer minor units or a string, never a float. IDs as strings.
- Return the created or updated resource.
- **Errors**: one format everywhere, for example `{ "error": { "code": "out_of_stock", "message": "...", "field": "size" } }`. A stable machine-readable `code`, and a human `message`.

## Lists

- Always paginate. Prefer cursor pagination for large or changing data (`?limit=50&cursor=...`). Return the next cursor.
- Allow filtering and sorting with explicit, validated parameters.

## Safety and evolution

- Authenticate every non-public endpoint, and check **ownership** on every object (user A must not read user B's order by changing the ID).
- Validate and limit all input sizes. Rate-limit expensive or sensitive endpoints.
- Make writes **idempotent** where retries happen (an `Idempotency-Key` header for payments and orders).
- Version from the start (`/v1/`) and never remove or rename a field without a deprecation period. Adding optional fields is safe.
- Document with an OpenAPI file and examples.

## When reviewing

List problems as: what is inconsistent or unsafe, the concrete risk, and the smallest change to fix it.
