# some tips

# retrieving and updating A[i] is O(1)
# event appending may result in resizing, if we double the size for every 
# resizing, the complexity for appending is amortized to O(1)
# for deleting and insertion of element at i, n-i elements need to be moved
# so the complexity is O(N)
# so better to delete/add elements from the end, not the start
# or instead of deleting an element, consider overwriting it
# "python array append vs insert"

# a benefit of array is we can work on it from both ends
# try to work on the space of the array itself, to reduce the space to O(1)
# be careful with index handling, never out of range

# learnt from apply_permutation, if want to change a list passed as parameter
# for example, for function, f(a), a is a list, inside the function, do
# a[:] = new_list, instead a = new_list, the former changed elements of a
# while the latter changed value of a, making a point to another object
# https://stackoverflow.com/questions/22054698/python-modifying-list-inside-a-function