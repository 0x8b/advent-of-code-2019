#!/usr/bin/env python

import datetime
import os
import subprocess
import sys
from pathlib import Path

import requests

try:
    day = int(sys.argv[-1])
except Exception:
    day = datetime.datetime.today().day

assert 1 <= day <= 25

script = Path(f"{str(day).zfill(2)}.py")

if script.exists():
    sys.exit("Script already exists.")

edition = 2019
aoc_url = f"https://adventofcode.com/{edition}/day/{day}"

if not (session := os.getenv("aoc-session")):
    sys.exit("Missing session ID.")

response = requests.get(aoc_url + "/input", cookies={"session": session})

source = f"""\
#!/usr/bin/env python
\n\n
with open(__file__, "r") as f:
    c = f.read()
    lines = iter(c[c.rindex("🎅") + 1 : c.rindex("🐍")].rstrip().split("\\n"))
\n\n
\"\"\"🎅{response.text}🐍\"\"\"
"""

script.write_text(source, encoding="utf8")

os.system(f"code {str(script)}")
subprocess.run(["firefox", "--new-tab", aoc_url])
sys.exit()
