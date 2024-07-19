"""fijesrif"""

def main():
    """ujdu9asiowejd"""
    want = int(input())
    prompt = False
    sum_number = 0
    while not(prompt == -1 or sum_number == want):
        prompt = int(input())
        if prompt == -1:
            pass
        else:
            sum_number += prompt
    print(sum_number)
main()
