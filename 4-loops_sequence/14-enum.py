#!/usr/bin/python3
"""Enumerate function
    Arguments:
            iterate to enumerate
            counting number(default = 0)
"""
#How enumerate works
for i, item in enumerate(['a','b','c','d'],1):
    print(i, item, sep = '. ')
## without variable to hold count
def main():
    with open("state.txt") as f:
        states = f.read().splitlines()

    for i, state in enumerate(states,1):
        state_name = state.split("\t")[0]
        print(f"{i}. {state_name}")
main()

