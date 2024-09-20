"""Harshad"""

def is_harshad(n):
    """Harshad"""
    devied_by = 0
    for i in str(n):
        devied_by += int(i)
    if devied_by == 0:
        return False
    if n % devied_by == 0:
        return True
    return False

def main():
    """Harshad"""
    for _ in range(10):
        numver = int(input())
        if is_harshad(numver):
            print("Yes")
        else:
            print("No")

main()
