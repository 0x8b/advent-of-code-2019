#!/usr/bin/env python

import os
import sys
from subprocess import run

completed_process = run(["git", "ls-files", "-m"], capture_output=True, encoding="utf8")
completed_process.check_returncode()

modified_files = completed_process.stdout.strip().split("\n")

for file in modified_files:
    if not file.endswith(".py"):
        continue

    if rc := run(["isort", file]).returncode:
        sys.exit(rc)

    if rc := run(["black", file]).returncode:
        sys.exit(rc)

os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))
run(["git", "add", "."])
