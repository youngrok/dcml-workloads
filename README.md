The DCML (Development Cost Measurement by LLM) method provides workload design principles and three representative workloads used in this repository. These workloads are designed to be solvable by coding agents from a single prompt without human intervention.

# Workload Design Principles
1. Regardless of task type or target stack, a single prompt must allow an AI agent to complete the task end-to-end.
   1. Describe all required information in `plan.md`.
   2. Execute the task using a single prompt, e.g., "Read plan.md and complete the task in {{LANGUAGE}}."
   3. If additional files are needed, describe their roles in `plan.md`.
   4. Provide automated test cases so the agent can iterate and complete the task.
2. Minimize confounding factors beyond the programming language.
   1. Provide scripts that run tests in a language-agnostic way and verify results.
   2. Restrict I/O to stdin/stdout whenever possible.
   3. Disallow external libraries.
3. Use detailed logging to verify that the task is executed without gaming and measures the intended target.
   1. Record the LLM's working process.
   2. Record the final code.
   3. Record metadata such as token usage as fully as possible.
4. Select realistic tasks where language-dependent differences can emerge clearly.

# Representative workloads
## Quicksort
A deterministic sorting workload with strict I/O behavior. This serves as a low-complexity baseline where most coding agents can succeed with minimal difficulty.

## MiniLambda
A small functional-language interpreter with parsing and evaluation semantics. This workload stresses algorithmic complexity and language features relevant to implementing interpreters.

## Ecommerce
A policy-heavy transaction engine covering discounts, coupons, points, shipping, and refunds. This workload emphasizes real-world business logic with many interacting rules.

# Note
We confirm that the representative workloads can be completed end-to-end by `Claude Code v2.0.64` from a single prompt. You can run a workload like this:

```sh
cd quicksort
claude -p "Read plan.md and complete the task in typescript." --dangerously-skip-permissions --output-format=json
```
Python 3 is required because the language-agnostic test runner `runtest.py` is implemented in Python.