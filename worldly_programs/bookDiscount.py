# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# user input copies?

def bookPrice(copies):
    """Calculates the price of wholesale copies for an entered number of copies

    Args:
        copies (_integer_): _description_
    """
    coverPrice = 24.95
    discount = 40/100  # discount in percentage

    # price per copy
    marketPrice = coverPrice * discount
    copiesPrice = marketPrice * copies
    
    # Shipping cost
    firstCopyAmount = 3
    additionalCopy = 0.75

    # price for additional copy
    additionalCopies = copies - 1  # subtract one for first copy
    costPerAdditionalCopy = additionalCopy * additionalCopies

    # total shipping cost
    totalWholeCost = costPerAdditionalCopy + firstCopyAmount + copiesPrice

    print(f"Total Wholesale cost for {copies} is {totalWholeCost:.2f}")
    

def main():
    copies = int(input("How many copies do you want to purchase? "))
    bookPrice(copies)

main()


