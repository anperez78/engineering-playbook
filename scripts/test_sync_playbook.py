import json, subprocess, sys
from pathlib import Path
SCRIPT = Path(__file__).with_name("sync_playbook.py")

def test_sync_updates_allowlisted_file_and_preserves_local_file(tmp_path: Path) -> None:
    source, target = tmp_path / "source", tmp_path / "target"
    source.mkdir(); target.mkdir()
    (source / "rules.md").write_text("new\n")
    (source / "manifest.json").write_text(json.dumps({"schema_version": 1, "managed_paths": ["rules.md"]}))
    (target / "rules.md").write_text("old\n")
    (target / "local.md").write_text("keep\n")
    result = subprocess.run([sys.executable, str(SCRIPT), "--source", str(source), "--target", str(target), "--version", "1.2.0"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert (target / "rules.md").read_text() == "new\n"
    assert (target / "local.md").read_text() == "keep\n"
    assert json.loads((target / ".engineering-playbook/manifest.json").read_text())["playbook_version"] == "1.2.0"

def test_check_fails_when_file_is_stale(tmp_path: Path) -> None:
    source, target = tmp_path / "source", tmp_path / "target"
    source.mkdir(); target.mkdir()
    (source / "rules.md").write_text("new\n")
    (source / "manifest.json").write_text(json.dumps({"schema_version": 1, "managed_paths": ["rules.md"]}))
    (target / "rules.md").write_text("old\n")
    result = subprocess.run([sys.executable, str(SCRIPT), "--source", str(source), "--target", str(target), "--version", "1.0.0", "--check"], capture_output=True, text=True)
    assert result.returncode == 1
