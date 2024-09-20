"""sor_ dunction"""
def sor__desc(num_str):
    """sor__desc"""
    num_list = list(num_str)
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] < num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return ''.join(num_list)

def sor__asc(num_str):
    """sor__asc"""
    num_list = list(num_str)
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return ''.join(num_list)

def main():
    """main"""
    time = 0
    number = int(input())
    while number != 6174:
        number = f'{number:04d}'
        large = int(sor__desc(number))
        small = int(sor__asc(number))
        number = large - small
        time += 1
    print(time)

main()
