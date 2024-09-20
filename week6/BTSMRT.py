"""BTSMRT"""        

def main():
    """BTSMRT"""
    day_type = input()
    old = float(input())
    height = float(input())

    if (old < 14) and (height < 90):
        print("FREE")
    elif (day_type == "Children Day") and (old < 14) and (height <= 140):
        print("FREE")
    elif (day_type == "Senior Day") and (old >= 60):
        print("FREE")
    else:
        print("PAY")

main()
