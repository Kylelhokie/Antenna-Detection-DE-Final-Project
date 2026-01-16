import csv
import matplotlib.pyplot as plt
from time import sleep
import randomangles = []      # will store angles you enter
powers = []      # will store corresponding power values
smooth_factor = 0.3  # smoothing weight (0-1)

def get_power_reading():
    """
    Replace this with real SDR reading.
    Currently simulates power in dB for testing.
    """
    # Example: random value around -60 dB
    power_db = -60 + random.uniform(-5, 5)
    return power_db

# DATA COLLECTION LOOP

print("Manual RDF Data Collection")
print("Enter angle in degrees. Type 'done' when finished.\n")

smoothed_power = None

while True:
    angle_input = input("Enter current angle (or 'done'): ")
    if angle_input.lower() == 'done':
        break
    try:
        angle = float(angle_input)
    except ValueError:
        print("Invalid input, try again.")
        continue

    # Get multiple readings and average
    readings = [get_power_reading() for _ in range(5)]
    avg_power = sum(readings)/len(readings)

    # Apply smoothing
    if smoothed_power is None:
        smoothed_power = avg_power
    else:
        smoothed_power = smooth_factor * avg_power + (1 - smooth_factor) * smoothed_power

    # Store data
    angles.append(angle)
    powers.append(smoothed_power)

    print(f"Angle {angle}° → Power: {smoothed_power:.2f} dB\n")
    sleep(0.2)  
filename = "rdf_data.csv"
with open(filename, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Angle", "Power_dB"])
    for a, p in zip(angles, powers):
        writer.writerow([a, p])

print(f"\nData saved to {filename}")

plt.figure(figsize=(6,6))
plt.plot(angles, powers, marker='o')
plt.xlabel("Angle (degrees)")
plt.ylabel("Smoothed Power (dB)")
plt.title("RDF: Power vs Angle")
plt.grid(True)
plt.show()
