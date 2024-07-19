"""docstring"""
import math

def main():
    """docstring"""
    position_x = float(input())
    position_y = float(input())
    radius = float(input())
    mos_position_x = float(input())
    mos_position_y = float(input())
    d = math.sqrt(((position_x - mos_position_x) ** 2) + ((position_y - mos_position_y) ** 2))
    if d <= radius:
        print("Yes")
    else:
        print("No")

main()
