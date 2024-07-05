"""F"""
def main():
    """F"""
    input_number = int(input())
    count_a = 0
    result = 0
    for _ in range(input_number):
        input_number = str(input())
        if input_number == "A":
            count_a += 1
        elif input_number in ("J","Q","K"):
            result += 10
        else:
            result += int(input_number)
    if count_a == 3:
        result += 11 + 1 + 1
    elif count_a == 2:
        if (result + 11 + 1) <= 21:
            result += 12
        else:
            result += 2
    elif count_a == 1:
        if (result + 11) <= 21:
            result += 11
        else:
            result += 1
    else:
        pass
    print(result)

main()
