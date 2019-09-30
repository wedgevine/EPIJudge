# Minimum number of jumps to reach end

# https://leetcode.com/problems/jump-game-ii/discuss/?currentPage=1&orderBy=hot&query=
# https://stackoverflow.com/questions/27858356/how-to-find-minimum-number-of-jumps-to-reach-the-end-of-the-array-in-on-time
def min_jump_to_end(A):

    if not A:
        return 0
    
    current_start, current_pos = 0, 0
    last_pos = len(A) - 1
    jump, limit = 0, 0

    while current_pos < last_pos:
        limit = current_start + A[current_start]
        #print('\nbefore: ', current_start, current_pos, limit)
        if limit >= last_pos:
            jump += 1
            break
        pre_limit = limit
        for i in range(current_pos, pre_limit + 1):
            if i + A[i] >= limit:
                limit = i + A[i]
                current_start = i
        if pre_limit == limit:
            return -1
        else:
            current_pos = pre_limit
            jump += 1
        #print('\nafter: ', current_start, current_pos, limit, jump)

    return jump

if __name__ == '__main__':
    print(min_jump_to_end([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(min_jump_to_end([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))
    print(min_jump_to_end([1, 3, 6, 1, 0, 9]))
    print(min_jump_to_end([2, 3, 1, 1, 4]))
    exit()