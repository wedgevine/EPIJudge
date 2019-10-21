#4.7 Cot'lpuuNc rlrE pARITy oF A woRD
#The parity of a binary word is 1 if the number of 1s in the word is odd; 
#otherwise, it is 0. For example, the parity of 1011 is 1, and the parity 
#of 10001000 is 0. Parity checks are used to detect single bit errors in 
#data storage and communication. It is fairly straightforward to write 
#code that computes the parity of a single 64-bit word.
#How would you compute the parity of a very large number of 64-bit words?

from test_framework import generic_test

def get_base_parity(x):
    result = 0
    while x > 0:
        result ^= x & 1
        x >>= 1
    return result
    
base4_parity = [get_base_parity(k) for k in range(1 << 4)]
base8_parity = [get_base_parity(k) for k in range(1 << 8)]
base16_parity = [get_base_parity(k) for k in range(1 << 16)]

def get_base4_parity(x):
    result = 0
    while x:
        result ^= base4_parity[x & 0xF]
        x >>= 4
    return result

def get_base8_parity(x):
    result = 0
    while x:
        result ^= base8_parity[x & 0xFF]
        x >>= 8
    return result

def get_base16_parity(x):
    result = 0
    while x:
        result ^= base16_parity[x & 0xFFFF]
        x >>= 16
    return result

def get_parity_lsb(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

def get_parity_association(x):
    # suppose x is represented 64 bit binary
    x ^= x >> 32
    x ^= x >> 16
    return base16_parity[x & 0xFFFF]

def parity(x):
    # return get_base16_parity(x)          # 6us, 4us, 3us
    # return get_parity_lsb(x)              # 6us
    return get_parity_association(x)      # 2us

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))


#%%
