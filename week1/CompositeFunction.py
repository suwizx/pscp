"""ejahu"""

def func_f(x):
    """f"""
    return 2*x

def func_g(x):
    """g"""
    return (x/2) + 1

def main():
    """main"""
    prompt = int(input())
    print(f"{func_f(func_g(prompt)):.2f}")
    print(f"{func_g(func_f(prompt)):.2f}")

main()
