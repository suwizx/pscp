"""BigFrame"""

def main():
    """BigFrame"""
    line_1 = input().strip()
    line_2 = input().strip()
    line_3 = input().strip()
    line_4 = input().strip()
    line_5 = input().strip()

    max_len = max(len(line_1), len(line_2), len(line_3), len(line_4), len(line_5))

    print("*" * (max_len + 4))
    print(f"* {line_1:<{max_len}} *")
    print(f"* {line_2:<{max_len}} *")
    print(f"* {line_3:<{max_len}} *")
    print(f"* {line_4:<{max_len}} *")
    print(f"* {line_5:<{max_len}} *")
    print("*" * (max_len + 4))

main()
