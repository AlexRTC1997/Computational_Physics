# Realizar un código que permita observar el comportamiento de fuerza
# eléctrica y el campo eléctrico en función del inverso cuadrado de
# la distancia

k = 9 * 10 ^ 9


def electric_force(q1, q2, r):
    electric_force = k * q1 * q2 / r ** 2
    return electric_force


def electric_field(Q, r):
    electric_field = k * Q / r ** 2
    return electric_field


option = None

while option != 3:
    option = int(input('[1] F [2] E [3] Exit: '))

    if option == 1:
        q1 = float(input('q1: '))
        q2 = float(input('q2: '))
        r = float(input('r: '))

        force = electric_force(q1, q2, r)
        print(f'\n[Result]: \n> Force: {force}N\n')

    elif option == 2:
        Q = float(input('Q: '))
        r = float(input('r: '))

        field = electric_field(Q, r)
        print(f'\n[Result]: \n> Field: {field}V\n')
    elif option == 3:
        print('\n> Program finished...\n')
