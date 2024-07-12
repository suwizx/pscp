"""Tiem"""

def main():
    """Main function"""
    is_error = False
    secound_input = int(input())
    if secound_input < 0 or secound_input >= 864000000:
        is_error = True

    day = secound_input // (60 * 60 * 24)

    hour = (secound_input - (day * 60 * 60 * 24)) // (60 * 60)
    minute = (secound_input - (day * 60 * 60 * 24) - (hour * 60 * 60)) // 60
    secound = secound_input - (day * 60 * 60 * 24) - (hour * 60 * 60) - (minute * 60)


    if is_error:
        print("ERR_:__:__:__")
    else:
        print(f"{day:>04}:{hour:>02}:{minute:>02}:{secound:>02}")

main()
