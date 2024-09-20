"""Divide3Or5"""
def main():
    """Divide3Or5"""
    num_cahr = 0
    problem = []
    for i in range(1, int(input()) + 1):
        num_cahr += (i // 10) + 1
    plus_symbol = len(problem) - 1
    print(num_cahr + plus_symbol + 1)
main()
