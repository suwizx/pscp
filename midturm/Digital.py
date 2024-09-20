"""Digital"""

def parse_to_bool(s_input):
    """parse tp bool"""
    if s_input == "Yes" or s_input == "True":
        return True
    return False

def digi_check(is_thai , is_home , age , income , bank):
    """digi_check"""
    condi_1 = False
    condi_2 = False
    condi_3 = False
    condi_4 = False
    if is_home and is_thai:
        condi_1 = True
    if age >= 16 and bank <= 500000:
        condi_2 = True
    if income <= 840000:
        condi_3 = True
    if bank <= 500000:
        condi_4 = True
    if condi_1 and condi_2 and condi_3 and condi_4:
        return True
    return False

def main():
    """Digital"""
    name = input()
    is_thai = input()
    is_home = input()
    age = float(input())
    income = float(input())
    bank = float(input())

    is_thai = parse_to_bool(is_thai)
    is_home = parse_to_bool(is_home)

    can_get = digi_check(is_thai , is_home , age , income , bank)

    if can_get:
        print(f"Congratulations! {name} is qualified to receive a digital wallet \
amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
