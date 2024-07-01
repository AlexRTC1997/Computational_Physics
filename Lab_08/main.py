import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the Lorenz attractor equations


def lorenz(X, t, sigma, beta, rho):
    x, y, z = X
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# Set parameters
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# Initial conditions
X0 = [1.0, 1.0, 1.0]

# Time points where solution is computed
t = np.linspace(0, 40, 10000)

# Solve ODE
solution = odeint(lorenz, X0, t, args=(sigma, beta, rho))

# Plot results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution[:, 0], solution[:, 1], solution[:, 2])
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()


# TIF - 2 points | Report and Slides with Latex
# Inital conditions 28, 10000, 10
