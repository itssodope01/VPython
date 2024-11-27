import numpy as np
import matplotlib.pyplot as plt


def sample_point(vertices):

    x_min = min(vertex[0] for vertex in vertices)
    x_max = max(vertex[0] for vertex in vertices)
    y_min = min(vertex[1] for vertex in vertices)
    y_max = max(vertex[1] for vertex in vertices)
    x = np.random.uniform(x_min, x_max)
    y = np.random.uniform(y_min, y_max)
    return np.array([x, y])


def simulate_points(vertices, pixels=10 ** 6, fraction=0.5, avoid_repeats=True):

    num_vertices = len(vertices)

    x_points = np.empty(pixels)
    y_points = np.empty(pixels)

    # initial random point
    current_point = sample_point(vertices)
    x_points[0], y_points[0] = current_point
    last_vertex = -1

    for i in range(1, pixels):
        if avoid_repeats:
            # vertex different from the last one
            choices = list(range(num_vertices))
            if last_vertex in choices:
                choices.remove(last_vertex)
            chosen_index = np.random.choice(choices)
        else:
            # any vertex
            chosen_index = np.random.randint(0, num_vertices)

        chosen_vertex = vertices[chosen_index]

        # new point/ mid-point
        current_point = current_point + fraction * (chosen_vertex - current_point)

        # new point stored
        x_points[i], y_points[i] = current_point

        # last vertex update
        last_vertex = chosen_index

        if (i + 1) % (pixels // 10) == 0:
            print(f"Progress: {(i + 1) / pixels * 100:.1f}%")

    return x_points, y_points


def plot_fractal(x, y, filename='fractal_fourPoints.png', figsize=(8, 8), dpi=300):

    plt.figure(figsize=figsize, dpi=dpi)
    plt.scatter(x, y, s=0.1, color='black', marker='o')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=dpi)
    plt.close()
    print(f"Fractal image saved as {filename}")


def main():
    # vertices A(0,0), B(1,0), C(1,1), D(0,1)
    A = np.array([0.0, 0.0])
    B = np.array([1.0, 0.0])
    C = np.array([1.0, 1.0])
    D = np.array([0.0, 1.0])
    vertices = [A, B, C, D]

    pixels = 10 ** 6

    fraction = 0.5  # choose mid-point

    avoid_repeats = True

    x, y = simulate_points(vertices, pixels, fraction, avoid_repeats)

    print("Plotting fractal...")
    plot_fractal(x, y, filename='fractal_fourPoints.png')
    print("Done.")


if __name__ == "__main__":
    main()
