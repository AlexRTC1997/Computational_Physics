

if __name__ == '__main__':
    option = None

    while option != 3:
        option = int(input('[1]MRU [2]MRUV [3]Exit: '))
        if option == 1:
            mru_option = None

            while mru_option != 4:
                mru_option = int(input('[1]Δx [2]Vx [3]Δt [4]Back: '))
                if mru_option == 1:
                    # Δx = VxΔt
                    Vx = float(input('Vx: '))
                    Δt = float(input('Δt: '))
                    Δx = Vx * Δt
                    print(f'Δx = {Δx}')
                elif mru_option == 2:
                    # Δt = Δx / Vx
                    Δx = float(input('Δx: '))
                    Vx = float(input('Vx: '))
                    while Vx == 0:
                        Vx = float(input('Vx: '))
                    Δt = Δx / Vx
                    print(f'Δt = {Δt}')
                elif mru_option == 3:
                    # Vx = Δx / Δt
                    Δx = float(input('Δx: '))
                    Δt = float(input('Δt: '))
                    while Δt == 0:
                        Δt = float(input('Δt: '))
                    Vx = Δx / Δt
                    print(f'Vx = {Vx}')
                elif mru_option == 4:
                    break

        elif option == 2:
            # Δx = ViΔt + (αΔt^2)/2
            # Plus Graph
            print('Running option 2')

        elif option == 3:
            # Vf = ViΔt + αΔt
            print('Exiting program')
