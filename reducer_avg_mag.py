#!/usr/bin/env python3
import sys

current_year = None
sum_mag = 0.0
count = 0

for line in sys.stdin:
    try:
        year, mag = line.strip().split("\t")
        mag = float(mag)

        if current_year == year:
            sum_mag += mag
            count += 1
        else:
            if current_year:
                avg = sum_mag / count if count else 0
                print(f"{current_year}\t{avg:.2f}")
            current_year = year
            sum_mag = mag
            count = 1
    except:
        continue

if current_year:
    avg = sum_mag / count if count else 0
    print(f"{current_year}\t{avg:.2f}")
