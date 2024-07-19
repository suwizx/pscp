"""lo"""

def asc(nb1, nb2, nb3):
    """asc"""
    if nb1 <= nb2 <= nb3:
        print(f"{nb1:.2f}", f"{nb2:.2f}", f"{nb3:.2f}", sep=", ", end="")
    elif nb1 <= nb3 <= nb2:
        print(f"{nb1:.2f}", f"{nb3:.2f}", f"{nb2:.2f}", sep=", ", end="")
    elif nb2 <= nb1 <= nb3:
        print(f"{nb2:.2f}", f"{nb1:.2f}", f"{nb3:.2f}", sep=", ", end="")
    elif nb2 <= nb3 <= nb1:
        print(f"{nb2:.2f}", f"{nb3:.2f}", f"{nb1:.2f}", sep=", ", end="")
    elif nb3 <= nb1 <= nb2:
        print(f"{nb3:.2f}", f"{nb1:.2f}", f"{nb2:.2f}", sep=", ", end="")
    elif nb3 <= nb2 <= nb1:
        print(f"{nb3:.2f}", f"{nb2:.2f}", f"{nb1:.2f}", sep=", ", end="")

def desc(nb1, nb2, nb3):
    """desc"""
    if nb1 >= nb2 >= nb3:
        print(f"{nb1:.2f}", f"{nb2:.2f}", f"{nb3:.2f}", sep=", ", end="")
    elif nb1 >= nb3 >= nb2:
        print(f"{nb1:.2f}", f"{nb3:.2f}", f"{nb2:.2f}", sep=", ", end="")
    elif nb2 >= nb1 >= nb3:
        print(f"{nb2:.2f}", f"{nb1:.2f}", f"{nb3:.2f}", sep=", ", end="")
    elif nb2 >= nb3 >= nb1:
        print(f"{nb2:.2f}", f"{nb3:.2f}", f"{nb1:.2f}", sep=", ", end="")
    elif nb3 >= nb1 >= nb2:
        print(f"{nb3:.2f}", f"{nb1:.2f}", f"{nb2:.2f}", sep=", ", end="")
    elif nb3 >= nb2 >= nb1:
        print(f"{nb3:.2f}", f"{nb2:.2f}", f"{nb1:.2f}", sep=", ", end="")

def main():
    """Main function"""
    how_to_do = input()
    nb1 = float(input())
    nb2 = float(input())
    nb3 = float(input())
    if how_to_do == "Ascend":
        asc(nb1, nb2, nb3)
    else:
        desc(nb1, nb2, nb3)

main()
