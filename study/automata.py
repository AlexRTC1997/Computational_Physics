import numpy as np
import matplotlib.pyplot as plt

# Parámetros del autómata
num_generations = 10   # Número de generaciones
num_cells = 2 * num_generations + 1  # Ancho de la matriz para espacio suficiente
initial_index = num_cells // 2  # Índice de la celda inicial activa

# Inicializar el estado del autómata
cells = np.zeros((num_generations, num_cells), dtype=int)
# Activar la celda central en la primera generación
cells[0, initial_index] = 1

# Función para aplicar la Regla 30 explícitamente


def apply_rule30(left, center, right):
    if (left == 0 and center == 0 and right == 0):
        return 0
    elif (left == 0 and center == 0 and right == 1):
        return 1
    elif (left == 0 and center == 1 and right == 0):
        return 1
    elif (left == 0 and center == 1 and right == 1):
        return 0
    elif (left == 1 and center == 0 and right == 0):
        return 1
    elif (left == 1 and center == 0 and right == 1):
        return 0
    elif (left == 1 and center == 1 and right == 0):
        return 0
    elif (left == 1 and center == 1 and right == 1):
        return 1


# Evolución del autómata
for i in range(1, num_generations):
    for j in range(num_cells):
        # Condición de frontera periódica
        left = cells[i - 1, (j - 1) % num_cells]
        center = cells[i - 1, j]
        # Condición de frontera periódica
        right = cells[i - 1, (j + 1) % num_cells]
        cells[i, j] = apply_rule30(left, center, right)

# Visualización del autómata celular
plt.figure(figsize=(12, 6))
plt.imshow(cells, cmap='binary', interpolation='nearest')
plt.title('Autómata Celular: Regla 30')
plt.xlabel('Celdas')
plt.ylabel('Generaciones')
plt.show()
