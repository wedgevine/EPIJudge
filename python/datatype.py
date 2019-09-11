# https://docs.python.org/3/index.html
# https://www.python.org/dev/peps/pep-0008/
# Getting Started with Python 
# https://docs.python-guide.org/
# Automate the Boring Stuff with Python 
# https://automatetheboringstuff.com/#toc
# digital ocean tutorial
# https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3
# Python 101 
# https://news.ycombinator.com/item?id=15932381
# Python Like You Mean It (PLYMI), lean, essential, with questions 
# https://www.pythonlikeyoumeanit.com/index.html
# books: learning python, python crash course, python tricks, 
#        introducing python, effective python

# book "introducing python" chapter 2 and chapter 3
# introduced basic types and container types
# book "learning python" 
# chapter 3 introduced module
# chapter 4 has a brief introduction to core data types
# python doc - built in types
# https://docs.python.org/dev/library/stdtypes.html#built-in-types


# primitive data types, boolean, integer, float, string
# in python, everything is implemented as an object
# the object has a type (class)
# type determine if an object can be changed (mutable) or is constant (immutable)
# python is strongly typed, meaning object type does not change
# type(thing) to get the type of a variable or a literal value
# variable, a name refer object, a reference
# variable name, letter, digit, underscore, can't start with a digit

###############################################################################

#%% integer
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

#%% bases
print(0b1) # binary
print(0o7) # octal
print(0xf) # hex
print(0x1f % 16)

#%% type conversion
# int() function
print(int(98.7))
print(int(True))
print(int(False))
print(int('-12'))
# print(int('98.7')) # will generate exception
print(1+2.0) # auto type conversion
# float() function
print(float(True))
print(float(False))
print(float(123))
print(float('-12.34'))

#%% boolean
print(type(True))
print(type(False))
print(isinstance(True, bool))
# operation
print(True and False)   # or use &
print(True or False)    # or use |
print(2 < 3)    
#%% boolean objects are integers
print(isinstance(True, int))
print(int(True))
print(int(False))
print(3*True + False)   # they can be used as numbers

#%% non-type, usually used as a placeholder, for comparison
print(None)
print(type(None))
# check if an object is non-type
a = 1
print(a is None)
b = None
print(b is not None)

###############################################################################

#%% 
# string
# a sequence, sequence of characters 
# strings are immutable, why?
# because in python, strings are considered as elemental as numbers
# like value 7 can't be changed anything else, string "seven" can't be changed
# 1. for efficiency, like if many varibles point to the same large string 
#    value, the same string value can be saved in memory only once
# 2. for convenience, string can be used as dictionary key, if a key has been 
#    changed, then the value will be lost

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
# extract character with [], specifying offset, 0, 1, 2, from start to right, 
# -1, -2, from end to left
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
# split() function, break s string into a list of smaller strings based on some
# seperator
todos = 'buy, cook, eat, wash'
todos.split(',')
todos.split()
# join() function, opposite of split, collapse a list of string into a single 
# string
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

###############################################################################

#%% sequence
# sequence of items, list, tuple, string, all are ordered set
# item/element of list/tuple/string are ordered in sequence
# they share common interface for inspect, retrieve, summarize 
# list: most expensive and versatile, item could be any object, mutable
#       list item can be inserted, updated and deleted
# tuple: item could be any object, immutable
# string: sequence of unicode character, immutable
# reference
# https://docs.python.org/3/library/stdtypes.html#sequence-types-str-bytes-bytearray-list-tuple-range
# https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html
# http://buildingskills.itmaybeahack.com/book/python-2.6/html/p02/p02c01_sequences.html
# http://www.openbookproject.net/books/bpp4awd/ch03.html

# creation and conversion
l = ['a', 'list', 0, True, None, 3.14]
empty_list = []
empty_list_2 = list()
t = ('a', 'tuple', False, 123)
empty_tuple = ()
empty_tuple_2 = tuple()
single_tuple = "this is a tuple",   # the trailing comma means it is a tuple
                                    # not a string
s = "this is a string"
empty_string = ""
empty_string_2 = str()
print(l, empty_list, empty_list_2)
print(t, empty_tuple, empty_tuple_2, single_tuple)
print(s, empty_string, empty_string_2)
# list() convert other data types to list
print(list("cat"))
print(list(('a', 'tuple', 1, False)))
# string.split() function can split a string into a list
print('1/2/2009'.split('/'))
# tuple() convert other data types to tuple
print(tuple(["this", 'is', 'a', 'list']))
# str() convert other data types to string
print(str(1), str(True), str(1.0e4))

#%% list is mutable, tuple and string are immutable
l = [1, 2, 3]
l[0] = 100
print(l)
del l[1]
print(l)
t = (1, 2, 3)
# the following generate error
# TypeError: 'tuple' object does not support item assignment
# t[0] = 100
# error "TypeError: 'tuple' object doesn't support item deletion"
# del t[2]    
s = "this is a string"
# this following generates error
# TypeError: 'str' object does not support item assignment
# s[1] = "x"
# error "TypeError: 'str' object doesn't support item deletion"
# del s[1]

#%% concatenation and repeatation
weekday = ['Monday', 'Tuesday', 'Wendsday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
week = weekday + weekend
print(week)
breakfast = ('milk', 'bread')
lunch = ('hotdog',)
dinner = ('steak',)
day_menu = breakfast + lunch + dinner
print(day_menu)
first_name = 'tom'
last_name = 'hanks'
full_name = first_name + ' ' + last_name
print(full_name)
print([1]*3, (1,)*3, '1'*3)

#%% in for checking if an item is in sequence
# membership checking
words = ['a', 'deer', 'a', 'female', 'deer']
print('deer' in words)
x = (1, 3, 5)   
print(2 not in x)
print("cat" in "cat in the hat")

#%% get an item by offset, zero-based indexing system
words = ['a', 'deer', 'a', 'female', 'deer']
print(words[0], words[1], words[2]) 
# negative index counts backward from the end
print(words[-1], words[-2], words[-3])
# the offset has to be valid
# the following generate error
# IndexError: list index out of range
# print(words[5], words[-5])  
x = (1, 3, 5)   
print(x[0], x[1], x[2]) 
print(x[-1], x[-2], x[-3]) 
s = 'cat in the hat'
print(s[0], s[1], s[2]) 
print(s[-1], s[-2], s[-3]) 

#%% splice, get sub sequence by offset range, [start:end:step]
words = ['a', 'deer', 'a', 'female', 'deer']
print(words[0:3], words[::2])
print(words[::-2])      # start from end and go left by 2
print(words[::-1])      # the trick to reverse a list
print(words[-50:50])    # slices are more forgiving for bad offsets
x = (1, 3, 5, 7)
print(x[0:3], x[::2])
print(x[::-2])
print(x[::-1])
print(x[-50:50])
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[1:])
print(letters[:3])
print(letters[1:3])    
print(letters[0:-1:7])
print(letters[2:-2:7])
print(letters[-1::-1]) # step backward for negative step
print(letters[::-1])
print(letters[-50:50]) # slices are more forgiving for bad offsets

#%% functions
# asking for the number of members in a sequence: len(seq)
words = ['a', 'deer', 'a', 'female', 'deer']
x = (1, 3, 5, 7)
letters = 'abcdefghijklmnopqrstuvwxyz'
print(len(words), len(x), len(letters))
print(len([]), len(()), len(""))
# getting the index of the first occurrence of x in a sequence: seq.index(x)
print(words.index('deer'), x.index(3), letters.index('x'))
# counting the number of occurrences of x in a sequence: seq.count(x)
print(words.count('a'), x.count(3), letters.count('x'))

#%% list functions
words = ['a', 'deer', 'a', 'female', 'deer']
# append object to end
words.append("123")
print(words)
# extend list by ppending elements from he iterable
words.extend(['1', '2', '3'])
print(words)
# or +=
words += ['hello', 'world']
print(words)
# insert object before index
words.insert(3, 'inserted string')
print(words)
# remove first occurrence of value
words.remove("1")
print(words)
# error "ValueError: list.remove(x): x not in list"
# words.remove("100")
# remove and return item at index (default last)    
word3 = words.pop(3)
word0 = words.pop(0)
word_last = words.pop()
print(word3, word0, word_last)
# append(), pop(): LIFO queue, stack
# append(), pop(0): FIFO queue
# stable sort "in place"
numbers = [1, 9, 47, 2]
numbers.sort()
print(numbers)
# reverse "in place"
numbers.reverse()
print(numbers)
# function sorted return a sorted copy of the list
sorted_numbers = sorted(numbers)
print(sorted_numbers)
# to sort descending
sorted_numbers.sort(reverse=True)
print(sorted_numbers)
# to get a fresh list from an existing list
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
print(a, b, c, d)

###############################################################################

#%% dictionary
# dictionary and set, like sequence, are collection of objects
# unlike sequence, the order of objects doesn't matter
# objects in dictionary are not selected by positiion/index/offset
# they are selected by keys, key could be any immutable type:
# string, integer, float, tuple, boolean, ...
# dictionary is mutable

empty_dict = {}
menu = {
    "food": "apple",
    "count": 1,
    "color": "red",
    # in python, it is okay to leave a comma after the last item in list, 
    # tuple and dictionary
}
print(empty_dict)
print(menu)

# dict() to convert 2 value sequence into dictionary
lol = [[1, 2], [3, 4], [5, 6]]
print(dict(lol))
# could be any 2 item sequence
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))
tos = ('a1', 'b2', 'c3')
print(dict(tos))

#%% add or change value by [key]
menu = {
    "breakfast": "bread",
    "lunch": "apple",
}
menu["dinner"] = "meat"
print(menu)

# combine dictionaries with update
snak = { "snak": "cookie" }
menu.update(snak)
print(menu)

# delete item by key with del
del menu["lunch"]
print(menu)

# delete all items by using clear
menu.clear()
print(menu)

# like sequence, test for a key by using in
d = { "a": 1, "x": 0 }
print("a" in d, "x" not in d) 

# get an item by [key]
print(d["a"])
# print(d["b"]) with KeyError: 'b'
# to avoid this, either check with in or use get
print(d.get("a", "000"), d.get("b", 123))

# get all keys with keys()
print(d.keys()) # returns dict_keys, an iterable
# get all values with values()
print(d.values()) 
# get all key-value pair with items()
print(d.items())    
# assign with =, copy with copy()
e = d.copy()
d["a"] = 100
print(e, d)

###############################################################################

#%% set
# like a dictionary, only with unique keys, no associated value for the keys
# use a set if only want to know something exists
# use a dictionary if want to attach some information to the key as a value
# like dictionary, sets are unordered

empty_set = set()
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7}  

# convert from other data types with set()
# from sequence, dictionary
print(set("letters"))       # note, duplicated elements are removed
print(set([1, 2, 3, 4, 5])) # from a list
print(set({"a":1, "b":2}))  # from dictionary, only the keys

# test with in
print(2 in odd_numbers)

# set operations
print(even_numbers & odd_numbers)   # intersection
print(even_numbers | odd_numbers)   # union
print(even_numbers - odd_numbers)   # difference, ele in first, not in second
print(even_numbers.difference(odd_numbers)) # same as above
print(even_numbers ^ odd_numbers)   # exclusive, element in first or second
                                    # but not in both
print(even_numbers <= odd_numbers)  # check if first is subset of second
print(even_numbers.issubset(odd_numbers))   
print(even_numbers <= even_numbers)
print(even_numbers < even_numbers)  # < to check proper subset
# correspondingly, >=, >, issuperset for superset

###############################################################################

# basic types, sequence types, dictionary, set can be nested to make bigger
# data structures

# sequence (list, tuple, string), dictionary, set, all these types are
# some collection of objects, container types, they have some commons
# 1. they need to be created, either with class or some literal
# 2. they can be converted from other types
# 3. they are either mutable or immutable, for mutable types, item can be
#    inserted, updated, deleted
# 4. they provide some way to get the item, index for sequence and key for dic
# 5. they provide some way to test if an item is in the collection
# 6. they provide some way to get part of the collection, like slice, all keys
# 7. they provide some common method to process items in the collection,
#    like, len(), sum(), max(), min()
# 8. they provide type specific methods, like string.upper(), list.sort()
#    and set operations
# 9. they have different internal implementation, application for different
#    cases: queue, stack, hash, set, ...

# most imporatntly, these container types are iterable objects, meaning
# they can return a iterator object, which has a next() function 
# iteration tools such as loop (for, while), map, filter function, 
# list comprehension can call the next() function to get item of the
# container one by one until a StopIteration exception was raised

# a good article https://nvie.com/posts/iterators-vs-generators/
# and followed https://nvie.com/posts/use-more-iterators/

###############################################################################

#%% iterable packing and unpacking
# https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
# http://openbookproject.net/thinkcs/python/english3e/tuples.html
# https://stackoverflow.com/questions/2238355/what-is-the-pythonic-way-to-unpack-tuples
# https://wsvincent.com/python-tuple-unpacking/
# https://chrisalbon.com/python/basics/unpacking_a_tuple/

