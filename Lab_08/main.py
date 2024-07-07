import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# (1) Define the Lorenz attractor equations


def lorenz(t: float, X: list, sigma: float, beta: float, rho: float) -> list:
    """
    Defines the Lorenz attractor differential equations.

    Parameters:
    t (float): Time variable.
    X (list or array): List or array containing the current values of x, y, and z.
    sigma (float): Parameter sigma in the Lorenz system.
    beta (float): Parameter beta in the Lorenz system.
    rho (float): Parameter rho in the Lorenz system.

    Returns:
    list: List containing the derivatives [dx/dt, dy/dt, dz/dt].
    """

    x, y, z = X
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# (2) Parameters of the Lorenz system
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# (3) Initial conditions
X0 = [1.0, 1.0, 1.0]

# [4] Time span for the integration
t_span = (0, 40)
t_eval = np.linspace(0, 40, 10000)

# (5) Solve the Lorenz system
sol = solve_ivp(lorenz, t_span, X0, args=(sigma, beta, rho), t_eval=t_eval)

# (6) Extract the solutions
x = sol.y[0]
y = sol.y[1]
z = sol.y[2]

# (7) Plot the Lorenz attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='m', lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Attractor")
plt.show()
