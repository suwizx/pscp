"""doc"""
number = int(input())
if not number % 4:
    print(1)
elif number % 4 == 1:
    print(7)
elif number % 4 == 2:
    print(9)
elif number % 4 == 3:
    print(3)
else:
    pass
