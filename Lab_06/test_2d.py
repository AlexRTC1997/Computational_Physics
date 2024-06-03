import numpy as np
import matplotlib.pyplot as plt

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

# Visualización de la solución en varios instantes de tiempo
plt.figure(figsize=(10, 6))
for j in range(0, nt, nt // 10):
    plt.plot(x, u[:, j], label=f't={j*dt:.2f}')
plt.xlabel('x')
plt.ylabel('u')
plt.title('Solución de la Ecuación de Onda')
plt.legend()
plt.show()
