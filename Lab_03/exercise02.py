import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def E(q: float, r0: float, x: float, y: float) -> float:
    """
    Return the electric field vector E=(Ex,Ey) due to charge q at r0.

    Parameters:
    q (float): The charge in Coulombs.
    r0 (float): The position of the charge.
    x (float): The x-coordinate of the point where the electric field is calculated.
    y (float): The y-coordinate of the point where the electric field is calculated.

    Returns:
    float: The components of the electric field vector E=(Ex, Ey).
    """
    den = np.hypot(x - r0[0], y - r0[1]) ** 3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den


def main():
    """
    The main function that runs the program.
    """
    while True:
        # Grid of x and y points
        nx, ny = 64, 64
        x = np.linspace(-2, 2, nx)
        y = np.linspace(-2, 2, ny)
        X, Y = np.meshgrid(x, y)

        # Menu to choose the charge configuration
        print('\n[1]. Different charges (positive and negative)')
        print('[2]. Two positive charges')
        print('[3]. Two negative charges')
        print('[4]. Exit')
        selected_option = input('> Select option: ')
        print()

        # Check if the selected option is to exit
        if selected_option == "4":
            print('> Program finished...\n')
            break

        # Configuration of charges based on user choice
        if selected_option == '1':
            charges = [(-1, (-1, 0)), (1, (1, 0))]
        elif selected_option == '2':
            charges = [(1, (-1, 0)), (1, (1, 0))]
        elif selected_option == '3':
            charges = [(-1, (-1, 0)), (-1, (1, 0))]
        else:
            print('> Invalid option. Please choose a valid option.\n')
            continue

        # Electric field vector, E=(Ex, Ey), as separate components
        Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
        for charge in charges:
            ex, ey = E(*charge, x=X, y=Y)
            Ex += ex
            Ey += ey

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Plot the streamlines with an appropriate colormap and arrow style
        color = 2 * np.log(np.hypot(Ex, Ey))
        ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
                      density=2, arrowstyle='->', arrowsize=1.5)

        # Add filled circles for the charges themselves
        charge_colors = {True: '#aa0000', False: '#0000aa'}
        for q, pos in charges:
            ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0]))

        # Chart settings
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        plt.show()


# Run the program
main()
