"""why sequance again"""

def top(n):
    """qojkerwoewr"""
    for i in range(1,n+1):
        top_indent = n-i+1
        print("   "*top_indent,end="")
        for i in range(1,i+1):
            if i >= 10:
                print(str(i)+" ",end="")
            else:
                print("0"+str(i)+" ",end="")
        for i in range(i-1,0,-1):
            if i >= 10:
                print(str(i)+" ",end="")
            else:
                print("0"+str(i)+" ",end="")
        print("")

def bottom(n):
    """jsut docstring"""
    for i in range(n+1,0,-1):
        top_indent = n-i+1
        print("   "*top_indent,end="")
        for i in range(1,i+1):
            if i >= 10:
                print(str(i)+" ",end="")
            else:
                print("0"+str(i)+" ",end="")
        for i in range(i-1,0,-1):
            if i >= 10:
                print(str(i)+" ",end="")
            else:
                print("0"+str(i)+" ",end="")
        print("")

def main():
    """jadij"""
    n = int(input())-1
    top(n)
    bottom(n)

main()
