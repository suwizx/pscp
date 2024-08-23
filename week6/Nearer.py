"""Nearer"""

def main():
    """Nearer"""
    Alice_position = int(input())
    Bob_position = int(input())
    Icream_position = int(input())

    if abs(Alice_position - Icream_position) < abs(Bob_position - Icream_position):
        print("Alice" , abs(Alice_position - Icream_position))
    elif abs(Alice_position - Icream_position) > abs(Bob_position - Icream_position):
        print("Bob" , abs(Bob_position - Icream_position))
    else:
        print("Sundaes"  , abs(Bob_position - Icream_position))
main()
