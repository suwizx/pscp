"""Game"""

def main():
    """Game"""
    score_a = int(input())
    score_b = int(input())

    mod_a = score_a % 3
    mod_b = score_b % 3

    if mod_a < mod_b:
        if not (score_b + (3 * mod_a) == score_a):
            print("Error")
        else :
            print(mod_a)
    else:
        if not (score_a + (3 * mod_b) == score_b):
            print("Error")
        else :
            print(mod_b)

main()
