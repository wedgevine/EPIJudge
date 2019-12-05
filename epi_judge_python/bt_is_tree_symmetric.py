from test_framework import generic_test


def first(tree):
    def is_tree_symmetric(root1, root2):
        if not root1 and not root2:
            return True
        elif (root1 and root2
            and root1.data == root2.data
            and is_tree_symmetric(root1.left, root2.right)
            and is_tree_symmetric(root1.right, root2.left)):
            return True
        else:
            return False

    return not tree or is_tree_symmetric(tree.left, tree.right)

def is_symmetric(tree):
    return first(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
