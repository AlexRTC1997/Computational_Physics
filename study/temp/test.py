import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Chua's circuit parameters
alpha = 9.0
beta = 15.0
m0 = -8.0/3.0
m1 = -5.0/7.0

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
t_span = (0, 300)
t_eval = np.linspace(t_span[0], t_span[1], 100000)

# Solve the differential equations
solution = solve_ivp(chua_deriv, t_span, initial_state,
                     t_eval=t_eval, rtol=1e-10, atol=1e-10)

# Extract the solutions
x = solution.y[0]
y = solution.y[1]
z = solution.y[2]

# Define the Poincare section plane (e.g., y = 0)
poincare_section = []
for i in range(1, len(y) - 1):
    if (y[i-1] < 0 and y[i] > 0):
        poincare_section.append((x[i], z[i]))

# Plotting the results
fig = plt.figure(figsize=(18, 8))

# Plot the Chua's circuit attractor in 3D with the plane
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(x, y, z, lw=0.5)
ax1.set_title("Chua's Circuit Attractor")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

# Add the plane y = 0 for visualization
xx, zz = np.meshgrid(np.linspace(min(x), max(x), 100),
                     np.linspace(min(z), max(z), 100))
yy = np.zeros_like(xx)
ax1.plot_surface(xx, yy, zz, alpha=0.3, color='red', edgecolor='none')

# Plot the Poincaré section in the plane y = 0
ax2 = fig.add_subplot(122)
poincare_x, poincare_z = zip(*poincare_section)
ax2.scatter(poincare_x, poincare_z, s=0.5, color='blue')
ax2.set_title("Poincaré Section of Chua's Circuit (y = 0)")
ax2.set_xlabel("x")
ax2.set_ylabel("z")
ax2.grid(True)

plt.tight_layout()
plt.show()
