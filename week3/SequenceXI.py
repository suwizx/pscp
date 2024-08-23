"""Sequence XI"""

def main():
    """Sequence XI"""
    prompt = int(input())
    for row in range(1, prompt+1):
        padding = prompt - row
        for col in range(1, row+1):
            print(f"{col:>02}", end=" ")
        print((f"{row:>02} ") * padding, end="")
        reversed_row = prompt - row
        reversed_padding = prompt - reversed_row
        print((f"{row:>02} ") * padding, end="")
        for col in range(reversed_padding - 1, 0 , -1):
            print(f"{col:>02}", end=" ")
        print()
    for row in range(prompt -1, 0, -1):
        padding = prompt - row
        for col in range(1, row+1):
            print(f"{col:>02}", end=" ")
        print((f"{row:>02} ") * padding, end="")
        reversed_row = prompt - row
        reversed_padding = prompt - reversed_row
        print((f"{row:>02} ") * padding, end="")
        for col in range(reversed_padding - 1, 0 , -1):
            print(f"{col:>02}", end=" ")
        print()
main()
