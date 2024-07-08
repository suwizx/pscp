"""docstring"""

GIFTS = []

def main():
    "main"
    for _ in range(8):
        prompt = int(input())
        GIFTS.append(prompt)

    for gift in GIFTS:
        if not gift % 2:
            print(gift)
main()
