"""sort dunction"""
def max_to_min(list):
    """ijeidiesji"""
    for i in range(len(list)):
        print(i)
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list

def main():
    """main"""
    number = int(input())
    # while number != 6174:
    print(max_to_min(str(number)))
    
main()