from  math import sqrt

def triangle_formulae(a,b,c):
    """
    Returns area of a triangle using heroes formulae.
    Args:
            a: One side of the triangle
            b: One side of the triangle
            c: One side of the triangle
    Operations:
            s: this is sum of all sides divided by 2
    Formulae:
        square root(s(s-a)*s(s-b)*s(s-c))
        
    """
    # calculating sum and s
    sum_of_sides = a + b + c
    s = sum_of_sides / 2
    
    #  find product of s an difference of al all sides
    
    difference_of_a = s - a
    difference_of_b = s - b
    difference_of_c = s - c
    
    # square root of all product of differences
    product = s * (difference_of_a * difference_of_b * difference_of_c)
    square_root = sqrt(product)
    
    print(f"Area of the triangle is {square_root:.2f}")

    
def main():
    """
        Promts user to enter the length of each side of triangle
    
    """
    a = int(input("Please Enter value of side a: "))
    b = int(input("Please Enter value of side b: "))
    c = int(input("Please Enter value of side c: "))
    
    triangle_formulae(a,b,c)

main()
    
    