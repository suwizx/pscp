"""Sequence XII"""

def main():
    """Main function"""
    prompt = int(input())
    for from_ in range(prompt,0,-1):
        to_ = prompt + 1 - from_
        for i in range(from_,prompt):
            print(f"{i:>02} ",end="")
        for i in range(prompt,to_-1,-1):
            print(f"{i:>02} ",end="")
        for i in range(to_+1,prompt+1):
            print(f"{i:>02} ",end="")
        for i in range(prompt-1,from_-1,-1):
            print(f"{i:>02} ",end="")
        print("")
    for from_ in range(2,prompt+1,1):
        to_ = prompt + 1 - from_
        for i in range(from_,prompt):
            print(f"{i:>02} ",end="")
        for i in range(prompt,to_-1,-1):
            print(f"{i:>02} ",end="")
        for i in range(to_+1,prompt+1):
            print(f"{i:>02} ",end="")
        for i in range(prompt-1,from_-1,-1):
            print(f"{i:>02} ",end="")
        print("")
main()
