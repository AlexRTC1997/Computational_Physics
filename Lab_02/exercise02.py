# 2. Un móvil de masa m recorre una distancia "d" en un tiempo "t", al inicio
# tiene una velocidad inicial "Vi" y una velocidad final "Vf". Escriba un código
# que determine la fuerza que describe el móvil al momento de realizar
# el cambio de velocidad y grafique el proceso
import matplotlib.pyplot as plt

option = None

while option != 2:
    option = int(input('[1] F [2] Exit: '))

    if option == 1:
        mass = float(input('> Mass: '))
        time = float(input('> Time: '))
        initial_speed = float(input('> Initial speed: '))
        final_speed = float(input('> Final speed: '))

        acceleration = (final_speed - initial_speed) / time
        force = mass * acceleration

        # Output
        print('\n[Result]: \n')
        print(f'> Force: {force}N')

        # Graph
        times = range(int(time) + 1)
        speeds = [(initial_speed + (final_speed - initial_speed) * t / time)
                  for t in times]

        plt.plot(times, speeds)
        plt.title('Speed change graph')
        plt.xlabel('Time (s)')
        plt.ylabel('Speed (m/s)')
        plt.grid(True)
        plt.show()

    elif option == 2:
        print('> Program finished...\n')
