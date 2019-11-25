from test_framework import generic_test

def first(path):
    path_stack = []
    start_with_root = path.startswith('/')

    for p in path.split('/'):
        if p.isalnum():
            path_stack.append(p)
        elif p == '..':
            if not path_stack or not path_stack[-1].isalnum():
                path_stack.append(p)
            else:
                path_stack.pop()
    
    return ('/' if start_with_root else '') + '/'.join(path_stack)

def shortest_equivalent_path(path):
    return first(path)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
