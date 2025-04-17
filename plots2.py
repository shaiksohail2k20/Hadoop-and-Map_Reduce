import matplotlib.pyplot as plt

def read_data(filepath):
    data = {}
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) != 2:
                continue
            year, val = parts
            try:
                data[int(year)] = float(val)
            except:
                continue
    return dict(sorted(data.items()))


max_mag_data = read_data('max_mag_output.txt')
avg_mag_data = read_data('avg_mag_output.txt')
strong_quakes_data = read_data('strong6_mag_output.txt')

# Plot Max Magnitude
plt.figure(figsize=(10, 5))
plt.plot(list(max_mag_data.keys()), list(max_mag_data.values()), marker='o', color='red')
plt.title("Maximum Earthquake Magnitude per Year")
plt.xlabel("Year")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("max_magnitude_per_year.png")
plt.show()

# Plot Average Magnitude
plt.figure(figsize=(10, 5))
plt.plot(list(avg_mag_data.keys()), list(avg_mag_data.values()), marker='o', color='blue')
plt.title("Average Earthquake Magnitude per Year")
plt.xlabel("Year")
plt.ylabel("Average Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("avg_magnitude_per_year.png")
plt.show()

# Plot Earthquakes > 6.0
plt.figure(figsize=(10, 5))
plt.bar(list(strong_quakes_data.keys()), list(strong_quakes_data.values()), color='green')
plt.title("Number of Earthquakes > 6.0 Magnitude per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("strong6_quakes_per_year.png")
plt.show()
