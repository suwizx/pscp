"""sefks"""

def main():
    """sefks"""
    size = int(input())
    align = input()
    text = input()
    if align == "left":
        print(f"{text:<{size}}")
    elif align == "right":
        print(f"{text:>{size}}")
    elif align == "center":
        text_len = len(text)
        if (size - text_len) % 2:
            print(f"{(((size - text_len) // 2) + 1) * ' ' }{text}{((size - text_len) // 2) * ' '}")
        else :
            print(f"{text: ^{size}}")
    else:
        print("Invalid alignment")

main()
