import numpy as np
import matplotlib.pyplot as plt


def sample_point(A, B, C):
    s, t = sorted(np.random.uniform(0, 1, 2))
    return A + s * (B - A) + t * (C - A)


def simulate_points(vertices, pixels):

    x_points = np.empty(pixels)
    y_points = np.empty(pixels)

    # initial sample point
    current_point = sample_point(vertices[0], vertices[1], vertices[2])
    x_points[0], y_points[0] = current_point


    for i in range(1, pixels):
        # randomly choose A, B or C
        chosen_vertex = vertices[np.random.randint(0, 3)]

        # midpoint
        current_point = (current_point + chosen_vertex) / 2

        # store the point
        x_points[i], y_points[i] = current_point

        if (i + 1) % (pixels // 10) == 0:
            print(f"Progress: {(i + 1) / pixels * 100:.1f}%")

    return x_points, y_points


def plot_fractal(x, y, filename='fractal.png', figsize=(8, 8), dpi=300):

    plt.figure(figsize=figsize, dpi=dpi)
    plt.scatter(x, y, s=0.1, color='black', marker='o')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()
    print(f"Fractal image saved as {filename}")


def main():
    # vertices A(0,0), B(0,1), C(0.5,1)
    A = np.array([0.0, 0.0])
    B = np.array([1.0, 0.0])
    C = np.array([0.5, 1.0])
    vertices = [A, B, C]

    pixels = 10 ** 6

    x, y = simulate_points(vertices, pixels)

    print("Plotting fractal...")
    plot_fractal(x, y, filename='fractal.png')
    print("Done.")


if __name__ == "__main__":
    main()
