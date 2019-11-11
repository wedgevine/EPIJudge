from test_framework import generic_test
import functools

def first(col):
    A_index, size = ord('A') - 1, len(col)
    iid = 0

    for i in range(size):
        iid = iid * 26 + ord(col[i]) - A_index

    return iid

# use reduce
def second(col):
    return functools.reduce(
        lambda iid, c: iid * 26 + ord(c) - ord('A') + 1,
        col,
        0
    )

def ss_decode_col_id(col):
    # return first(col)
    return second(col)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
