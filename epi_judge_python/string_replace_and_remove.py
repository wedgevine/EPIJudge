import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def first(size, s):
    current, final_size = size - 1, size * 2 - 1

    while current:        
        if s[current] == 'a':
            s[final_size] = 'd'
            s[final_size - 1] = 'd'
            final_size -= 2            
        elif s[current] != 'b':
            s[final_size] = s[current]
            final_size -= 1

        current -= 1
    
    current = final_size + 1
    index = 0
    while current < size * 2:
        s[index] = s[current]
        index += 1
        current += 1
    print(index)
    s = s[:index]
    return s
    
def replace_and_remove(size, s):
    current, final_size = size - 1, size * 2 - 1

    while current:        
        if s[current] == 'a':
            s[final_size] = 'd'
            s[final_size - 1] = 'd'
            final_size -= 2            
        elif s[current] != 'b':
            s[final_size] = s[current]
            final_size -= 1

        current -= 1
    
    current = final_size + 1
    index = 0
    while current < size * 2:
        s[index] = s[current]
        index += 1
        current += 1

    return index


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
