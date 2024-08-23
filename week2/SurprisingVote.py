'''Suprising vote'''

def main():
    '''Suprising vote'''
    all_score = float(input())
    max_score = float(input())
    if all_score - (max_score * 2) > 0:
        min_score = all_score - max_score * 2
    else :
        min_score =  all_score - max_score
    if abs(max_score - min_score) > 2:
        print("Surprising")
    else :
        print("Not surprising")

main()
