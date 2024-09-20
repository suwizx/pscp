"""Easy Histogram No Dict"""

def main():
    """Easy Histogram No Dict"""
    output = []
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    text = input()
    for i in alphabet:
        if i in text:
            number = 0
            for j in text:
                if i == j:
                    number += 1
            output.append(f"{i} = {number}")
    for i in output:
        print(i)
main()
