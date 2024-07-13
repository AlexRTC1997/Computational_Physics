import matplotlib.pyplot as plt


def rule30(current_state: list) -> list:
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


def generate_automaton(width: int, steps: int) -> list:
    # Initial state (1 in the middle and 0 elsewhere)
    initial_state = [0] * width
    initial_state[width // 2] = 1

    # Array to store the states
    automaton = [initial_state]

    # Generate the automaton manually with periodic boundary conditions
    for _ in range(steps - 1):
        new_state = rule30(automaton[-1])
        automaton.append(new_state)

    return automaton


def plot_automaton(automaton_rectangular: list, automaton_square: list, steps: int, width: int) -> None:
    # Plot the rectangular automaton
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), )

    ax[0].imshow(automaton_rectangular, cmap='Blues')
    ax[0].set_title(
        f"Rule 30 Cellular Automaton (Rectangular)\n{steps} steps, {width} width")
    ax[0].set_xlabel("Cell")
    ax[0].set_ylabel("Step")

    # Plot the square automaton
    ax[1].imshow(automaton_square, cmap='Blues', aspect='auto')
    ax[1].set_title(
        f"Rule 30 Cellular Automaton (Square)\n{steps} steps, {steps} width")
    ax[1].set_xlabel("Cell")
    ax[1].set_ylabel("Step")

    plt.show()


def main() -> None:
    # Request user input for the initial parameters
    try:
        steps = int(input("\n> Enter the number of iterations: "))
        width = 2 * steps + 1  # Automatic width for rectangular version
    except ValueError:
        print("Please enter valid integers for the number of iterations.")
        return

    print("\n> Generating automaton...\n")
    # Generate rectangular and square automatons
    automaton_rectangular = generate_automaton(width, steps)
    automaton_square = generate_automaton(steps, steps)

    # Plot automatons
    plot_automaton(automaton_rectangular, automaton_square, steps, width)
    print("> Program finished...\n")


if __name__ == "__main__":
    main()
