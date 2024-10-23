
# README

## Random Walk Simulation

This folder contains a Python script that simulates a **Random Walk** in a one-dimensional space. The program demonstrates how an entity randomly moves left or right within defined boundaries based on the outcome of simulated coin flips. 

### Overview
In this simulation, the position of the entity is represented along a line with two walls marking the boundaries. The entity starts at the center position and moves randomly to the left or right with each flip of a coin. The simulation continues until the entity reaches either wall, allowing us to observe the path taken during the random walk.

### Components of the Program
- **Variables:**
  - `left_wall` and `right_wall`: These define the movement boundaries for the entity, set at -15 and 15, respectively.
  - `position`: This variable tracks the entity's current position, starting at 0.
  - `flips`: This counts the total number of coin flips made during the simulation.

- **Functions:**
  - `flip_coin()`: Simulates a coin flip by randomly returning -1 (indicating a move to the left) or +1 (indicating a move to the right).
  - `display_position(position, left_wall, right_wall)`: Visualizes the current position of the entity within the walls. The entity's position is represented by an asterisk (*) on the console, along with the current position value.

### Output
The program prints a visual representation of the entity’s movement along the line, displaying its position relative to the left and right walls in real-time. Once the entity reaches one of the walls, the total number of flips (or steps taken) is displayed.

### Example Usage
To execute the simulation, run the script in a Python environment. Observe how the entity moves based on the random outcomes of coin flips, and note the total number of moves required to reach one of the walls.
