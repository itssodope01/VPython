
# Volume Estimation of Hyperspheres

This project estimates the volume of hyperspheres up to 20 dimensions using the Monte Carlo method. It calculates both the estimated volume and the theoretical volume based on mathematical formulas, allowing for a comparison of the two.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Output](#output)
- [How It Works](#how-it-works)
- [License](#license)

## Overview

The volume of a hypersphere can be mathematically derived, but this project uses Monte Carlo simulation to estimate the volume for various dimensions. The estimated volume is then compared to the theoretical volume to analyze accuracy.

## Requirements

To run the code, you need the following:

- Python 3.x
- NumPy
- CSV module (included in Python's standard library)

You can install NumPy using pip:

```bash
pip install numpy
```

## Usage

1. Go to task Directory:

   ```bash
   cd HyperSphereVolume
   ```

2. Run the script:

   ```bash
   python volume_estimation.py
   ```

3. The results will be saved in a CSV file named `volume_data.csv`.

## Output

The program generates a CSV file with the following columns:

- **Dimension**: The number of dimensions for the hypersphere.
- **Calculated Volume**: The estimated volume of the hypersphere using the Monte Carlo method.
- **Calculated/Mathematical Volume Ratio**: The ratio of the calculated volume to the theoretical volume.


## How It Works

- The script generates random points uniformly distributed within a hypercube in \(Nd\) dimensions.
- It calculates the distances of these points from the origin to determine how many lie within the unit hypersphere.
- The estimated volume of the hypersphere (Vo) is calculated based on the ratio of points within the hypersphere to total points.
- The theoretical volume (Vt) is derived from the formula:

  For odd dimensions:
  
  ```
  V = π^(Nd/2) / Γ(Nd/2 + 1)
  ```

  For even dimensions:
  
  ```
  V = π^(Nd/2) / (Nd/2)!
  ```

- Finally, the results are saved in a CSV file for analysis.