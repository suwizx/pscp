"""All_Primes"""

def is_prime(number):
    """is_prime()"""
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
    """All_Primes"""
    count = 0
    number = int(input())
    for i in range(2, number + 1):
        if is_prime(i):
            count += 1
    print(count)
main()
