#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Case:
    file: pathlib.Path
    line_no: int
    program: str
    expect: str


def parse_markdown_tests(path: pathlib.Path) -> List[Case]:
    """
    Markdown test format (md-only), delimiter-based:

    Each case must look like:

      ## case: <name>
      <<<
      <program... may be multi-line, may be empty>
      >>>
      <expected single-line output>

    Notes:
    - Content outside cases is ignored.
    - The program is the raw text between <<< and >>>, with a trailing newline appended.
    - Expect is the first non-empty line after >>> (up to the next case or EOF).
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    cases: List[Case] = []

    def find_next(start: int, pred) -> int:
        i = start
        while i < len(lines):
            if pred(lines[i]):
                return i
            i += 1
        return -1

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if line.startswith("## case:"):
            case_line_no = i + 1

            # program section: <<< ... >>>
            j = find_next(i + 1, lambda s: s.strip() == "<<<")
            if j == -1:
                raise ValueError(f"{path}:{case_line_no}: missing '<<<' program delimiter")
            k = find_next(j + 1, lambda s: s.strip() == ">>>")
            if k == -1:
                raise ValueError(f"{path}:{j+1}: missing '>>>' delimiter to end program block")
            program = "\n".join(lines[j + 1 : k]).rstrip("\n") + "\n"

            # expect: first non-empty line after >>>
            expect = ""
            e = k + 1
            while e < len(lines):
                if lines[e].startswith("## case:"):
                    break
                t = lines[e].strip()
                if t:
                    expect = t
                    break
                e += 1
            if not expect:
                raise ValueError(f"{path}:{k+1}: expected output must be non-empty (e.g., 'OK 1' or 'ERR PARSE_ERROR')")

            cases.append(Case(file=path, line_no=case_line_no, program=program, expect=expect))
            i = k + 1
            continue
        i += 1

    return cases


def parse_tests(path: pathlib.Path) -> List[Case]:
    if path.suffix.lower() != ".md":
        raise ValueError(f"{path}: only Markdown tests (*.md) are supported")
    return parse_markdown_tests(path)


def run_case(exe: str, case: Case, timeout_sec: float) -> Tuple[bool, str, str]:
    """
    Returns (passed, actual, detail)
    detail includes stderr and other diagnostics.
    """
    try:
        p = subprocess.run(
            [exe],
            input=case.program.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout_sec,
        )
    except subprocess.TimeoutExpired:
        actual = "ERR TIMEOUT"
        detail = f"timeout after {timeout_sec}s"
        return (case.expect == actual, actual, detail)

    stdout = p.stdout.decode("utf-8", errors="replace").strip()
    stderr = p.stderr.decode("utf-8", errors="replace").strip()

    # normalize: only first line matters
    actual = stdout.splitlines()[0].strip() if stdout else ""
    if not actual:
        actual = "ERR EMPTY_OUTPUT"

    passed = (actual == case.expect)
    detail = ""
    if stderr:
        detail += f"stderr:\n{stderr}\n"
    detail += f"exit_code: {p.returncode}"
    return (passed, actual, detail)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("executable", help="Path to MiniLambda implementation executable")
    ap.add_argument("tests_dir", help="Directory containing Markdown test files (*.md)")
    ap.add_argument("--timeout", type=float, default=1.0, help="Per-test timeout seconds (default: 1.0)")
    args = ap.parse_args()

    exe = args.executable
    tests_dir = pathlib.Path(args.tests_dir)

    if not tests_dir.exists() or not tests_dir.is_dir():
        print(f"tests_dir is not a directory: {tests_dir}", file=sys.stderr)
        return 2

    test_files = sorted(tests_dir.rglob("*.md"))
    if not test_files:
        print(f"No .md files found under: {tests_dir}", file=sys.stderr)
        return 2

    cases: List[Case] = []
    for tf in test_files:
        cases.extend(parse_tests(tf))

    total = len(cases)
    failed = 0

    for idx, case in enumerate(cases, 1):
        ok, actual, detail = run_case(exe, case, args.timeout)
        if not ok:
            failed += 1
            print(f"\nFAIL [{idx}/{total}] {case.file}:{case.line_no}")
            print("Program:")
            print(case.program.rstrip("\n"))
            print(f"Expected: {case.expect}")
            print(f"Actual:   {actual}")
            if detail:
                print(detail)

    passed = total - failed
    print(f"\nRESULT: {passed}/{total} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())