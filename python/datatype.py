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

# float
#%% 
# float() function
print(float(True))
print(float(False))
print(float(123))
print(float('-12.34'))

# string
# a sequence, sequence of characters 
# strings are immutable, why?
# because in python, strings are considered as elemental as numbers
# like value 7 can't be changed anything else, string "seven" can't be changed
# 1. for efficiency, like if many varibles point to the same large string value, the same string value can be saved in memory only once
# 2. for convenience, string can be used as dictionary key, if a key has been changed, then the value will be lost

#%% 
# a string can be created with single or double quotes
'Snap'
"Crakle"
# why, because we want string containing quotes
print("he's been to there")
# three single/double quotes for multiple line strings
poem = '''this is line1
thisis line2
and 3'''
print(poem)
# empty strings
print('', "", '''''', """""")
# convert other data types to strings, str() function
print(str(123))
print(str(True), str(False))
# escape with \
print("a\tb\tc\nd\te\tf")
# combine with +, or just by having one after another
print("string1" + "string2")
print("string3" "string4")
print("string5", "string6")
# duplicate with *
print("he"*2 + "\t"*2 + "em...")
# extract character with [], specifying offset, 0, 1, 2, from start to right, -1, -2, from end to left
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
# letters[100] will generate exception, offset should less than length
# because strings are immutable, the following will generate exception
name = 'peter'
# name[0] = 'P'
# shoudl do like this
name = 'P' + name[1:]
print(name)
# or like this
print(name.replace('P', 'p'))
# slice to get substring, [start:end:step]  
print(letters[:])
print(letters[1:])
print(letters[:3])
print(letters[1:3])    
print(letters[0:-1:7])
print(letters[2:-2:7])
print(letters[-1::-1]) # step backward for negative step
print(letters[::-1])
print(letters[-50:50]) # slices are more forgiving for bad offsets
#%%
# len() function 
print(len(letters))
print(len(''))
# split() function, break s string into a list of smaller strings based on some seperator
todos = 'buy, cook, eat, wash'
todos.split(',')
todos.split()
# join() function, opposite of split, collapse a list of string into a single string
fruits = ['apple', 'grape', 'orange', 'strawberry']
print(','.join(fruits))
print('\t'.join(fruits))
# other functions
todos.startswith('buy')
todos.endswith('eat')
print(todos.find('a')) # find the first
print(todos.rfind('a')) # find the last
print(todos.count('a')) # how many times 'a' occurs
'a'.isalnum() # is the string a letter or number?
#%%
setup = 'a duck goes into a bar...'
setup.strip('.') # remove leading or trailing character
setup.capitalize()
setup.title()
setup.upper()
setup.lower()
setup.swapcase()
#%% alignment
setup.center(30)
setup.ljust(30)
setup.rjust(30)
#%% substitute and replace
setup = 'a duck goes into a bar...'
setup.replace('duck', 'marmoset')
setup.replace('a ', 'the ', 100)
#%%
# sequence data types
#%%
