#!/usr/bin/python3
"""
    Users enters state abbreviation  to get full state name
"""
def get_state(abbreviation):
    """REad data in file to alist"""
    with open('state.txt') as f:
        states = f.read().splitlines()

        #loop through list
    for state_row in states:
        # split earch row in tab to two-element list
        state = state_row.split('\t')

        # If second element match passed abreviation return first element
        if state[1] == abbreviation.upper():
            return state[0]

    ## if no state match abbreviation return None
    return None

def main():
    # loop until break statement
    while True:
        abbr = input("Enter state  abbreviation (q to quit): ").upper()

    # allow user to break by entering Q
        if abbr == 'Q':
            print("Goodbye")
            break

    # get state name from abbreviation
        state = get_state(abbr)

    # tell uuser which state if any maps with abbreviation
        if state:
            print("f{abbr} is abbreviation of state {state}.")

        else:
            print(f"No state has abbreviation {abbr}")
main()
