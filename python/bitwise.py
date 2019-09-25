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

#%% bitwise application

# ref
# http://h14s.p5r.org/2012/09/0x5f3759df.html
# https://www.quora.com/What-are-some-cool-bit-manipulation-tricks-hacks
# https://www.cs.cmu.edu/~guna/15-123S11/Lectures/Lecture19.pdf
# https://blog.logrocket.com/interesting-use-cases-for-javascript-bitwise-operators/
# What are the applications of bitwise operators, right shift and left shift?
# https://www.quora.com/What-is-the-use-or-benefit-of-bitwise-operators
# https://chess24.com/en/read/news/how-do-chess-engines-think
# bitsets to represent a chess board.
# https://www.reddit.com/r/learnprogramming/comments/8y7vdr/practical_uses_of_bitwise_operators/
# bitwise applications

#%% EPI chapter 4 summary
# many algos utilize a fact that any non-negative number can be represented
# by a series of power of 2, given this fact, also any non-negative number
# was represented internally as binary format, left shift << 1 equals multiple
# 2, right shift >> 1 equals floor divide by 2 and these bitwise ops are fast

# for any alogs, always try brute force algo first, get answer, then improve

# parity, divide and conquer, lookup table
# swap bit: know bitwise operation tricks, hacks, applications
# reverse bit: divide and conquer and lookup table
# closest int with same weight: prove the math assumption, using bit hacks to
#                               swap 2 bits
# primitive divide: bf is stepping by 1, then tried stepping by power of 2
#                   book solution is simple and elegent
# primitive multiply: only can use bitwise and comparision, need add help
#                     function, multiply is implemented by additinon
# x to the power of y: step by power of 2, third algo, natrual, elegent, fast
#                      bring the time complexity from N^2 to N
#                      which based on obeservation that any number can be
#                      represented by a sum of series of power of 2
# reverse digit: modular, floor divide, how to get LSB/MSB of a digit
# is number palindromic: same as above
# unifor ramdom number: based on a (0, 1) random function, based on any number
#                       can be represent by binary format
# rectangle intersection: think one dimention at a time, divide and conquer?
#                         sweep line algo?                         



# ref
# http://mathhelpforum.com/number-theory/123347-every-natural-number-sum-powers-2-a.html
# https://mathlesstraveled.com/2008/04/18/challenge-12-sums-of-powers-of-two/
# https://en.wikipedia.org/wiki/1_%2B_2_%2B_4_%2B_8_%2B_%E2%8B%AF