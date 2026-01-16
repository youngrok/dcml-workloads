You are implementing a Quicksort workload as an experimental task.

IMPORTANT INTERACTION RULE
- The next user message will contain ONLY the target programming language name (e.g., "Rust", "Python 3.12").
- Do NOT ask follow-up questions. Do NOT request additional specs. Proceed immediately.
- Treat the language name as the only variable; everything else is fixed by the repository files.

WORKSPACE INITIALIZATION (mandatory)
- Before writing any code, you MUST reset the per-language workspace directory:
  - Target directory: `workloads/quicksort/{{LANGUAGE}}/`
  - Do not delete anything in the directory

DEVELOPMENT ENVIRONMENT (mandatory)
- Prefer using tools already installed on the current OS and available on PATH.
  - Do not assume you can install new compilers/runtimes/package managers.
  - When writing build/run instructions, pick commands that work with typical PATH-installed toolchains.
- Special rule for TypeScript:
  - Use `bun` (not `node`, not `ts-node`, not `deno`) for running/building TypeScript solutions.

TARGET LANGUAGE
- Target language: {{LANGUAGE}}  (this will be provided by the user as the next message)

TASK
Implement a Quicksort executable that behaves like `sort`:
1) Reads integers from STDIN (UTF-8).
2) Sorts them deterministically using quicksort.
3) Writes the sorted integers to STDOUT, one per line.

INPUT (stdin)
- Text containing integers separated by whitespace (spaces, tabs, or newlines).
- Empty input is allowed and should produce empty output.

Semantics:
- Sort all parsed integers in non-decreasing order.
- Use a deterministic pivot choice (e.g., first element).

OUTPUT (stdout)
- Print the sorted integers, one per line.
- No extra text.

Error rules:
- If any token is not a valid integer -> print exactly `ERR INVALID_INPUT` (single line).

OUTPUT/IO CONSTRAINTS (strict)
- On success, print only sorted integers (one per line).
- On error, print exactly one line: `ERR INVALID_INPUT`.
- The executable is invoked with no command-line arguments.
- Stderr should be empty if possible.

IMPLEMENTATION CONSTRAINTS (for fair comparison)
- Use ONLY the target language's standard library.
- No external packages/frameworks.
- Keep the implementation deterministic.
- Implement quicksort explicitly (no library sort).

LOGGING (mandatory)
- You MUST keep a detailed work log in a per-language file:
  - Path: `workloads/quicksort/{{LANGUAGE}}/log.md`
- Update `log.md` continuously as you work (not only at the end). Each major step must have:
  - What you did (design decisions, alternatives considered, file changes)
  - Why you did it (link back to this spec)
  - The outcome (what now passes/fails, next action)

DELIVERABLES
Produce:
1) The full source code (as files to create/update under `workloads/quicksort/{{LANGUAGE}}/`).
2) Exact build instructions (one command, if possible).
3) Exact run instructions that read JSON from STDIN and output JSON to STDOUT.

NOW WAIT FOR THE USER TO PROVIDE THE TARGET LANGUAGE NAME (ONLY).
When you receive it, replace {{LANGUAGE}} and begin implementation immediately.
