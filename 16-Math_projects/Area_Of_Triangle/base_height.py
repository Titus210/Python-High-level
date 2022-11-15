def base_height(b,h):
    """Calculate the height of triangle

    Args:
        b (integer): height of a right angle triangle
        h (integer): height of a right angle triangle
    
    Formulae:
        area = base * height divided by 2
    """
    
    area = (b * h) /2
    cm_unicode = "cm\u00b2"
    print(f"Area of triangle is {area:.2f}{cm_unicode}")


def main():
    """
        Promts user to enter the length of each side of triangle

    """
    height = int(input("Please Enter value of Height: "))
    base = int(input("Please Enter value of base: "))

    base_height(height, base)


main()
