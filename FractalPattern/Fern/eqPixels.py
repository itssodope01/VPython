import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def generate_fern(n_points, x_start=0, y_start=0):
    x = np.zeros(n_points)
    y = np.zeros(n_points)
    x[0], y[0] = x_start, y_start


    probabilities = [0.85, 0.07, 0.07, 0.01]
    cum_prob = np.cumsum(probabilities)

    for i in range(1, n_points):
        r = np.random.random()
        x0, y0 = x[i - 1], y[i - 1]
        if r < cum_prob[0]:
            x[i] = 0.85 * x0 + 0.04 * y0
            y[i] = -0.04 * x0 + 0.85 * y0 + 1.6
        elif r < cum_prob[1]:
            x[i] = 0.2 * x0 - 0.26 * y0
            y[i] = 0.23 * x0 + 0.22 * y0 + 1.6
        elif r < cum_prob[2]:
            x[i] = -0.15 * x0 + 0.28 * y0
            y[i] = 0.26 * x0 + 0.24 * y0 + 0.44
        else:
            x[i] = 0
            y[i] = 0.16 * y0

    return x, y

def plot_fern_with_square(x, y, square_coords, filename):
    fig, ax = plt.subplots(figsize=(6, 10), dpi=400)
    ax.scatter(x, y, s=0.1, color='green', marker='.', linewidths=0)
    ax.axis('off')

    # Add the red square to the plot
    square = Rectangle(
        (square_coords['x'], square_coords['y']),
        square_coords['dx'],
        square_coords['dy'],
        edgecolor='red',
        facecolor='none',
        linewidth=1
    )
    ax.add_patch(square)

    plt.tight_layout()
    plt.savefig(filename, dpi=400, bbox_inches='tight')
    plt.close(fig)

# Function to plot the magnified area
def plot_magnified_area(x_zoom, y_zoom, square_coords, filename):
    fig2, ax2 = plt.subplots(figsize=(6, 6), dpi=400)
    ax2.scatter(x_zoom, y_zoom, s=0.1, color='green', marker='.', linewidths=0)
    ax2.axis('off')
    ax2.set_xlim(square_coords['x'], square_coords['x'] + square_coords['dx'])
    ax2.set_ylim(square_coords['y'], square_coords['y'] + square_coords['dy'])

    plt.tight_layout()
    plt.savefig(filename, dpi=400, bbox_inches='tight')
    plt.close(fig2)


if __name__ == '__main__':

    n_points = 5 * 10 ** 6

    # generate the fern points
    x, y = generate_fern(n_points)

    # calculating the data coordinate ranges
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()


    fig_width_cm = 6 * 2.54  # 6 inches to cm
    fig_height_cm = 10 * 2.54  # 10 inches to cm

    # data units per cm
    data_per_cm_x = (x_max - x_min) / fig_width_cm
    data_per_cm_y = (y_max - y_min) / fig_height_cm


    dx = data_per_cm_x * 3
    dy = data_per_cm_y * 3

    # random center
    x_center = np.random.uniform(x_min + dx / 2, x_max - dx / 2)
    y_center = np.random.uniform(y_min + dy / 2, y_max - dy / 2)


    square_x = x_center - dx / 2
    square_y = y_center - dy / 2

    square_coords = {
        'x': square_x,
        'y': square_y,
        'dx': dx,
        'dy': dy
    }


    plot_fern_with_square(x, y, square_coords, 'fractal_fern_with_square.png')

    # magnification
    n_points_magnified = 10 * 10 ** 6
    x_magnified, y_magnified = generate_fern(n_points_magnified, x_center, y_center)

    # points within the square
    mask = (
        (x_magnified >= square_x) & (x_magnified <= square_x + dx) &
        (y_magnified >= square_y) & (y_magnified <= square_y + dy)
    )
    x_zoom = x_magnified[mask]
    y_zoom = y_magnified[mask]


    while len(x_zoom) < n_points:

        x_extra, y_extra = generate_fern(n_points_magnified, x_magnified[-1], y_magnified[-1])

        # new points
        mask_extra = (
            (x_extra >= square_x) & (x_extra <= square_x + dx) &
            (y_extra >= square_y) & (y_extra <= square_y + dy)
        )
        x_zoom = np.concatenate((x_zoom, x_extra[mask_extra]))
        y_zoom = np.concatenate((y_zoom, y_extra[mask_extra]))


        x_magnified = np.concatenate((x_magnified, x_extra))
        y_magnified = np.concatenate((y_magnified, y_extra))


        n_points_magnified += n_points_magnified


    x_zoom = x_zoom[:n_points]
    y_zoom = y_zoom[:n_points]


    plot_magnified_area(x_zoom, y_zoom, square_coords, 'fractal_fern_magnified.png')

    print("Images have been generated and saved successfully.")