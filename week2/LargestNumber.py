"""doc string"""

def main():
    """main"""
    input_1 = str(input())
    input_2 = str(input())
    input_3 = str(input())

    number_1 = int(input_1 + input_2 + input_3)
    num_m = number_1
    number_2 = int(input_1 + input_3 + input_2)
    if number_2 > num_m:
        num_m = number_2
    number_3 = int(input_2 + input_1 + input_3)
    if number_3 > num_m:
        num_m = number_3
    number_4 = int(input_2 + input_3 + input_1)
    if number_4 > num_m:
        num_m = number_4
    number_5 = int(input_3 + input_1 + input_2)
    if number_5 > num_m:
        num_m = number_5
    number_6 = int(input_3 + input_2 + input_1)
    if number_6 > num_m:
        num_m = number_6
    print(num_m)

main()
