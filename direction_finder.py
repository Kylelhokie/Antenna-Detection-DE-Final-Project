import csv
import matplotlib.pyplot as plt

def read_power_csv(filename):
    power_values = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) < 6:
                continue

            for raw in row[5:]:
                try:
                    power = float(raw)
                    if -120 < power < 0:
                        power_values.append(power)
                except ValueError:
                    continue

    return power_values
powers = read_power_csv('/home/kyle/test_scan.csv')

print("Read", len(powers), "power values:")
print(powers[:20])

if len(powers) == 0:
    print("No valid power values found — check CSV contents")
    exit()

num_values = len(powers)
angles = [i * 360 / num_values for i in range(num_values)]

plt.figure(figsize=(8, 4))
plt.plot(angles, powers, marker='o')
plt.title("Simulated Antenna Rotation Power")
plt.xlabel("Angle (degrees)")
plt.ylabel("Signal Power (dB)")
plt.grid(True)

plt.tight_layout()
plt.show()
