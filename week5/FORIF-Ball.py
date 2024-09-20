"""FOR!F-Ball"""

def main():
    """FOR!F-Ball"""
    left = 1
    middle = 0
    right = 0
    command = input()
    for text in command:
        if text == "A":
            left, middle = middle, left
        if text == "B":
            middle , right = right, middle
        if text == "C":
            left, right = right, left
    if left == 1:
        print("1")
    elif middle == 1:
        print("2")
    else:
        print("3")
main()
