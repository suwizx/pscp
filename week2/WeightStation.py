"""main"""

def main():
    """main"""
    average_weight = float(input())
    weight_1 = float(input())
    weight_2 = float(input())
    weight_3 = float(input())

    weight_4 = (average_weight * 4) - (weight_1 + weight_2 + weight_3)

    weight_1_condition = abs(weight_1 - average_weight) > average_weight / 2
    weight_2_condition = abs(weight_2 - average_weight) > average_weight / 2
    weight_3_condition = abs(weight_3 - average_weight) > average_weight / 2
    weight_4_condition = abs(weight_4 - average_weight) > average_weight / 2

    if weight_1 + weight_2 + weight_3 + weight_4 > 15 * 1000:
        print("Overweight")

    elif weight_1_condition or weight_2_condition or weight_3_condition or weight_4_condition:
        print("Unbalance")

    else:
        print(f"Pass {weight_4:.2f}")
main()
