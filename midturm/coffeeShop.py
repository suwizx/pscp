"""Coffee Shop"""
def main():
    """Coffee"""
    coffee_price = float(input())
    discount_1 = float(input())
    discount_2 =  float(input())
    promotion_2 = float(input())
    coffee_want = int(input())

    price_1 = 0
    if coffee_want > 0:
        price_1 += coffee_price
        promotion_1 = (coffee_price * (coffee_want - 1) - ((coffee_price * (coffee_want - 1)) * (discount_1 / 100)))
        price_1 += promotion_1

    price_2 = 0
    price_2 = coffee_want * coffee_price
    if price_2 >= promotion_2:
        price_2 = price_2 - (price_2 * discount_2 / 100)

    if price_2 <= price_1:
        print(2)
        print(f"{price_2:.2f}")
    else:
        print(1)
        print(f"{price_1:.2f}")

main()
