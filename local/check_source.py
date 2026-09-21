"""Structural checks for this fork. Run with an isolated PyYAML environment.

uv run --isolated --no-project --with PyYAML==6.0.3 python -B -X utf8 local/check_source.py
"""

import json
from pathlib import Path
import re

import yaml

from verify_install import ROOT, sources


def main():
    skills = sources()
    for name, path in skills.items():
        text = (path / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", text, re.S)
        assert match, path
        front = yaml.safe_load(match[1])
        assert front["name"] == name and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name), path
        assert isinstance(front["description"], str) and 0 < len(front["description"]) <= 1024, path
        ui = yaml.safe_load((path / "agents/openai.yaml").read_text(encoding="utf-8"))
        assert ui.get("policy", {}).get("allow_implicit_invocation", True) == (not front.get("disable-model-invocation", False)), path
    promoted = {"./" + p.relative_to(ROOT).as_posix() for p in skills.values() if p.parent.name in ("engineering", "productivity")}
    manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    assert set(manifest["skills"]) == promoted
    for name in ("assurance-case", "implement", "tdd", "code-review", "ask-matt"):
        skill = skills[name]
        for file in skill.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
                if ":" not in target and not target.startswith("#"):
                    assert (file.parent / target.split("#")[0]).exists(), (file, target)
        doc = (ROOT / "docs/engineering" / f"{name}.md").read_text(encoding="utf-8")
        for heading in ("What it does", "When to reach for it", "Common questions", "It's working if", "Where it fits"):
            assert f"## {heading}" in doc, (name, heading)
    print(json.dumps({"skills": len(skills), "invocation_alignment": "pass", "promoted_manifest": "pass", "changed_skill_links_and_docs": "pass"}))


if __name__ == "__main__":
    main()
