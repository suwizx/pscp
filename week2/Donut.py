"""Donut"""
def main():
    """Donut"""
    donut_price = int(input())
    dount_pro_number = int(input())
    donut_pro_get_free = int(input())
    all_donut_want = int(input())

    now_donut_buy = 0
    now_donut_get = 0
    now_price = 0

    while now_donut_get < all_donut_want:
        now_donut_buy += 1
        now_donut_get += 1
        now_price += donut_price
        if now_donut_buy >= dount_pro_number:
            now_donut_buy = 0
            now_donut_get += donut_pro_get_free
    print(now_price , now_donut_get , sep=" ")

main()
