import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros
L = 10.0        # Longitud del dominio espacial
T = 10.0        # Tiempo total de simulación
c = 1.0         # Velocidad de la onda
dx = 0.1        # Paso espacial
dt = 0.01       # Paso de tiempo
nx = int(L / dx) + 1  # Número de puntos en el espacio
nt = int(T / dt) + 1  # Número de puntos en el tiempo
r = c * dt / dx  # Número de Courant

# Verificación de la condición de estabilidad
if r > 1:
    raise ValueError(
        "El número de Courant r debe ser <= 1 para la estabilidad.")

# Inicialización de las matrices de solución
u = np.zeros((nx, nt))

# Condiciones iniciales
# Ejemplo: una onda senoidal inicial
x = np.linspace(0, L, nx)
u[:, 0] = np.sin(np.pi * x / L)
# u[:, 1] = u[:, 0]  # Para una inicialización simple (puedes modificar esto para condiciones más realistas)

# Cálculo del siguiente paso en el tiempo (usualmente con una fórmula específica o una condición de contorno inicial)
for i in range(1, nx-1):
    u[i, 1] = u[i, 0] + 0.5 * r**2 * (u[i+1, 0] - 2 * u[i, 0] + u[i-1, 0])

# Iteración en el tiempo
for j in range(1, nt-1):
    for i in range(1, nx-1):
        u[i, j+1] = 2 * (1 - r**2) * u[i, j] + r**2 * \
            (u[i+1, j] + u[i-1, j]) - u[i, j-1]

# Crear la malla para la visualización 3D
X, T = np.meshgrid(np.linspace(0, L, nx), np.linspace(0, T, nt))

# Transponer la matriz u para que coincida con las dimensiones de X y T
U = u.T

# Visualización de la solución en 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, U, cmap='viridis')

ax.set_xlabel('Posición espacial (x)')
ax.set_ylabel('Tiempo (t)')
ax.set_zlabel('Desplazamiento (u)')
ax.set_title('Evolución de la Ecuación de Onda en el Tiempo y el Espacio')

plt.show()
