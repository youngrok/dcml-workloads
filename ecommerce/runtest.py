#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path


def parse_http_test(text: str) -> tuple[str, list[str | None]]:
    blocks = []
    current = []
    for raw in text.splitlines():
        if raw.strip() == "":
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(raw)
    if current:
        blocks.append(current)

    requests = []
    expected = []
    for block in blocks:
        exp = None
        req_lines = []
        for line in block:
            if line.startswith(">>>"):
                exp = line.split(">>>", 1)[1].strip()
            else:
                req_lines.append(line)
        if req_lines:
            requests.append("\n".join(req_lines))
            expected.append(exp)
    input_text = "\n\n".join(requests) + "\n"
    return input_text, expected


def run_case(exe: str, inp: str) -> tuple[int, str, str]:
    p = subprocess.run(
        [exe],
        input=inp,
        text=True,
        capture_output=True,
        check=False,
    )
    return p.returncode, p.stdout, p.stderr


def normalize_json(s: str):
    return json.loads(s)


def is_subset(expected, actual) -> bool:
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return False
        for k, v in expected.items():
            if k not in actual:
                return False
            if not is_subset(v, actual[k]):
                return False
        return True
    if isinstance(expected, list):
        if not isinstance(actual, list):
            return False
        if len(expected) > len(actual):
            return False
        for i, v in enumerate(expected):
            if not is_subset(v, actual[i]):
                return False
        return True
    return expected == actual


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
        input_text, expected = parse_http_test(path.read_text(encoding="utf-8"))
        total += len(expected)
        code, out, err = run_case(exe, input_text)
        if code != 0 or err:
            print(f"[FAIL] {path.name}")
            print(f"  exit_code={code}")
            if err:
                print("  stderr:")
                print(err)
            failed += len(expected)
            continue

        outputs = [line for line in out.splitlines() if line.strip() != ""]
        if len(outputs) != len(expected):
            print(f"[FAIL] {path.name}")
            print(f"  expected {len(expected)} response lines, got {len(outputs)}")
            failed += len(expected)
            continue

        for idx, exp in enumerate(expected):
            if exp is None:
                continue
            try:
                out_json = normalize_json(outputs[idx].strip())
                exp_json = normalize_json(exp)
            except json.JSONDecodeError as exc:
                print(f"[FAIL] {path.name} :: request {idx + 1}")
                print(f"  JSON parse error: {exc}")
                failed += 1
                continue
            if not is_subset(exp_json, out_json):
                print(f"[FAIL] {path.name} :: request {idx + 1}")
                print("  expected:")
                print(json.dumps(exp_json, ensure_ascii=False, sort_keys=True))
                print("  got:")
                print(json.dumps(out_json, ensure_ascii=False, sort_keys=True))
                failed += 1
            else:
                print(f"[OK] {path.name} :: request {idx + 1}")

    print(f"\n{total - failed}/{total} tests passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
