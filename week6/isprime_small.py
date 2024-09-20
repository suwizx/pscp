"""isprime_small"""

def is_prime(number):
    if number < 2:
        return False
    count = 0
    for i in range(1,number + 1):
        if not number % i:
            count += 1
    if count > 2:
        return False
    return True

def main():
    """is_prime()"""
    number = int(input())
    if  is_prime(number):
        print("Yes")
    else:
        print("No")
main()
