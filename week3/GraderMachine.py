"""haha"""

def main():
    """aasasd"""
    start = int(input())
    stop = int(input())
    count = 0
    print("pass : ",end="")
    if stop < start:
        for i in range(start, stop-1, -2):
            if not i % 2:
                count += i
                print(int(i),sep=" ",end=" ")
        print(f"\nSum : {count}")
    else:
        for i in range(start, stop+1):
            if not i % 2:
                count += i
                print(int(i),sep=" ",end=" ")
        print(f"\nSum : {count}")

main()
