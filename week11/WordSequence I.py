"""WordSequence I"""

def main():
    """WordSequence I"""
    text = input()
    alphaCount = len(text)
    for i in range(alphaCount):
        print(text[0:i+1])
main()
