"""doc sitring"""

def restrict_word_by_m(lixt):
    """find the side"""
    for i , _ in enumerate(lixt):
        for j , _ in enumerate(lixt[i+1:],start=i+1):
            if lixt[i] < lixt[j]:
                lixt[i], lixt[j] = lixt[j], lixt[i]
    return lixt

def is_triangle(lixt):
    """check"""
    true_size = ((lixt[1])**2 + (lixt[2])**2)**0.5
    if true_size - 0.01 <= lixt[0] <= true_size + 0.01:
        print("Yes")
    else:
        print("No")

def main():
    """docs"""
    lixt = []
    lixt.append(float(input()))
    lixt.append(float(input()))
    lixt.append(float(input()))
    sor_list = restrict_word_by_m(lixt)
    is_triangle(sor_list)
main()
