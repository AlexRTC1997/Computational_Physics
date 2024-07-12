import matplotlib.pyplot as plt


def rule30_periodic(current_state):
    """
    Apply Rule 30 to a 1D list of binary states with periodic boundary conditions.

    Parameters:
    current_state (list): The current state of the automaton.

    Returns:
    list: The new state after applying Rule 30.
    """
    new_state = [0] * len(current_state)
    for i in range(len(current_state)):
        left = current_state[i-1] if i > 0 else current_state[-1]
        center = current_state[i]
        right = current_state[i +
                              1] if i < len(current_state) - 1 else current_state[0]
        neighborhood = [left, center, right]

        if neighborhood == [1, 1, 1]:
            new_state[i] = 0
        elif neighborhood == [1, 1, 0]:
            new_state[i] = 0
        elif neighborhood == [1, 0, 1]:
            new_state[i] = 0
        elif neighborhood == [1, 0, 0]:
            new_state[i] = 1
        elif neighborhood == [0, 1, 1]:
            new_state[i] = 1
        elif neighborhood == [0, 1, 0]:
            new_state[i] = 1
        elif neighborhood == [0, 0, 1]:
            new_state[i] = 1
        else:
            new_state[i] = 0
    return new_state


def main():
    # Solicitar al usuario los parámetros iniciales
    try:
        n_steps = int(input("Enter the number of iterations (steps): "))
        width = n_steps  # Para una matriz cuadrada
    except ValueError:
        print("Please enter valid integers for the number of iterations.")
        return

    # Estado inicial
    initial_state = [0] * width
    initial_state[width // 2] = 1

    # Array para almacenar los estados
    automaton = [initial_state]

    # Generar el autómata manualmente con condiciones periódicas de contorno
    for _ in range(n_steps - 1):
        new_state = rule30_periodic(automaton[-1])
        automaton.append(new_state)

    # Graficar el autómata
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(automaton, cmap='binary', interpolation='nearest', aspect='auto')
    ax.set_title(
        f"Rule 30 Cellular Automaton with Periodic Boundary Conditions\n({n_steps} steps, {width} width)")
    ax.set_xlabel("Cell")
    ax.set_ylabel("Step")
    plt.show()


if __name__ == "__main__":
    main()
