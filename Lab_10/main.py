import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Chua's circuit parameters
alpha = 9.0
beta = 15.0
m0 = -8.0/3.0
m1 = -5.0/7.0


def chua_nonlinear(x):
    # Nonlinear function for Chua's circuit
    return m1 * x + 0.5 * (m0 - m1) * (np.abs(x + 1) - np.abs(x - 1))


def chua_deriv(t, state):
    # Chua's circuit differential equations
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

# Define the Poincare section plane in x = 0
poincare_section = []
for i in range(1, len(x) - 1):
    if (x[i-1] < 0 and x[i] > 0):
        poincare_section.append((y[i], z[i]))

# Plotting the results
fig = plt.figure(figsize=(18, 8))

# Plot the Chua's circuit attractor in 3D with the plane
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(x, y, z, lw=0.5)
ax1.set_title("Chua's Circuit Attractor")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

# Add the plane x = 0 for visualization
yy, zz = np.meshgrid(np.linspace(min(y), max(y), 100),
                     np.linspace(min(z), max(z), 100))
xx = np.zeros_like(yy)
ax1.plot_surface(xx, yy, zz, alpha=0.3, color='green', edgecolor='none')

# Plot the Poincaré section in the plane x = 0
ax2 = fig.add_subplot(122)
poincare_y, poincare_z = zip(*poincare_section)
ax2.scatter(poincare_y, poincare_z, s=0.5, color='blue')
ax2.set_title("Poincaré Section of Chua's Circuit (x = 0)")
ax2.set_xlabel("y")
ax2.set_ylabel("z")
ax2.grid(True)

plt.tight_layout()
plt.show()
