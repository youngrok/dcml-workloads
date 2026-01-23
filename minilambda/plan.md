You are implementing an interpreter for the MiniLambda language as an experimental workload.

IMPORTANT INTERACTION RULE
- The next user message will contain ONLY the target programming language name (e.g., "Rust", "Python 3.12").
- Do NOT ask follow-up questions. Do NOT request additional specs. Proceed immediately.
- Treat the language name as the only variable; everything else is fixed by the repository files.

WORKSPACE INITIALIZATION (mandatory)
- If the per-language workspace directory does not exist, create it:
  - Target directory: `workloads/minilambda/{{LANGUAGE}}/`
- Work only in the language root directory above; do not create or use any numbered or archived subdirectories.

DEVELOPMENT ENVIRONMENT (mandatory)
- Prefer using tools already installed on the current OS and available on PATH.
  - Do not assume you can install new compilers/runtimes/package managers.
  - When writing build/run instructions, pick commands that work with typical PATH-installed toolchains.
- Special rule for TypeScript:
  - Use `bun` (not `node`, not `ts-node`, not `deno`) for running/building TypeScript solutions.

TARGET LANGUAGE
- Target language: {{LANGUAGE}}  (this will be provided by the user as the next message)

WHAT YOU HAVE ACCESS TO (in this repo)
- Language spec: `workloads/minilambda/spec.md`
- Grammar (EBNF): `workloads/minilambda/grammer.ebnf`
- Test runner: `workloads/minilambda/runtest.py`
- Tests: `workloads/minilambda/tests/*.md` (Markdown case blocks)
  - Markdown test format: each case is:
    - `## case: <name>`
    - `<<<` then the program (multi-line allowed)
    - `>>>` then the expected single-line output (e.g., `OK 7` or `ERR PARSE_ERROR`)

TASK
Implement a MiniLambda interpreter executable that:
1) Reads a MiniLambda program from STDIN (UTF-8).
2) Parses it according to `grammer.ebnf`.
3) Evaluates it according to `spec.md`.
4) Prints EXACTLY ONE LINE to STDOUT (no extra logs), matching the test oracle:
   - Success: `OK <value>`
     - <value> is either an unsigned decimal integer (e.g., `0`, `42`) or `true`/`false`.
   - Error: `ERR <CODE>`
     - <CODE> must be one of:
       - PARSE_ERROR
       - UNBOUND_VAR
       - DIV_BY_ZERO
       - TYPE_ERROR
       - TIMEOUT

OUTPUT/IO CONSTRAINTS (strict)
- Only the first line of stdout is checked by `runtest.py`. Still, you MUST emit exactly one line.
- Do not print anything else (no debug prints, no prompts, no stack traces).
- Stderr is ignored for pass/fail but may be printed by the harness on failures; keep it empty if possible.
- The executable is invoked with no command-line arguments.

SEMANTICS (must match spec.md)
- Program is exactly one expression; its value is the program result.
- Values: integers + booleans only.
- Evaluation: strict (eager), call-by-value, no side effects.
- `let` is implicitly recursive (the bound identifier is visible within its own definition).
- Functions are first-class, single-argument, lexically scoped closures.
- Division by zero must be `ERR DIV_BY_ZERO`.
- Referencing an undefined variable must be `ERR UNBOUND_VAR`.
- Any syntax error must be `ERR PARSE_ERROR`.

IMPLEMENTATION CONSTRAINTS (for fair comparison)
- Use ONLY the target language's standard library.
- No external packages/frameworks.
- No parser generators.
- Implement a handwritten lexer + parser (precedence/associativity per spec).
- Keep the implementation deterministic.

LOGGING (mandatory)
- You MUST keep a detailed work log in a per-language file:
  - Path: `workloads/minilambda/{{LANGUAGE}}/log.md`
- Update `log.md` continuously as you work (not only at the end). Each major step must have:
  - What you did (design decisions, alternatives considered, file changes)
  - Why you did it (link back to `spec.md` / `grammer.ebnf` / failing tests)
  - The outcome (what now passes/fails, next action)
- If you have completed the task, append a final line `Task Complete.` to `log.md`.
- Keep the log concrete and diff-friendly (bullet points, short sections, links to relevant files/tests).

DELIVERABLES
Produce:
1) The full source code (as files to create/update under `workloads/minilambda/{{LANGUAGE}}/`).
   - Must include `workloads/minilambda/{{LANGUAGE}}/log.md` with the step-by-step record.
2) Exact build instructions (one command, if possible).
3) Exact run instructions that produce an executable compatible with:
     `python3 workloads/minilambda/runtest.py <path-to-executable> workloads/minilambda/tests`

ROBUSTNESS
- Your interpreter must handle arbitrary whitespace/newlines between tokens.
- Must complete within the harness timeout (default 1.0s per test).
- If you implement internal step limits to avoid non-termination, map it to `ERR TIMEOUT`.

NOW WAIT FOR THE USER TO PROVIDE THE TARGET LANGUAGE NAME (ONLY).
When you receive it, replace {{LANGUAGE}} and begin implementation immediately.
