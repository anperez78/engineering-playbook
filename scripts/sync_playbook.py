#!/usr/bin/env python3
"""Sync explicitly managed files from a trusted playbook release; unlisted files are untouched."""
from __future__ import annotations
import argparse, json, shutil, sys
from pathlib import Path, PurePosixPath

def safe_relative_path(value: str) -> Path:
    p = PurePosixPath(value)
    if p.is_absolute() or not value or any(part in ("..", "") for part in p.parts):
        raise ValueError(f"Unsafe managed path: {value!r}")
    return Path(*p.parts)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path, help="Release managed/ directory")
    parser.add_argument("--target", default=Path.cwd(), type=Path)
    parser.add_argument("--version", required=True)
    parser.add_argument("--check", action="store_true", help="Check drift without writing")
    args = parser.parse_args()
    source, target = args.source.resolve(), args.target.resolve()
    try:
        manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
        if manifest.get("schema_version") != 1:
            raise ValueError("Unsupported manifest schema")
        paths = manifest.get("managed_paths")
        if not isinstance(paths, list) or not all(isinstance(p, str) for p in paths):
            raise ValueError("manifest.json needs managed_paths: list[str]")
        if len(paths) != len(set(paths)):
            raise ValueError("Duplicate paths in managed_paths")
        stale = []
        for raw in paths:
            rel = safe_relative_path(raw)
            src, dst = (source / rel).resolve(), (target / rel).resolve()
            if source not in src.parents or (dst != target and target not in dst.parents):
                raise ValueError(f"Path escapes source/target: {raw}")
            if not src.is_file():
                raise FileNotFoundError(f"Missing managed source file: {src}")
            if not dst.is_file() or src.read_bytes() != dst.read_bytes():
                stale.append(raw)
                if not args.check:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
        if args.check:
            if stale:
                print("Managed files are out of date:\n" + "\n".join(f" - {p}" for p in stale))
                return 1
            print("Managed files are up to date.")
            return 0
        meta = target / ".engineering-playbook" / "manifest.json"
        meta.parent.mkdir(parents=True, exist_ok=True)
        meta.write_text(json.dumps({"playbook_version": args.version, "managed_paths": paths}, indent=2) + "\n", encoding="utf-8")
        print(f"Synchronized {len(paths)} managed paths to playbook {args.version}.")
        if stale: print("Updated:\n" + "\n".join(f" - {p}" for p in stale))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
