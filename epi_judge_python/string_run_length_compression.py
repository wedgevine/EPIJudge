from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding_first(s):
    size, result = len(s), []
    count, count_start, count_end = 0, 0, 0

    # print("s: ", s)
    while count_start < size:
        while count_end + 1 < size and s[count_end + 1].isdigit():
            count_end += 1
        count = int(s[count_start:count_end + 1])
        # print('\n', count, s[count_end + 1])
        for _ in range(count):
            result.append(s[count_end + 1])
        count_end = count_end + 2
        count_start = count_end
    # print('result: ', result)
    return ''.join(result)

def decoding(s):
    return decoding_first(s)


def encoding_first(s):
    size, result = len(s), []
    current = 0

    # print('encode s: ', s)
    while current < size:
        count = 1
        while current + 1 < size and s[current + 1] == s[current]:
            current += 1
            count += 1
        result.append(str(count) + s[current])
        current += 1

    # print('encode result: ', result)
    return ''.join(result)

def encoding(s):
    return encoding_first(s)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
