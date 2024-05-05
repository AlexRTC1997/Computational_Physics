import matplotlib.pyplot as plt

if __name__ == '__main__':
    option = None

    while option != 3:
        option = int(input('[1] MRU [2] MRUV [3] Exit: '))

        if option == 1:
            mru_option = None

            while mru_option != 4:
                mru_option = int(input('\n\t[1] Δx [2] V [3] Δt [4] Back: '))
                print()

                if mru_option == 1:
                    V = float(input('\t> V: '))
                    Δt = float(input('\t> Δt: '))

                    print('\t> Δx = V x Δt')
                    print(f'\t  Δx = {V} x {Δt}')
                    print(f'\t  Δx = {V * Δt}m')
                elif mru_option == 2:
                    print('\tNote: V != 0')
                    Δx = float(input('\t> Δx: '))
                    V = float(input('\t> V: '))

                    while V == 0:
                        V = float(input('\tV: '))

                    print('\t> Δt = Δx / V')
                    print(f'\t  Δt = {Δx} / {V}')
                    print(f'\t  Δt = {Δx / V}s')
                elif mru_option == 3:
                    print('\tNote: Δt != 0')
                    Δx = float(input('\t> Δx: '))
                    Δt = float(input('\t> Δt: '))

                    while Δt == 0:
                        Δt = float(input('\tΔt: '))

                    print('\t> V = Δx / Δt')
                    print(f'\t  V = {Δx} / {Δt}')
                    print(f'\t  V = {Δx / Δt}m/s')
                elif mru_option == 4:
                    break

        elif option == 2:
            mruv_option = None

            while mruv_option != 3:
                mruv_option = int(input('\n\t[1] Δx [2] Vf [3] Back: '))
                print()

                if mruv_option == 1:
                    Vi = float(input('\t> Vi: '))
                    Δt = float(input('\t> Δt: '))
                    α = float(input('\t> α: '))

                    print('\t> Δx = ViΔt + (αΔt^2)/2')
                    print(f'\t  Δx = {Vi} x {Δt} + ({α} x {Δt}^2)/2')
                    print(f'\t  Δx = {Vi * Δt + (α * Δt ** 2)/2}m')

                    # Chart
                    time_interval = range(int(Δt) + 1)
                    distances = [(Vi * time + (α * time ** 2)/2)
                                 for time in time_interval]

                    plt.plot(time_interval, distances)
                    plt.title('MRUV Chart')
                    plt.xlabel('Time (s)')
                    plt.ylabel('Distance (m)')
                    plt.grid(True)
                    plt.show()

                elif mruv_option == 2:
                    Vi = float(input('\t> Vi: '))
                    Δt = float(input('\t> Δt: '))
                    α = float(input('\t> α: '))

                    print('\t> Vf = Vi + αΔt')
                    print(f'\t  Vf = {Vi} + {α} x {Δt}')
                    print(f'\t  Vf = {Vi + α * Δt}m/s')
                elif mruv_option == 3:
                    break

        elif option == 3:
            print('\n> Program finished...\n')
