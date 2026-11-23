# Writes the one funny line to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
LINE = "I bought a planner to organise my life, and now I just have a very organised record of all the things I didn't do."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
