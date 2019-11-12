from test_framework import generic_test, test_utils



digit_letters = {
    '0': ['0'],
    '1': ['1'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
}


# def get_letters(digit):
#     letters = []
#     if digit == 0 or digit == 1:
#         letters.append(str(digit))
#     else:
#         letter_range = (range(3) if digit < 9 else range(4))
#         for i in letter_range:
#             letters.append(chr(ord('A') + 3 * (digit - 2) + i))

#     return letters

def first(num):
    global digit_letters

    if len(num) == 1:
        return digit_letters[num]

    digit = num[-1]
    num = num[:-1]
    d_letters = digit_letters[digit]
    n_letters = first(num)
    letters = []

    for d in d_letters:
        for n in n_letters:
            letters.append(n + d)

    return letters

MAPPING = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

def second(phone_number):
    def get_letters(digit):
        if digit == len(phone_number):
            letters.append(''.join(word))        
        else:
            for c in MAPPING[int(phone_number[digit])]:
                word[digit] = c
                get_letters(digit + 1)

    letters = []
    word = [0] * len(phone_number)

    get_letters(0)

    return letters

def phone_mnemonic(phone_number):
    # return first(phone_number)
    return second(phone_number)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
