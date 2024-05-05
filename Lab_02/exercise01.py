print('[Atwood Machine]')
print()

gravity = 9.8

acceleration = None
tension = None

option = None

while option != 2:
    option = int(input('[1] Atwood [2] Exit: '))

    if option == 1:
        mass1 = float(input('> Mass 1: '))
        mass2 = float(input('> Mass 2: '))
        print()

        if mass1 == mass2:
            acceleration = 0
            tension = mass1 * gravity

            print('[Case 1: Equal masses]')
            print(f'> Acceleration: {acceleration}m/s2')
            print(f'> Tension: {tension}N')
        elif mass1 > mass2:
            acceleration = gravity * (mass1 - mass2) / (mass1 + mass2)
            tension = mass1 * gravity - mass1 * acceleration

            print('[Case 2: mass1 > mass2]')
            print(f'> Acceleration: {acceleration}m/s2')
            print(f'> Tension: {tension}N')
        elif mass2 > mass1:
            acceleration = gravity * (mass2 - mass1) / (mass1 + mass2)
            tension = mass1 * acceleration + mass1 * gravity

            print('[Case 3: mass2 > mass1]')
            print(f'> Acceleration: {acceleration}m/s2')
            print(f'> Tension: {tension}N')

        print()
    elif option == 2:
        print('> Program finished...\n')
