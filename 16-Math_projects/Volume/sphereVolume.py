import math


def volumeOfSphere(r):
    """Calculates the volume of  a sphere 

    Args:
        r(integer): The radius of the sphere

    Basic formulae
        volume = 4/3*pi* r*r*r
    """

    x = 4/3    # the integer part of the formulae
    pi = math.pi  # getting the pi from math module
    cubicRadius = r * r * r

    volume = x * pi * cubicRadius

    return volume


def main():
    try:
        radius = int(input("Enter the radius of sphere: "))
        cm_unicode = "cm\u00b3"
        print(
            f"The volume of the sphere is {volumeOfSphere(radius):.2f}{cm_unicode}")
    except ValueError:
        print("Please enter a valid integer")
        main()


main()
