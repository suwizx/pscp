"""0811234567 International"""

def main():
    """0811234567 International"""
    phone = input()
    cuntry_type = input()

    if cuntry_type == "International":
        phone = phone.replace("0", "+66", 1)

    if len(phone) == 12 and cuntry_type == "International":
        print(f"{phone[:4]} {phone[4:8]} {phone[8:]}")

    if len(phone) == 10 and cuntry_type == "Domestic":
        print(f"{phone[:2]} {phone[2:6]} {phone[6:]}")

    if len(phone) == 9 and cuntry_type == "Domestic":
        print(f"{phone[:1]} {phone[1:5]} {phone[5:]}")

    if len(phone) == 11 and cuntry_type == "International":
        print(f"{phone[:3]} {phone[3:7]} {phone[7:]}")

main()
