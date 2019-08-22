# https://docs.python.org/3/index.html
# https://www.python.org/dev/peps/pep-0008/
# Getting Started with Python https://docs.python-guide.org/
# Automate the Boring Stuff with Python https://automatetheboringstuff.com/#toc
# https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3
# Python 101 https://news.ycombinator.com/item?id=15932381
# books: learning python, python crash course, python tricks, introducing python, effective python

# primitive data types, boolean, integer, float, string
# in python, everything is implemented as an object
# the object has a type (class)
# type determine if an object can be changed (mutable) or is constant (immutable)
# python is strongly typed, meaning object type does not change
# type(thing) to get the type of a variable or a literal value
# variable, a name refer object, a reference
# variable name, letter, digit, underscore, can't start with a digit

# integer
#%%
print(9 / 5)
print(9 / 3)
print(9 // 5)
print(9 % 5)
print(divmod(9, 5))

a = 5
a /= 3
print(a)

# python3 can handle any length integer
googol = 10**100
print(googol)
print(googol * googol)
#%%
# bases
print(0b1) # binary
print(0o7) # octal
print(0xf) # hex
print(0x1f % 16)
#%%
# type conversion
# int() function
print(int(98.7))
print(int(True))
print(int(False))
print(int('-12'))
# print(int('98.7')) # will generate exception
print(1+2.0) # auto type conversion

#%% float
# float() function
print(float(True))
print(float(False))
print(float(123))
print(float('-12.34'))

#%% string

#%%
# sequence data types
#%%
