"""this is docstring"""

import math

def main():
    """d"""
    x = int(input())
    y = int(input())
    r = int(input())
    xn = int(input())
    yn = int(input())

    distance = math.sqrt(((x - xn) ** 2) + ((y - yn) ** 2))
    if distance <= r:
        print(True)
    else:
        print(False)
main()
