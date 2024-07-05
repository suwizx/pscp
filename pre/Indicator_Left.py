"""Indicator_Left"""
k = int(input())
n = int(input())

for line in range(n):
    indent = abs(line - (n//2))
    print(indent*" ",k*"*",sep="",end="\n")
