import numpy as np
import math
import csv

dimensions = 20
points = 10 ** 6
radius = 1

output_data = []

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def get_known_volume(dim):
    if dim == 1:
        return 2
    elif dim == 2:
        return np.pi
    elif dim == 3:
        return 4 / 3 * np.pi
    return None

for Nd in range(1, dimensions + 1):
    square_points = np.random.uniform(-radius, radius, (points, Nd))
    distances_squared = np.sum(square_points ** 2, axis=1)

    # points inside hypersphere
    No = np.sum(distances_squared <= radius ** 2)
    Ns = points

    # volume of the Nd dimensional hypercube
    Vs = (2 * radius) ** Nd
    Vo_calculated = Vs * No / Ns

    # Mathematical volume
    if Nd % 2 == 0:
        Vo_mathematical = (math.pi ** (Nd / 2)) / factorial(Nd // 2)
    else:
        Vo_mathematical = (math.pi ** (Nd / 2)) / math.gamma(Nd / 2 + 1)

    ratio = Vo_calculated / Vo_mathematical

    # Verification against known values
    known_vol = get_known_volume(Nd)
    if known_vol is not None:
        print(f"Dimension {Nd}:")
        print(f"  Calculated: {Vo_calculated:.6f}")
        print(f"  Mathematical: {Vo_mathematical:.6f}")
        print(f"  Known value: {known_vol:.6f}")
        print(f"  Ratio: {ratio:.6f}\n")

    output_data.append([Nd, Vo_calculated, ratio])

with open('volume_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Dimension", "Calculated Volume", "Calculated/Mathematical Volume Ratio"])
    writer.writerows(output_data)

print("Volume data has been saved to volume_data.csv")
