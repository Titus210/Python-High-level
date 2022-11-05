"""Compute money for rented Cars """
import math
def count_money():
        countData = []
        # Read data in transActions.txt
        with open("../transActions.txt","r", encoding="utf-8") as f:
            for col in f:
                amount = float(col.split(",")[-1].strip())
                countData += [amount]
        # Sum last column 
        list_item  = list(map(float,countData))
        total = (math.fsum(list_item))

        print(f"The total amount of money is {total} euros")
