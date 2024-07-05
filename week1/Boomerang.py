"""main function"""

import math

def func_f(x):
    """function"""
    return x+1

def func_y(y):
    """function"""
    return (7*(y**3)) + (2*(y**2)) - (31*y) + 1

def func_z(z):
    """function"""
    return -1 * z

def func_xy(x,y):
    """function"""
    return (x+y)*(x-y)

def func_xyz(x,y,z):
    """function"""
    return (y-(math.sqrt((y**2) - (4*x*z))))/(2*x)

def main():
    """stupid function"""
    x = int(input())
    y = int(input())
    z = int(input())
    print(func_f(x))
    print(func_y(y))
    print(func_z(z))
    print(func_xy(x,y))
    print(func_xyz(x,y,z))
main()
