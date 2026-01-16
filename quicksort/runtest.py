#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


def parse_cases(text: str) -> list[tuple[str, str, str]]:
    cases = []
    name = "unnamed"
    state = "idle"
    inp_lines = []
    exp_lines = []

    def flush_case():
        nonlocal inp_lines, exp_lines, name
        if state == "expect":
            inp = "".join(inp_lines)
            exp = "".join(exp_lines)
            cases.append((name, inp, exp))
        inp_lines = []
        exp_lines = []

    for raw in text.splitlines(keepends=True):
        line = raw.rstrip("\n")
        if line.startswith("## case:"):
            if state == "expect":
                flush_case()
            name = line.split(":", 1)[1].strip() or "unnamed"
            state = "idle"
            continue
        if line.strip() == "<<<":
            if state == "expect":
                flush_case()
            state = "input"
            continue
        if line.strip() == ">>>":
            state = "expect"
            continue

        if state == "input":
            inp_lines.append(raw)
        elif state == "expect":
            exp_lines.append(raw)

    if state == "expect":
        flush_case()

    return cases


def run_case(exe: str, inp: str) -> tuple[int, str, str]:
    p = subprocess.run(
        [exe],
        input=inp,
        text=True,
        capture_output=True,
        check=False,
    )
    return p.returncode, p.stdout, p.stderr


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: runtest.py <executable> [tests_dir]")
        return 2

    exe = sys.argv[1]
    tests_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent / "tests"

    test_files = sorted(tests_dir.glob("*.md"))
    if not test_files:
        print(f"No test files found in {tests_dir}")
        return 2

    total = 0
    failed = 0

    for path in test_files:
        cases = parse_cases(path.read_text(encoding="utf-8"))
        for name, inp, exp in cases:
            total += 1
            code, out, err = run_case(exe, inp)
            out_norm = out.rstrip("\n")
            exp_norm = exp.rstrip("\n")
            if code != 0 or err:
                print(f"[FAIL] {path.name} :: {name}")
                print(f"  exit_code={code}")
                if err:
                    print("  stderr:")
                    print(err)
                failed += 1
                continue
            if out_norm != exp_norm:
                print(f"[FAIL] {path.name} :: {name}")
                print("  expected:")
                print(exp_norm)
                print("  got:")
                print(out_norm)
                failed += 1
            else:
                print(f"[OK] {path.name} :: {name}")

    print(f"\n{total - failed}/{total} tests passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
