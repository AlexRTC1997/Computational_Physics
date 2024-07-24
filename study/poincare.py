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
num_steps = 100000

# Superficie de sección de Poincaré
z_section = 28.0

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

# Lista para guardar los puntos de la sección de Poincaré
poincare_points = []

# Condiciones iniciales
xs[0], ys[0], zs[0] = x0, y0, z0

# Integración numérica usando el método de Euler
for i in range(num_steps):
    dx, dy, dz = lorenz(xs[i], ys[i], zs[i], sigma, rho, beta)
    xs[i + 1] = xs[i] + dx * dt
    ys[i + 1] = ys[i] + dy * dt
    zs[i + 1] = zs[i] + dz * dt

    # Verificar si se cruza la superficie z = z_section
    if zs[i] < z_section and zs[i + 1] >= z_section:
        poincare_points.append((xs[i], ys[i]))


print(poincare_points)

# Convertir la lista de puntos a un array de NumPy si no está vacío
if poincare_points:
    poincare_points = np.array(poincare_points)

    # Graficar los resultados de la sección de Poincaré
    plt.figure(figsize=(8, 6))
    plt.scatter(poincare_points[:, 0],
                poincare_points[:, 1], s=1, color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sección de Poincaré del Sistema de Lorenz')
    plt.grid(True)
    plt.show()
else:
    print("No se encontraron intersecciones con la superficie de sección z = 0.0")
