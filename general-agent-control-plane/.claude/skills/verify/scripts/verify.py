#!/usr/bin/env python3
# verify.py — backend/SRE verification CLI (see ../SKILL.md)
#
# Usage:
#   verify.py list [--config PATH]
#   verify.py run <check> [--task ID] [--config PATH]
#   verify.py all [--task ID] [--config PATH]
#
# Each check is a shell command defined in verify.config.yaml (simple format:
# a "checks:" line, then one "  name: command" line per check). The command
# runs in the current directory (run this from the repo root). Its exit code
# is the verdict. Output is filed as evidence:
#   evidence/<task>/<check>.log   — full raw output
#   evidence/<task>/report.json   — per-check status, exit code, duration
#
# Task ID comes from --task, else $AGENT_TASK_ID, else "local".
# A check missing from the config exits 2 and prints NOT CONFIGURED —
# that means the check does not exist yet, never that it passed.

import json
import os
import subprocess
import sys
import time
from pathlib import Path

DEFAULT_CONFIG_NAMES = ["verify.config.yaml", ".claude/skills/verify/verify.config.yaml"]


def find_config(explicit):
    if explicit:
        return Path(explicit)
    for name in DEFAULT_CONFIG_NAMES:
        p = Path(name)
        if p.exists():
            return p
    return None


def load_checks(config_path):
    checks = {}
    if config_path is None or not config_path.exists():
        return checks
    in_checks = False
    for raw in config_path.read_text().splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.strip() == "checks:":
            in_checks = True
            continue
        if in_checks:
            if not line.startswith((" ", "\t")):
                in_checks = False
                continue
            stripped = line.strip()
            if ":" in stripped:
                name, _, cmd = stripped.partition(":")
                checks[name.strip()] = cmd.strip()
    return checks


def evidence_dir(task):
    d = Path("evidence") / task
    d.mkdir(parents=True, exist_ok=True)
    return d


def update_report(task, check, entry):
    d = evidence_dir(task)
    report_path = d / "report.json"
    report = {"task": task, "checks": {}}
    if report_path.exists():
        try:
            report = json.loads(report_path.read_text())
        except json.JSONDecodeError:
            pass
    report["checks"][check] = entry
    statuses = [c["status"] for c in report["checks"].values()]
    report["overall"] = "fail" if "fail" in statuses else "pass"
    report_path.write_text(json.dumps(report, indent=2))
    return report_path


def run_check(name, checks, task):
    if name not in checks or not checks[name] or checks[name].startswith("TODO"):
        print(f"NOT CONFIGURED: check '{name}' has no real command in verify.config.yaml.")
        print("Add it (see verify.config.example.yaml) — until then this check does not exist,")
        print("and it must never be reported as passed.")
        return 2
    cmd = checks[name]
    d = evidence_dir(task)
    log_path = d / f"{name}.log"
    print(f"RUN {name}: {cmd}")
    start = time.time()
    with log_path.open("w") as log:
        log.write(f"$ {cmd}\n")
        log.flush()
        proc = subprocess.run(cmd, shell=True, stdout=log, stderr=subprocess.STDOUT)
    duration = round(time.time() - start, 2)
    status = "pass" if proc.returncode == 0 else "fail"
    entry = {
        "status": status,
        "exit_code": proc.returncode,
        "duration_s": duration,
        "command": cmd,
        "log": str(log_path),
    }
    report_path = update_report(task, name, entry)
    print(f"{status.upper()} {name} (exit {proc.returncode}, {duration}s) — log: {log_path}, report: {report_path}")
    return proc.returncode


def main(argv):
    args = argv[1:]
    config_explicit = None
    task = os.environ.get("AGENT_TASK_ID", "local")
    cleaned = []
    i = 0
    while i < len(args):
        if args[i] == "--config" and i + 1 < len(args):
            config_explicit = args[i + 1]
            i += 2
        elif args[i] == "--task" and i + 1 < len(args):
            task = args[i + 1]
            i += 2
        else:
            cleaned.append(args[i])
            i += 1

    if not cleaned:
        print(__doc__)
        return 2

    config_path = find_config(config_explicit)
    checks = load_checks(config_path)
    action = cleaned[0]

    if action == "list":
        if not checks:
            print("No checks configured. Copy verify.config.example.yaml to verify.config.yaml and fill it in.")
            return 2
        print(f"Config: {config_path}")
        for name, cmd in checks.items():
            state = "ready" if cmd and not cmd.startswith("TODO") else "TODO (not configured)"
            print(f"  {name}: {state} — {cmd}")
        return 0

    if action == "run":
        if len(cleaned) < 2:
            print("Usage: verify.py run <check> [--task ID]")
            return 2
        return run_check(cleaned[1], checks, task)

    if action == "all":
        if not checks:
            print("No checks configured — see verify.py list.")
            return 2
        worst = 0
        for name in checks:
            rc = run_check(name, checks, task)
            if rc != 0:
                worst = rc if worst == 0 else worst
        return worst

    print(f"Unknown action: {action} (use list, run <check>, or all)")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
