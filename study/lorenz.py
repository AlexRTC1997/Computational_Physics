import numpy as np
import matplotlib.pyplot as plt

# Inicializar parámetros
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Condiciones iniciales
x0 = 0.0
y0 = 1.0
z0 = 1.05

# Paso de tiempo y número de iteraciones
dt = 0.01
num_steps = 10000

# Función que define el sistema de Lorenz


def lorenz(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz


# Listas para guardar los resultados
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)
# times = np.linspace(0, num_steps * dt, num_steps + 1)

# Condiciones iniciales
xs[0], ys[0], zs[0] = x0, y0, z0

# Integración numérica usando el método de Euler
for i in range(num_steps):
    dx, dy, dz = lorenz(xs[i], ys[i], zs[i], sigma, rho, beta)
    xs[i + 1] = xs[i] + dx * dt
    ys[i + 1] = ys[i] + dy * dt
    zs[i + 1] = zs[i] + dz * dt

# Graficar los resultados en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Atractor de Lorenz')

plt.show()
