

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
            # Δx = ViΔt + (αΔt^2)/2
            # Plus Graph
            print('Running option 2')

            # Vf = ViΔt + αΔt
        elif option == 3:
            print('\n> Program finished...\n')
