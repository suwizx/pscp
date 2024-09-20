"""Counting Stars"""

def main(s):
    """Counting Stars"""
    comet_count = 0
    shooting_star_count = 0
    constellation_count = 0

    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == '~' and s[i + 1] == '*':
            comet_count += 1
            i += 2
        elif i + 1 < len(s) and s[i] == '*' and s[i + 1] == '/':
            shooting_star_count += 1
            i += 2
        elif i + 1 < len(s) and s[i] == '*' and s[i + 1] == '*':
            constellation_count += 1
            i += 2
        else:
            i += 1
    
    if constellation_count == 0 and comet_count == 0 and shooting_star_count == 0:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {constellation_count}")
        print(f"comet: {comet_count}")
        print(f"shooting star: {shooting_star_count}")

main(input())
