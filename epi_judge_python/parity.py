#4.7 Cot'lpuuNc rlrE pARITy oF A woRD
#The parity of a binary word is 1 if the number of 1s in the word is odd; 
#otherwise, it is 0. For example, the parity of 1011 is 1, and the parity 
#of 10001000 is 0. Parity checks are used to detect single bit errors in 
#data storage and communication. It is fairly straightforward to write 
#code that computes the parity of a single 64-bit word.
#How would you compute the parity of a very large number of 64-bit words?

from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
