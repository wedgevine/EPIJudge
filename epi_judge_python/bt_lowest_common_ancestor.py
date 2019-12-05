import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple

def first(tree, node0, node1):
    # AncestorNode = namedtuple('AncestorNode', ('node', 'ancestor0', 'ancestor1', 'visited'))

    # if not tree or not node0 or not node1:
    #     return None

    # if node0 is tree or node1 is tree:
    #     return tree
    
    ancestors = []
    current = tree
    node0_found = node1_found = False 

    while ancestors or current:
        if current:
            # node = AncestorNode(current, False, False, False)
            node = [current, False, False, False]
            ancestors.append(node)
            if current is node0:
                node0_found = True
                for n in ancestors:
                    # n.ancestor0 = True
                    n[1] = True
            if current is node1:
                node1_found = True
                for n in ancestors:
                    # n.ancestor1 = True
                    n[2] = True
            if node0_found and node1_found:
                break
            current = current.left
        else:
            node = ancestors.pop()
            # if not node.visited:
            if not node[3]:
                # ancestors.append(AncestorNode(node.node, False, False, True))
                node[3] = True
                ancestors.append(node)
                current = node[0].right

    for n in reversed(ancestors):
        # if n.ancestor0 and n.ancestor1:
        if n[1] and n[2]:
            return n[0]
    
    return None

def lca(tree, node0, node1):
    return first(tree, node0, node1)


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
