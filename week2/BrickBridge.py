"""BrickBridge"""

def main():
    """BrickBridge"""
    small_brick_num = int(input())
    large_brick_num = int(input())
    goal_distance = int(input())
    want_use_large = goal_distance // 5
    if want_use_large <= large_brick_num:
        want_use_small = goal_distance - (want_use_large * 5)
        if want_use_small > small_brick_num:
            print(-1)
        else:
            print(want_use_small)

    # big want use > have
    else :
        if (large_brick_num * 5) + small_brick_num >= goal_distance :
            print(goal_distance - (large_brick_num * 5))
        else :
            print(-1)
main()
