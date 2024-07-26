"""why sequance again"""
def main():
    """jadij"""
    n = int(input())
    for i in range(1,n+1):
        top_indent = n-i
        print("   "*top_indent,end="")
        for i in range(1,i+1):
            if i >= 10:
                print(str(i)+" ",end="")
            else:
                print("0"+str(i)+" ",end="")
        print("")
main()
