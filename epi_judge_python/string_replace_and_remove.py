import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# a simpler solution based on an assumption
# that the array's length is more than 2 times of the size parameter
# well, it is not true
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

    return index
    
# the idea is for every element checked, it may need to go back, stay, or go forward
# based on free_space value kept, it is easier to go back or stay
# for go forward, need to record the first element position need to go forward
# as long as we find enough space (within or outside size limit) for these elements, move them forward
def second(size, s):
    current, c_char = 0, ''
    move_start = float('inf')
    final_size = size
    free_space = 0

    while current < size:
        c_char = s[current]
        if free_space > 0:
            if c_char == 'b':
                free_space += 1
                final_size -= 1
            elif c_char == 'a':
                s[current - free_space] = 'd'
                s[current - free_space + 1] = 'd'
                free_space -= 1
                final_size += 1
            else:
                s[current - free_space] = c_char
        elif free_space == 0:
            if c_char == 'a':
                move_start = current
                free_space -= 1
                final_size += 1
            elif c_char == 'b':
                free_space += 1
                final_size -= 1
        else:
            if c_char == 'a':
                free_space -= 1
                final_size += 1
            elif c_char == 'b':
                free_space += 1
                if free_space == 0:
                    move_target = current
                    index = current

                    while index >= move_start:
                        if s[index] == 'a':
                            s[move_target] = 'd'
                            s[move_target - 1] = 'd'
                            move_target -= 2
                        elif s[index] != 'b':
                            s[move_target] = s[index]
                            move_target -= 1
                        index -= 1

                    move_start = float('inf')

                final_size -= 1

        current += 1
        if move_start < 0:
            move_start = current
        
    if free_space < 0:
        final_size = size + free_space * (-1)
        move_target = final_size - 1
        index = size - 1

        while index >= move_start:
            if s[index] == 'a':
                s[move_target] = 'd'   
                s[move_target - 1] = 'd'
                move_target -= 2
            elif s[index] != 'b':
                s[move_target] = s[index]
                move_target -= 1
            index -= 1

    return final_size

def replace_and_remove(size, s):
    # return first(size, s)
    return second(size, s)

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
