#!/usr/bin/python3
"""Check if meal is blacklisted."""
def main(meals,blacklist):
    """Iterates and check if meal entered is allowed.
        Parameters:
                blacklist: Meals not allowed
    """

    for food in meals.split():
        if food in blacklist:
            print(f"{food} is not allowed")
            break
        else:
            print(f"{food}  is allowed")

def input_meal():
    """User enter food he/she wants to carry
        Returns:Food entered
    """
    food = input("Please enter food you want to carry: ").lower()

    blacklisted = ["cocacola","biscuits","cakes","pizza","birihani","yourght","bacon","fried chicken"]
    main(food, blacklisted)
input_meal()
