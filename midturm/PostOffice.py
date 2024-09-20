"""Post Office"""

def envelop_price(weight):
    """envelop_price"""
    if weight > 1000:
        return 68
    elif weight > 500:
        return 48
    elif weight > 250:
        return 33
    elif weight > 100:
        return 28
    elif weight > 20:
        return 23
    elif weight > 10:
        return 18
    return 16

def package_price(weight):
    """package_price"""
    if weight > 1000:
        return 70
    elif weight > 500:
        return 55
    return 45

def main():
    """Post Office"""
    price = 0
    envelop = int(input())
    package = int(input())
    for _ in range(envelop):
        envelop_weight = float(input())
        price += (envelop_price(envelop_weight) + 13)
    for _ in range(package):
        package_weight = float(input())
        price += (package_price(package_weight) + 15)
    print(price)
main()
