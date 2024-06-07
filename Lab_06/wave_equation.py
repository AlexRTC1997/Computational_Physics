import numpy as np
import matplotlib.pyplot as plt


def wave_equation(num_steps: int, num_points: int, r: float) -> None:
    """
    Solves the wave equation numerically using finite difference method.

    Parameters:
    num_steps (int): Number of time steps for the simulation.
    num_points (int): Number of spatial grid points.
    r (float): Courant number

    Returns:
    None: The function visualizes the wave propagation in a 3D plot.
    """

    length = 1.0
    T = 1.0

    # Initialize the grid
    u = np.zeros((num_points, num_steps + 1))

    # Initial condition: a sine wave at t=0
    x = np.linspace(0, length, num_points)
    u[:, 0] = np.sin(np.pi * x)

    # Initial condition at t=1
    u[:, 1] = u[:, 0]

    # Time iteration
    # u{i, j+1} = 2(1-r^2)u{i,j} + r^2(u{i+1, j} + u{i-1, j}) - u{i, j-1}
    for j in range(1, num_steps):
        for i in range(1, num_points - 1):
            u[i, j + 1] = 2 * (1 - r**2) * u[i, j] + r**2 * \
                (u[i + 1, j] + u[i - 1, j]) - u[i, j - 1]

    # Visualization
    t = np.linspace(0, T, num_steps + 1)
    X, T = np.meshgrid(x, t)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u.T, cmap='viridis')
    ax.set_xlabel('Position')
    ax.set_ylabel('Time')
    ax.set_zlabel('Displacement')
    ax.set_title('Evolution of the Wave Equation in Time and Space')
    plt.show()


# Simulation parameters
num_points = 50  # Number of spatial grid points
num_steps = 500  # Number of time steps
r = 0.1  # Courant number

# Solve the wave equation
wave_equation(num_steps=num_steps, num_points=num_points, r=r)
