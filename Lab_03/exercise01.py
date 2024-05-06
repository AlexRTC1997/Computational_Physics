import matplotlib.pyplot as plt

k = 9 * 10 ^ 9


def electric_force(q1, q2, r):
    electric_force = k * q1 * q2 / r ** 2
    return electric_force


def electric_field(Q, r):
    electric_field = k * Q / r ** 2
    return electric_field


def show_force_graph(q1, q2, r):
    # Add units N / m^2
    distances = range(1, int(r) + 1)
    forces = [electric_force(q1, q2, d) for d in distances]

    plt.plot(distances, forces)
    plt.title('Electric force graph')
    plt.xlabel('Distance (m^2)')
    plt.ylabel('Force (N)')
    plt.grid(True)
    plt.show()


def show_field_graph(Q, r):
    distances = range(1, int(r) + 1)
    fields = [electric_field(Q, d) for d in distances]

    plt.plot(distances, fields)
    plt.title('Electric field graph')
    plt.xlabel('Distance (m^2)')
    plt.ylabel('Field (V)')
    plt.grid(True)
    plt.show()


option = None

while option != 3:
    option = int(input('[1] F [2] E [3] Exit: '))

    if option == 1:
        q1 = float(input('q1: '))
        q2 = float(input('q2: '))
        r = float(input('r: '))

        force = electric_force(q1, q2, r)
        print(f'\n[Result]: \n> Force: {force}N\n')

        show_force_graph(q1, q2, r)
    elif option == 2:
        Q = float(input('Q: '))
        r = float(input('r: '))

        field = electric_field(Q, r)
        print(f'\n[Result]: \n> Field: {field}V\n')

        show_field_graph(Q, r)
    elif option == 3:
        print('\n> Program finished...\n')
