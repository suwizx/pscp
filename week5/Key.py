"""key"""
def main():
    """key"""
    sum_digit = 0
    id_card = input()
    last_3_digitsvalid_cardate = int(id_card[-3:]) * 10
    for i in id_card:
        sum_digit += int(i)
    key = sum_digit + last_3_digitsvalid_cardate
    if key < 1000:
        key += 1000
        # print(key)
    if key > 9999:
        print(str(key)[-4:])
    else:
        print(key)

main()
