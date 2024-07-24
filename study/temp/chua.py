import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Chua's circuit parameters
alpha = 9.0
beta = 14.286
m0 = -1.143
m1 = -0.714

# Nonlinear function for Chua's circuit


def chua_nonlinear(x):
    return m1 * x + 0.5 * (m0 - m1) * (np.abs(x + 1) - np.abs(x - 1))

# Chua's circuit differential equations


def chua_deriv(t, state):
    x, y, z = state
    dxdt = alpha * (y - x - chua_nonlinear(x))
    dydt = x - y + z
    dzdt = -beta * y
    return [dxdt, dydt, dzdt]


# Initial conditions
initial_state = [0.1, 0.0, 0.0]

# Time span for the simulation
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the differential equations
solution = solve_ivp(chua_deriv, t_span, initial_state,
                     t_eval=t_eval, rtol=1e-10, atol=1e-10)

# Extract the solutions
x = solution.y[0]
y = solution.y[1]
z = solution.y[2]

# Plot the results
fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_title("Chua's Circuit Attractor")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
