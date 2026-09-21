"""Read-only comparison of the all-current skill source and installed copies.

Usage: python -B -X utf8 local/verify_install.py INSTALLED_ROOT [CLAUDE_ROOT]
The CLI installer owns copying/linking. This check owns no installation behavior.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
BUCKETS = ("engineering", "productivity", "in-progress", "misc")


def files(path: Path) -> dict[str, str]:
    """Compare bytes, including reference files and invocation metadata."""
    return {
        file.relative_to(path).as_posix(): hashlib.sha256(file.read_bytes()).hexdigest()
        for file in sorted(path.rglob("*"))
        if file.is_file()
    }


def sources(root: Path = ROOT) -> dict[str, Path]:
    result = {}
    for bucket in BUCKETS:
        for entry in sorted((root / "skills" / bucket).glob("*/SKILL.md")):
            name = entry.parent.name
            if name in result:
                raise ValueError(f"Duplicate skill: {name}")
            result[name] = entry.parent
    return result


def compare(expected: dict[str, str], actual: dict[str, str]) -> dict[str, list[str]]:
    return {
        "missing": sorted(expected.keys() - actual.keys()),
        "extra": sorted(actual.keys() - expected.keys()),
        "changed": sorted(key for key in expected.keys() & actual.keys() if expected[key] != actual[key]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("installed_root", type=Path)
    parser.add_argument("claude_root", type=Path, nargs="?")
    args = parser.parse_args()
    result = {"source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(), "skills": {}}
    failures = []
    for name, source in sources().items():
        expected = files(source)
        delta = compare(expected, files(args.installed_root / name))
        alias_delta = compare(expected, files(args.claude_root / name)) if args.claude_root else None
        result["skills"][name] = {"bucket": source.parent.name, "files": expected, "installed_delta": delta, "claude_delta": alias_delta}
        if any(delta.values()) or (alias_delta is not None and any(alias_delta.values())):
            failures.append(name)
    result["failures"] = failures
    print(json.dumps(result, indent=2))
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
