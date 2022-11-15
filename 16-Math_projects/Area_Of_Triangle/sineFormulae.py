from math import sin
 
def sin_formulae(angle, c,b):
    """Calculate area using sine formulae

    Args:
        angle (integer): abgle of one side which is equivalent to sin(angle) = height/ hypotenuse
        c (integer): One side of triangle which is equivalent to height = c * sin angle
        b (integer): base of the triangle
       
    """
    product_of_side = c * b * sin(angle)
    area_of_triangle = product_of_side / 2
    
    print(f"Area of triangle is {area_of_triangle:.2f}")


def main():
    """
        Promts user to enter the length of each side of triangle
    
    """
    angle = int(input("Please Enter value of angle: "))
    b = int(input("Please Enter value of side b: "))
    c = int(input("Please Enter value of side c: "))

    sin_formulae(angle, c, b)


main()
