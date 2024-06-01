from gmes import *


class MaxwellSolver:
    def __init__(self, size, resolution):
        self.size = size
        self.resolution = resolution
        self.space = None
        self.geom_list = []
        self.src_list = []
        self.fdtd = None

    def set_space(self):
        self.space = Cartesian(size=self.size, resolution=self.resolution)

    def add_geometry(self, geometry):
        self.geom_list.append(geometry)

    def add_source(self, source):
        self.src_list.append(source)

    def init_fdtd(self):
        if self.space is None:
            print("Error: Space not set. Call set_space() method first.")
            return
        self.fdtd = TMzFDTD(self.space, self.geom_list, self.src_list)
        self.fdtd.init()

    def run_simulation(self, steps):
        if self.fdtd is None:
            print("Error: FDTD not initialized. Call init_fdtd() method first.")
            return
        self.fdtd.step_until_t(steps)

    def show_field(self, field, component, plane):
        if self.fdtd is None:
            print("Error: FDTD not initialized. Call init_fdtd() method first.")
            return
        self.fdtd.show_field(field, component, plane)


def run_example(example_number):
    if example_number == 1:
        solver = MaxwellSolver(size=(5, 5, 0), resolution=10)
        solver.set_space()
        solver.add_geometry(DefaultMedium(material=Dielectric()))
        solver.add_geometry(Shell(material=Cpml(), thickness=0.5))
        solver.add_source(PointSource(src_time=Continuous(
            freq=0.8), center=(0, 0, 0), component=Ez))
        solver.init_fdtd()
        solver.run_simulation(steps=50)
        solver.show_field(Ez, Z, 0)
    elif example_number == 2:
        solver = MaxwellSolver(size=(10, 10, 0), resolution=20)
        solver.set_space()
        solver.add_geometry(DefaultMedium(material=Dielectric()))
        solver.add_geometry(Cylinder(material=Dielectric(
            3), center=(0, 0, 0), radius=0.5, axis=(0, 0, 1)))
        solver.add_geometry(Shell(material=Cpml(), thickness=0.5))
        solver.add_source(PointSource(src_time=Continuous(
            freq=0.5), center=(-2, 0, 0), component=Ez))
        solver.init_fdtd()
        solver.run_simulation(steps=75)
        solver.show_field(Ez, Z, 0)
    elif example_number == 3:
        solver = MaxwellSolver(size=(10, 10, 0), resolution=20)
        solver.set_space()
        solver.add_geometry(DefaultMedium(material=Dielectric()))
        solver.add_geometry(Block(material=Dielectric(12), size=(5, 0.5, inf)))
        solver.add_geometry(Shell(material=Cpml(), thickness=0.5))
        solver.add_source(PointSource(src_time=Continuous(
            freq=0.15), center=(-3, 0, 0), component=Ez))
        solver.init_fdtd()
        solver.run_simulation(steps=100)
        solver.show_field(Ez, Z, 0)


def main_menu():
    while True:
        print("\n[GMES Simulation]\n")
        print("1. Simulation 1: Simple dielectric medium with CPML shell")
        print("2. Simulation 2: Dielectric cylinder scatterer")
        print("3. Simulation 3: Dielectric slab waveguide")
        print("4. Exit\n")

        choice = raw_input(" > Enter your choice (1-4): ")

        if choice == '1':
            run_example(1)
        elif choice == '2':
            run_example(2)
        elif choice == '3':
            run_example(3)
        elif choice == '4':
            print(" \n> Program finished...\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()
