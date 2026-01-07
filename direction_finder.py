import csv

def read_power_csv(filename):
    power_values = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # Columns 6 onward have power values
            for val in row[5:]:
                power_values.append(float(val))
    return power_values

powers = read_power_csv('/home/kyle/test_scan.csv')
print("Read", len(powers), "power values:")
print(powers[:20])  # Show first 20 values


import matplotlib.pyplot as plt

# powers list comes from your previous read_power_csv function
# if you haven’t already, make sure this line runs:
# powers = read_power_csv('/home/kyle/test_scan.csv')

# simulate angles assuming 360 degrees total, evenly spaced
num_values = len(powers)
angles = [i * 360 / num_values for i in range(num_values)]

# plot power vs. angle
plt.figure(figsize=(8,4))
plt.plot(angles, powers, marker='o')
plt.title("Simulated Antenna Rotation Power")
plt.xlabel("Angle (degrees)")
plt.ylabel("Signal Power (dB)")
plt.grid(True)
plt.show()
