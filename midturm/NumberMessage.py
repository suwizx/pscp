"""Number Message"""

def main():
    """Number Message"""
    output_str = ""
    prompt = input()
    prompt = prompt.replace("12","R")
    prompt = prompt.replace("13","B")
    prompt = prompt.replace("0","O")
    prompt = prompt.replace("5","S")
    prompt = prompt.replace("4","A")
    prompt = prompt.replace("3","E")
    prompt = prompt.replace("1","I")
    for char in prompt:
        if char == " ":
            output_str += " "
        elif char.isalpha():
            output_str += char.upper()
        elif not char.isnumeric():
            output_str += char

    print(output_str)

main()
