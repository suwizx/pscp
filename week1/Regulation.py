"""just code"""
A = int(input())
B = float(input())
C = input()

print(f"{A:>30}")
if A < 0:
    print(f"-{abs(A):0>29}")
else :
    print(f"{A:0>30}")
print(f"{B:.2f}")
print(f"{B:.12f}")
print(f"{C:>40}")
