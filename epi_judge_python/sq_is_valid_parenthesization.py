from test_framework import generic_test

# from book, simpler
def second(s):
    LOOKUP = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stack = []
    for p in s:
        if p in LOOKUP:
            stack.append(p)
        elif not stack or LOOKUP[stack.pop()] != p: 
            return False
    
    return not stack

def first(s):
    test = ['']
    PARENTHESIS = {
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{',
        '': '',
    }
    for p in s:
        if p == PARENTHESIS[test[-1]]:
            test.pop()
        else:
            test.append(p)
    
    return True if test == [''] else False

def is_well_formed(s):
    # return first(s)
    return second(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
