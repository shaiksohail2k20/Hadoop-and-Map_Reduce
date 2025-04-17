#!/usr/bin/env python3
import sys

current_year = None
count = 0

for line in sys.stdin:
    try:
        year, val = line.strip().split("\t")
        val = int(val)
    except:
        continue

    if year == current_year:
        count += val
    else:
        if current_year is not None:
            print(f"{current_year}\t{count}")
        current_year = year
        count = val

if current_year:
    print(f"{current_year}\t{count}")
