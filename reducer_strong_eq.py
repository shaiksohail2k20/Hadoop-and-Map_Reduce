#!/usr/bin/env python3
import sys

current_year = None
total = 0

for line in sys.stdin:
    try:
        year, count = line.strip().split("\t")
        count = int(count)

        if current_year == year:
            total += count
        else:
            if current_year:
                print(f"{current_year}\t{total}")
            current_year = year
            total = count
    except:
        continue

if current_year:
    print(f"{current_year}\t{total}")
