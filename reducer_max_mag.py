#!/usr/bin/env python3
import sys

current_year = None
max_mag = 0.0

for line in sys.stdin:
    try:
        year, mag = line.strip().split("\t")
        mag = float(mag)

        if current_year == year:
            max_mag = max(max_mag, mag)
        else:
            if current_year:
                print(f"{current_year}\t{max_mag}")
            current_year = year
            max_mag = mag
    except:
        continue

if current_year:
    print(f"{current_year}\t{max_mag}")
