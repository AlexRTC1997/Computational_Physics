import matplotlib.pyplot as plt

# Constant (Nm^2/C^2)
k = 9 * 10 ^ 9


def electric_force(q1: float, q2: float, r: float) -> float:
    """
    Calculate the electric force between two charges based on Coulomb's law.

    Parameters:
    q1 (float): The value of the first charge in Coulombs.
    q2 (float): The value of the second charge in Coulombs.
    r (float): The distance between the charges in meters.

    Returns:
    float: The electric force between the charges in Newtons.
    """
    electric_force = k * q1 * q2 / r ** 2
    return electric_force


def electric_field(Q: float, r: float) -> float:
    """
    Calculate the electric field based on the input values.

    Parameters:
    Q (float): The charge in Coulombs.
    r (float): The distance in meters.

    Returns:
    float: The electric field value in Newtons/Coulombs.
    """
    electric_field = k * Q / r ** 2
    return electric_field


def show_force_graph(q1: float, q2: float, r: float) -> None:
    """
    Display a graph of the electric force between two charges based on the input charges and distance.

    Parameters:
    q1 (float): The value of the first charge in Coulombs.
    q2 (float): The value of the second charge in Coulombs.
    r (float): The distance between the charges in meters.

    Returns: 
    None
    """
    distances = range(1, int(r) + 1)
    forces = [electric_force(q1, q2, d) for d in distances]

    plt.plot(distances, forces)
    plt.title('Electric force graph')
    plt.xlabel('Distance (m^2)')
    plt.ylabel('Force (N)')
    plt.grid(True)
    plt.show()


def show_field_graph(Q: float, r: float) -> None:
    """
    Display a graph of the electric field based on the input charge and distance.

    Parameters:
    Q (float): The charge in Coulombs.
    r (float): The distance in meters.

    Returns:
    None
    """
    distances = range(1, int(r) + 1)
    fields = [electric_field(Q, d) for d in distances]

    plt.plot(distances, fields)
    plt.title('Electric field graph')
    plt.xlabel('Distance (m^2)')
    plt.ylabel('Field (N/C)')
    plt.grid(True)
    plt.show()


def main():
    """
    A function that serves as the main control loop for the program, allowing the user to choose between different options.
    """

    option = None

    while option != 3:
        option = int(input('[1] F [2] E [3] Exit: '))

        if option == 1:
            q1 = float(input('q1: '))
            q2 = float(input('q2: '))
            r = abs(float(input('r: ')))

            force = electric_force(q1, q2, r)
            print(f'\n[Result]: \n> Force: {force}N\n')

            show_force_graph(q1, q2, r)
        elif option == 2:
            Q = float(input('Q: '))
            r = abs(float(input('r: ')))

            field = electric_field(Q, r)
            print(f'\n[Result]: \n> Field: {field}N/C\n')

            show_field_graph(Q, r)
        elif option == 3:
            print('\n> Program finished...\n')


# Run main function
main()
