"""Easy Histogram No Dict"""

def main():
    """Easy Histogram No Dict"""
    output = []
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    text = input()
    for i in alphabet:
        if i in text:
            number = text.count(i)
            if number > 0:
                output.append(i + " = " +  str(number))
    for i in output:
        print(i)
main()
