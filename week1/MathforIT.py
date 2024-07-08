"""Math for IT"""

import math

PI = math.pi

def main():
    """main"""
    radius = float(input())
    area =  PI * radius ** 2
    circumference = 2 * PI * radius
    print(f"Area: {area:.3f}\nCircumference: {circumference:.3f}")
main()
