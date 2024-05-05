

if __name__ == '__main__':
    option = None

    while option != 3:
        option = int(input('[1] MRU [2] MRUV [3] Exit: '))
        if option == 1:
            mru_option = None

            while mru_option != 4:
                mru_option = int(input('\n[1] Δx [2] V [3] Δt [4] Back: '))
                print()
                if mru_option == 1:
                    V = float(input('> V: '))
                    Δt = float(input('> Δt: '))

                    print('> Δx = V x Δt')
                    print(f'  Δx = {V} x {Δt}')
                    print(f'  Δx = {V * Δt}')
                elif mru_option == 2:
                    print('Note: V != 0')
                    Δx = float(input('> Δx: '))
                    V = float(input('> V: '))

                    while V == 0:
                        V = float(input('V: '))

                    print('> Δt = Δx / V')
                    print(f'  Δt = {Δx} / {V}')
                    print(f'  Δt = {Δx / V}')
                elif mru_option == 3:
                    print('Note: Δt != 0')
                    Δx = float(input('> Δx: '))
                    Δt = float(input('> Δt: '))

                    while Δt == 0:
                        Δt = float(input('Δt: '))

                    print('> V = Δx / Δt')
                    print(f'  V = {Δx} / {Δt}')
                    print(f'  V = {Δx / Δt}')
                elif mru_option == 4:
                    break

        elif option == 2:
            # Δx = ViΔt + (αΔt^2)/2
            # Plus Graph
            print('Running option 2')

            # Vf = ViΔt + αΔt
        elif option == 3:
            print('\n> Program finished...\n')
