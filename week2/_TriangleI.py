"""doc sitring"""

def is_triangle(a, b, c):
    """docs"""
    if a**2 + b**2 == c**2:
        return "Yes"
    elif a**2 + c**2 == b**2:
        return "Yes"
    elif b**2 + c**2 == a**2:
        return "Yes"
    elif a**2 + b**2 == c**2 + 0.01:
        return "Yes"
    elif a**2 + c**2 == b**2 + 0.01:
        return "Yes"
    elif b**2 + c**2 == a**2 + 0.01:
        return "Yes"
    elif a**2 + b**2 == c**2 - 0.01:
        return "Yes"
    elif a**2 + c**2 == b**2 - 0.01:
        return "Yes"
    elif b**2 + c**2 == a**2 - 0.01:
        return "Yes"
    
    else:
        return "No"

def main():
    """docs"""
    a = float(input())
    b = float(input())
    c = float(input())
    print(is_triangle(a, b, c))
main()
