'''t'''
num = int(input())
for _ in range(num):
    if _+1  == num:
        print(str(num))
    else:
        print(str(_+1), end="")
        print("_", end="")
