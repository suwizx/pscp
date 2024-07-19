'''30%'''
def main():
    '''main'''
    now_start= 1
    want = int(input())
    for _ in range(want):
        for i in range(now_start, now_start + want):
            print(i, end=" ")
        print("")
        now_start += want
main()
