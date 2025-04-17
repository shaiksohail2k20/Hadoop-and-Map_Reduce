import matplotlib.pyplot as plt

years = []
counts = []

with open("earthquake_counts.txt", "r") as f:
    for line in f:
        year, count = line.strip().split("\t")
        years.append(int(year))
        counts.append(int(count))

plt.figure(figsize=(10,5))
plt.plot(years, counts, marker='o')
plt.title("Earthquakes per Year")
plt.xlabel("Year")
plt.ylabel("Number of Earthquakes")
plt.grid(True)
plt.tight_layout()
plt.savefig("earthquakes_per_year.png")
plt.show()
