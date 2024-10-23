
# README

## Estimating π (Pi)

This folder contains Python scripts that demonstrate two methods for estimating the value of π (pi): the **Leibniz formula** and the **Monte Carlo method**. Both approaches provide an approximation of π, showcasing different mathematical techniques for calculating this fundamental constant.

### Task 1: Leibniz Formula for Pi
The first task implements the Leibniz formula, which approximates π by summing an infinite series (π = 4 × (1 - 1/3 + 1/5 - 1/7 + ...)):

<div align="center">
    <img src="https://latex.codecogs.com/svg.latex?\pi%20=%204%20\times%20\left(1%20-%20\frac{1}{3}%20+%20\frac{1}{5}%20-%20\frac{1}{7}%20+%20\ldots\right)" title="π = 4 × (1 - 1/3 + 1/5 - 1/7 + ...)" style="background-color: white; padding: 5px;" />
</div>

- **Function:** `leibniz_pi(num_terms)`
  - **Parameters:** 
    - `num_terms`: The number of terms in the series to sum. More terms will yield a more accurate approximation.
  - **Returns:** An estimate of π based on the specified number of terms.
  
### Task 2: Monte Carlo Method for Pi
The second task uses the Monte Carlo method, which estimates π by simulating random points in a unit square and counting how many fall within a quarter-circle inscribed within that square.

- **Function:** `monte_carlo_pi(num_points)`
  - **Parameters:** 
    - `num_points`: The total number of random points to generate. Increasing this number improves the accuracy of the π estimation.
  - **Returns:** An estimate of π based on the ratio of points that land inside the quarter-circle compared to the total number of points.

### Output
Both scripts print the estimated value of π based on their respective methods when executed with `num_terms` and `num_points` set to 1,000,000.