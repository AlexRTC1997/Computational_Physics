import matplotlib.pyplot as plt


def rule30(current_state) -> list:
    """
    Apply Rule 30 to a 1D list of binary states manually.

    Parameters:
    current_state (list): The current state of the automaton.

    Returns:
    list: The new state after applying Rule 30.
    """
    new_state = [0] * len(current_state)
    for i in range(1, len(current_state) - 1):
        neighborhood = current_state[i-1:i+2]
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


def display_automaton(automaton) -> None:
    # Plot the automaton
    plt.figure(figsize=(10, 5))
    plt.imshow(automaton, cmap='Blues', interpolation='nearest')
    plt.title("Cellular Automaton - Rule 30")
    plt.xlabel("Cell")
    plt.ylabel("Step")
    plt.show()


def main() -> None:
    try:
        steps = int(input("> Enter the number of iterations (steps): "))
    except ValueError:
        print("> Please enter valid integers for the number of iterations.")
        return

    # Parameters
    width = 2 * steps + 1

    # Initial state
    initial_state = [0] * width
    initial_state[width // 2] = 1

    # Array to store the states
    automaton = [initial_state]

    # Generate the automaton manually
    for _ in range(steps - 1):
        new_state = rule30(automaton[-1])
        automaton.append(new_state)

    display_automaton(automaton)


if __name__ == '__main__':
    main()


# TODO: For non-quadractic matrix (30 x 10) -> 2 extra points
