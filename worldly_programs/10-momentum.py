def momentum(mass=0, velocity=0, momentum=0):
    """Calculates the momentum of an object.

    Args:
        mass (float): Mass of the object.
        velocity (float): Velocity of the object in m/s.
        momentum (float): Momentum of the object.
    """


def calculate_mass(velocity=0, momentum=0):
    """Calculates the mass of an object given momentum and velocity.

    Args:
        velocity (float): Velocity of the object in m/s. Defaults to 0.
        momentum (float): Momentum of the object. Defaults to 0.
    """
    mass = momentum / velocity
    print(f"The mass of an object is: {mass} g")


def calculate_velocity(mass=0, momentum=0):
    """Calculates the velocity of an object given momentum and mass.

    Args:
        mass (float): Mass of the object.
        momentum (float): Momentum of the object. Defaults to 0.
    """
    velocity = momentum / mass
    print(f"The velocity of an object is: {velocity} m/s")


def calculate_momentum(velocity=0, mass=0):
    """Calculates the momentum of an object given velocity and mass.

    Args:
        velocity (float): Velocity of the object in m/s.
        mass (float): Mass of the object.
    """
    momentum = velocity * mass
    print(f"The momentum of an object is: {momentum}")


def velocity_values():
    try:
        mass = float(input("Enter the mass of the object: "))
    except ValueError:
        print("Enter a valid data type")

    try:
        momentum = float(input("Enter the momentum of the object: "))
    except ValueError:
        print("Enter a valid data type")

    calculate_velocity(mass, momentum)


def mass_values():
    try:
        velocity = float(input("Enter the velocity of the object: "))
    except ValueError:
        print("Enter a valid data type")

    try:
        momentum = float(input("Enter the momentum of the object: "))
    except ValueError:
        print("Enter a valid data type")

    calculate_mass(velocity, momentum)


def momentum_values():
    try:
        mass = float(input("Enter the mass of the object: "))
    except ValueError:
        print("Enter a valid data type")

    try:
        velocity = float(input("Enter the velocity of the object: "))
    except ValueError:
        print("Enter a valid data type")

    calculate_momentum(velocity, mass)


def main():
    """Main function to execute the program."""
    print("Which operation do you want to perform?")
    print("1. Calculate velocity")
    print("2. Calculate momentum")
    print("3. Calculate mass")

    try:
        choice = int(input("Enter the operation number: "))
    except ValueError:
        print("Sorry, the input must be an integer.")

    if choice == 1:
        velocity_values()
    elif choice == 2:
        mass_values()
    elif choice == 3:
        momentum_values()
    else:
        print("Invalid choice. Please try again.")


main()
