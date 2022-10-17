#!/usr/bin/python3
"""Checks if its a state available"""
def is_state(state):
    """checks if state entered by user is a state available
        Paremeter:
                state: User inputed states
    """
    with open("state.txt") as f:
        states = f.read().splitlines()
    state_abbr = []
    for state_row in states:
        state_abbr = state_row.split("\t")[1]
        state_abbr.append(state_abbr)

    return state in state_abbr

def main():
    print("Name as many state abbrviations you know:\n Separate them with spaces ")
    states = input('').split()
    bad_state = False
    for state in states:
        state = state.upper()
        if not is_state(state):
            print(f"{state} is not a state")
            bad_state = True
            break
    else:
        print(f"You named {len(states)} states.")

main()
