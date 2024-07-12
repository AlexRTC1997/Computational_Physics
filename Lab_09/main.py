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


def generate_automaton(width, n_steps):
    # Initial state
    initial_state = [0] * width
    initial_state[width // 2] = 1

    # Array to store the states
    automaton = [initial_state]

    # Generate the automaton manually with periodic boundary conditions
    for _ in range(n_steps - 1):
        new_state = rule30_periodic(automaton[-1])
        automaton.append(new_state)

    return automaton


def main():
    # Request user input for the initial parameters
    try:
        n_steps = int(input("Enter the number of iterations (steps): "))
        width = 2 * n_steps + 1  # Automatic width for rectangular version
    except ValueError:
        print("Please enter valid integers for the number of iterations.")
        return

    # Generate rectangular automaton
    automaton_rectangular = generate_automaton(width, n_steps)

    # Generate square automaton
    automaton_square = generate_automaton(n_steps, n_steps)

    # Plot the rectangular automaton
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))

    ax[0].imshow(automaton_rectangular, cmap='binary',
                 interpolation='nearest', aspect='auto')
    ax[0].set_title(
        f"Rule 30 Cellular Automaton (Rectangular)\n{n_steps} steps, {width} width")
    ax[0].set_xlabel("Cell")
    ax[0].set_ylabel("Step")

    # Plot the square automaton
    ax[1].imshow(automaton_square, cmap='binary',
                 interpolation='nearest', aspect='auto')
    ax[1].set_title(
        f"Rule 30 Cellular Automaton (Square)\n{n_steps} steps, {n_steps} width")
    ax[1].set_xlabel("Cell")
    ax[1].set_ylabel("Step")

    plt.show()


if __name__ == "__main__":
    main()
