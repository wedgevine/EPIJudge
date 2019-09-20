#%% bitwise operators
# in python, int has no limit, has infinite precision, thus has infinite bits
# also in python, int, when interested in its binary representation,
# is represented by 2's complement notation/schema
# thus, for positive numbers and 0, 2's complement notation is the same as 
# classical binary representation
# for negative numbers, -x, is written using bit pattern for (x-1), then
# with all the bits complemented (switch from 1 to 0 and 0 to 1)
# so -1 is (1-1), 0, with all bits complemented, 1111 (if we use 4 bits as 
# limit), since there is no bit limit for python int, it actually should be
# ...1111...1, unlimited 1
# for the same reason, for positive int, there are unlimited 0 in the beginning
# of its binary representation, 5 is ...000...0101

# based on this representation, we have the following bitwise operators
# x << y, like x * pow(2, y)
# x >> y, like x // pow(2, y), // is floor division
# x & y, bitwise and, each bit of output is 1 if x and y is 1, otherwise 0
# x | y, bitwise or, each bit of output is 0 if x and y is 0, otherwise 1
# ~x, complement of x, switch each bit to its complement, 1 to 0 and 0 to 1
# x ^ y, bitwise exclusive or, each bit of output is the same the corresponding
# bit in x if that bit in y is 0, and it's the complement of the bit of x if 
# that bit in y is 1
# all these operations should apply commuutativity and associativity laws

# considering int is represented by 2's complement
# positive & negative results positive int
# positive | negative results in negative int
# ~x acturally get -x-1
# postive ^ negative results negative int

# ref
# https://wiki.python.org/moin/BitwiseOperators
# https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html
# https://stackoverflow.com/questions/1049722/what-is-2s-complement

#%% bit hacks and applications
# clear the lowermost set bit
x = 0b011100
print(bin(x & (x-1)))
# extract the lowest set bit
x = 0b011100
print(bin(x & ~(x-1)))
# set the lowermost 0
x = 0b11101011
print(bin(x | (x+1)))
# get position of least significant bit in a number
# note -x = ~x + 1
x = 0b00000000000000000000000001100000
print(bin(x & (-x)))
# right propagate the rightmost set bit
x = 0b01010000
print(bin(x ^ (x-1) | x))
# computer x modulo a power of 2
x = 77
print(77 ^ 0b01000000)
# test x is power of 2
x = 64
print((x != 0) and (x & (x-1) == 0))

# ref 
# http://graphics.stanford.edu/~seander/bithacks.html
# https://wiki.python.org/moin/BitManipulation
# https://stackoverflow.com/questions/tagged/bit-manipulation
# https://stackoverflow.com/questions/47981/how-do-you-set-clear-and-toggle-a-single-bit?rq=1
# just search "bit hacks", "bit manipulations"
