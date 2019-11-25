from test_framework import generic_test

def first(tree):
    result = []

    if not tree:
        return result

    current_nodes = [tree]
    while current_nodes:
        result.append([cur.data for cur in current_nodes])
        current_nodes = [
            child 
            for cur in current_nodes for child in [cur.left, cur.right]
            if child
        ]
        # list comprehension
        # [expression for item in list if condition]

    return result


def binary_tree_depth_order(tree):
    return first(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
