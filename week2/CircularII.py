"""doc"""
import math

def main():
    """docs"""
    x_1 = float(input())
    y_1 = float(input())
    r_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())
    r_2 = float(input())

    all_r = r_1 + r_2
    d = math.sqrt(((x_1 - x_2) ** 2) + ((y_1 - y_2) ** 2))
    if all_r > d:
        print("Yes")
    else:
        print("No")
main()
