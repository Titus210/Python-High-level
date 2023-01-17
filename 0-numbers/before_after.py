#/usr/bin/python3

def before_after_dot(digit, before, after):
    """
        Args:
            digit(float): Float number
            before(integer): Integer number before float
            after(integer): Integer number after float
        Return:
            Float consisting of  before variable before decimal point
            after variable after decimal point
    """
    s= str(digit)
    i = s.index(".")
    return s[i-before:i+after+1]

def main():
    try:
        before = int(input("Please enter a digit before: "))
    except ValueError:
        print("Enter an integer number")
        main()
    try:
        after = int(input("Please enter a after digit: "))
    except ValueError:
        print("Enter Valid integer")
        main()
    try:
        digit = float(input("Please Enter a floating point"))
    except ValueError:
        print("Enter a valid decimal number")
        main()
    print(f"The decimal digit is {before_after_dot(digit,before,after)}")

main()
