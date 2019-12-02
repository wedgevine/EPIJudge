from test_framework import generic_test
from collections import namedtuple

# from book, better
def second(tree):
    Balance = namedtuple('Balance', ('is_balance', 'height'))

    def check_balance(tree):
        if not tree:
            return Balance(True, -1)
        
        left_balance = check_balance(tree.left)
        
        if not left_balance.is_balance:
            return left_balance

        right_balance = check_balance(tree.right)

        if not right_balance.is_balance:
            return right_balance

        is_balance = abs(left_balance.height - right_balance.height) <= 1
        height = max(left_balance.height, right_balance.height) + 1

        return Balance(is_balance, height)
        
    return check_balance(tree).is_balance

# fatser than second, use height to denote balance and height
# height = -1 not balanced
# height >= 0 balanced, real height
def first(tree):
    def get_balanced_height(tree):
        if not tree:
            return 0 

        left_height = get_balanced_height(tree.left)
        if left_height == -1:
            return left_height

        right_height = get_balanced_height(tree.right)
        if right_height == -1:
            return right_height

        if abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1

    return get_balanced_height(tree) != -1

def is_balanced_binary_tree(tree):
    return first(tree)
    # return second(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
