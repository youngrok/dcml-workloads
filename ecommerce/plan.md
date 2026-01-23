You are implementing an ecommerce policy engine as an experimental workload.

IMPORTANT INTERACTION RULE
- The next user message will contain ONLY the target programming language name (e.g., "Rust", "Python 3.12").
- Do NOT ask follow-up questions. Do NOT request additional specs. Proceed immediately.
- Treat the language name as the only variable; everything else is fixed by the repository files.

WORKSPACE INITIALIZATION (mandatory)
- If the per-language workspace directory does not exist, create it:
  - Target directory: `workloads/ecommerce/{{LANGUAGE}}/`
- Implement from scratch in the target directory; do not copy or reuse existing implementations from other runs or languages.

DEVELOPMENT ENVIRONMENT (mandatory)
- Prefer using tools already installed on the current OS and available on PATH.
  - Do not assume you can install new compilers/runtimes/package managers.
  - When writing build/run instructions, pick commands that work with typical PATH-installed toolchains.
- Special rule for TypeScript:
  - Use `bun` (not `node`, not `ts-node`, not `deno`) for running/building TypeScript solutions.

TARGET LANGUAGE
- Target language: {{LANGUAGE}}  (this will be provided by the user as the next message)

WHAT YOU HAVE ACCESS TO (in this repo)
- Core data schema: `workloads/ecommerce/schema.tsp`
- Policy: `workloads/ecommerce/shop-policy.md`
- Scenarios: `workloads/ecommerce/test-scenario.md`
- Tests: `workloads/ecommerce/tests/*.md`
- Test runner: `workloads/ecommerce/runtest.py`

TASK
Implement an ecommerce policy engine executable that:
1) Reads HTTP-like requests from STDIN (UTF-8).
2) Maintains in-memory DB state across requests within a session.
3) Outputs one JSON response line per request (in order).

I/O SPECIFICATION
- Input format (stdin): HTTP-like request, simplified
  ```
  METHOD /resource
  {json body}
  ```
  - Body is optional and must be valid JSON if present.
- Output format (stdout): one JSON object per request
  - **Every request MUST produce exactly one line of JSON output**, even if no `>>>` assertion exists in the test.
  - Output must be in the same order as requests.

API DESIGN PRINCIPLES
- Each model in `schema.tsp` maps to a REST-like resource:
  - `POST /{resource}` → create (e.g., `POST /user`, `POST /order`)
  - `GET /{resource}/{id}` → read by ID (e.g., `GET /order/O1`)
  - `GET /{resource}?{query}` → read by query (e.g., `GET /refund?orderId=O1`)
- Request body: include only the fields you need; omit optional fields.
- Response body: return the resource object. For `POST`/`PATCH`, return the created/updated object (including computed fields). For `GET`, return the requested object.
- Field definitions follow `schema.tsp`. Optional fields (marked `?`) may be omitted in requests.

FIELD RULES
- Coupon/Benefit discount fields:
  - `discountType=RATE` → use `rate` field (float, e.g., 0.10 for 10%)
  - `discountType=FIXED` → use `amount` field (integer KRW)

ENDPOINT-SPECIFIC BEHAVIOR
- `POST /refund`: create a Refund for an order item. Input: `{orderId, variantId, quantity}`. Returns the created Refund object with all computed fields.
- `GET /refund?orderId={id}`: returns the Refund object for the given order (not by refund ID).

Examples:
```
POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":100000}}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1}]}

GET /order/O1
```

TEST FILE FORMAT
- Each request is `METHOD /resource` followed by optional JSON body
- `>>>` indicates the expected response for that request (subset match)
- Blank line separates requests
- Program maintains state within a single test file execution
  ```
  POST /user
  {"id":"U1",...}

  POST /order
  {"id":"O1",...}

  GET /order/O1
  >>> {"id":"O1","totalAmount":37000}
  ```

DB PERSISTENCE (mandatory)
- Store the db state in a local file `db.json` (in the current working directory).
- Each test file = one invocation of the executable.
- On each invocation:
  - Start with empty state (clear or ignore existing `db.json`).
  - After processing each request, write the updated db state to `db.json`.
- The `db.json` file is for debugging/inspection purposes; tests rely on stdout output.

SEMANTIC RULES (must match policy + scenarios)
- The policies in `shop-policy.md` are authoritative.
- The scenarios in `test-scenario.md` are the reference calculations.
- Ensure discounts, coupons, points, shipping, and refunds follow the stated priorities, rounding, and edge cases.

OUTPUT/IO CONSTRAINTS (strict)
- Print one line of JSON to STDOUT per request (no extra logs).
- The executable is invoked with no command-line arguments.
- Stderr should be empty if possible.

IMPLEMENTATION CONSTRAINTS (for fair comparison)
- Use ONLY the target language's standard library.
- No external packages/frameworks.
- Keep the implementation deterministic.

LOGGING (mandatory)
- You MUST keep a detailed work log in a per-language file:
  - Path: `workloads/ecommerce/{{LANGUAGE}}/log.md`
- Update `log.md` continuously as you work (not only at the end). Each major step must have:
  - What you did (design decisions, alternatives considered, file changes)
  - Why you did it (link back to policy/tests)
  - The outcome (what now passes/fails, next action)
- If you have completed the task, append a final line `Task Complete.` to `log.md`.

DELIVERABLES
Produce:
1) The full source code (as files to create/update under `workloads/ecommerce/{{LANGUAGE}}/`).
2) Exact build instructions (one command, if possible).
3) Exact run instructions compatible with:
   `python3 workloads/ecommerce/runtest.py <path-to-executable> workloads/ecommerce/tests`
4) You must run the test suite and pass all tests before declaring completion.

NOW WAIT FOR THE USER TO PROVIDE THE TARGET LANGUAGE NAME (ONLY).
When you receive it, replace {{LANGUAGE}} and begin implementation immediately.
