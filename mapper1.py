#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split(",")
    if parts[0] == "time" or len(parts) < 5:
        continue
    try:
        year = parts[0].split("-")[0]
        print(f"{year}\t1")
    except:
        continue
