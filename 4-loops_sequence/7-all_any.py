#!/usr/bin/python3
"""Checks if values passed are all true or any exist among them"""

def all_True(iterable):
    """Check if all are true"""
    # Returns false if item is false
    for item in iterable:
        if not item:
            return False
    # Return  true if is Looped items are not false
    return True


def any_True(iterable):
    """Checks if any among is true"""
    # Return True if any item is true
    for item in iterable:
        if item:
            return True
    # Return false if items are not true frm loop
    return False

def main():
    a = all_True([1, 0, 1, 1, 1])
    b = all_True([1, 1, 1, 1, 1])
    c = any_True([0, 0, 0, 1, 1])
    d = any_True([0, 0, 0, 0, 0])
    print(f'{a} \n {b} \n {c} \n {d} ')
main()
