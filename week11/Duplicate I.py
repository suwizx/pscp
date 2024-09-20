"""Duplicate I"""
def main():
    """Duplicate I"""
    student = []
    duplicate = []
    a_number = int(input())
    b_number = int(input())
    for _ in range(a_number+b_number):
        student.append(input())
    for i in student:
        if student.count(i) > 1:
            if i not in duplicate:
                duplicate.append(i)
    if not duplicate:
        print("Nope")
    else:
        duplicate.sort(reverse=True)
        print("\n".join(duplicate))
main()
