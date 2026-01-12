# Antenna-Detection-DE-Final-Project
A directional antenna that is able to rotate and detect the strongest signal


<img width="727" height="371" alt="image" src="https://github.com/user-attachments/assets/23f923ca-5684-4909-aadf-074c5f5c3104" />

<img width="1381" height="703" alt="image" src="https://github.com/user-attachments/assets/7682c29f-8d4e-40df-8a5d-be86f8d81af7" />


<img width="650" height="470" alt="image" src="https://github.com/user-attachments/assets/f80a21d8-8b43-4b48-b5bf-8882df9f89d4" />

Was supposed to use NOAA signal, would not work because I am not actually transmitting anything (162.45000 MHz)

Changed to 2 meter band (144.5000) 
<img width="466" height="183" alt="image" src="https://github.com/user-attachments/assets/a0e155ed-2e1a-4f9c-8a05-aaa6b4e4ac3a" />

<img width="261" height="182" alt="image" src="https://github.com/user-attachments/assets/ca45a401-72a5-4f79-9fc0-9b79668b4f85" />


<img width="856" height="589" alt="image" src="https://github.com/user-attachments/assets/169b47c2-f9f7-44b5-a28b-7d13753abb89" />

<img width="459" height="654" alt="image" src="https://github.com/user-attachments/assets/f4191b68-cf7e-4965-b8ee-e4cb5ff389bc" />

Initially using In-phase Quadrature data (IQ), too complex so switched the RTL_power (uses driver)
def read_power_csv(filename):
    power_values = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            # Columns 6 onward have power values
            for val in row[5:]:
                power_values.append(float(val))
    return power_values
            if len(row) < 6:
                continue

powers = read_power_csv('/home/kyle/test_scan.csv')
print("Read", len(powers), "power values:")
print(powers[:20])  # Show first 20 values
            for raw in row[5:]:
                try:
                    power = float(raw)
                    if -120 < power < 0:
                        power_values.append(power)
                except ValueError:
                    continue

    return power_values
powers = read_power_csv('/home/kyle/test_scan.csv

How this works is basically with the function read_power_csv it gives a path to the CSV file of the RTL_SDRand returns a list of power values as numebrs (dB). power_values = [] will then collect all valid power values found in the CSV. It then displays these power values in six rows from if len(row) < 6:
    Continue, which basically just makes it so that there has to be at least six rows in order to move on. I then filter valid power levels between -120 and 0 for realistic values and to filter out noise. if -120 < power < 0:
    power_values.append(power)

Antenna dipole length measurement for 144.5000 = 3.3 feet (1 meter). Length of the antenna has to match the length of the wavelength

