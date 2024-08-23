"""sjefesjfisjefiesj"""

def beatify(text):
    """kseokfose"""
    time_arr = []
    length = len(text)
    for i in range(0,length):
        if not i % 2:
            time_arr.append(text[i:i+2])
    return time_arr

data = beatify(input())
for i in data:
    time = int(i[0])
    char = str(i[1])
    print(char*time, end="")
