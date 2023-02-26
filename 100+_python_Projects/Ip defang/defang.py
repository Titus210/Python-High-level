

def ip_defang(address, separator):
    """
    Defangs user IP adress """

    # create null address to hold ip
    new_address = ""

    # split address in comma
    split_address = address.split(".")

    # join the split address with separator
    new_address = separator.join(split_address)

    user_authentication(separator, new_address)

def user_authentication(separator, new_address):
    """
    Gets user to input the separator"""

    user_separator = str(input("Enter the separator to view ip adress: "))


    if user_separator == separator:
        print(f"The new ip address is : {new_address}")
    else:
        print("sorry you can't view the ip address! Enter valid separator")
        user_authentication()
    

def main():
    """Get ip adress from client
    """

    ip_address = str(
        input("Enter a valid IP address in format:(192.168.2.1) "))

    # make a separator
    separator = "$."

    # call defang method
    ip_defang(ip_address, separator)


main()
