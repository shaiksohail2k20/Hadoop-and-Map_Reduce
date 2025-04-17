#!/usr/bin/env python3
import sys

for line in sys.stdin:
    if line.startswith("time"):
        continue
    try:
        parts = line.strip().split(",")
        year = parts[0][:4]
        mag = float(parts[4])
        if mag > 6:
            print(f"{year}\t1")
    except:
        continue
