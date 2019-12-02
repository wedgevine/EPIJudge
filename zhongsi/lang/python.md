## data type

### int
in python 3, int has no limit, has infinite precision, thus has infinite bits.
in case infinity is needed (for init comparison), there are float('inf'), float('-inf')
float('nan') can be used as initial value

* there are articles discussed about python integer object implementation
generally, int is implemented as an object, inside the object, there is an array
storing every digit of the int, the array length is only limited by memory of machine
https://rushter.com/blog/python-integer-implementation/
https://www.laurentluce.com/posts/python-integer-objects-implementation/

* there is a good explaination in SO, why is '1000000 in range(10000000)' so fast
https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3?rq=1
range() is an object, which has a 'contain' method, which can calculate if a number is
in the range, no need to scan through all numbers in the range

### ternary
<expression 1> if <condition> else <expression 2

### format function
```
print('value1 {}, value2 {}'.format(value1, value2))
```
### looping
Loop over a single list with a regular for-in:
```
for n in numbers:
    print(n)
```
Loop over multiple lists at the same time with zip:
```
for header, rows in zip(headers, columns):
    print("{}: {}".format(header, ", ".join(rows)))
```
Loop over a list while keeping track of indexes with enumerate:
```
for num, line in enumerate(lines):
    print("{0:03d}: {}".format(num, line))
```
https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

### container, iterable, iterator, generator and iteration tools: loop, list comprehension, map, filter, all
* containers are data structures that holding elements and support membership tests, like list, str, tuple, dict, set
* containers typically are iterable, many others are iterable as well, like file, socket (often for infinite source of data). 
  an iterable is any object that can return an iterator by calling iter() function for the iterable object
* iterator, a stateful helper object that will produce the next value when call next() function for it, it is a lazy value factory,
  only next() call will produce next value
* a generator is always an iterator, an elegent iterator, not like ordinary iterator object, which has init, next, iter methods,
  a generator is a function, without return value, but has a "yield" statement, the call to the generator function will return a generator
  then this generator could be used as an iterator
* besides generator function, a generator can also be a generator expression, with syntax like:
  (expression for item in list if condition)
  just like a list comprehension
* iteration tools such as loop, list comprehension, all, filter, map functions can work with these iterable objects
* specifically, steam objects are better to dealt as an iterable object, a lazy data factory

https://nvie.com/posts/iterators-vs-generators/

* PEP 8 style guide for For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
```
if not seq:
if seq:
```

### collections
#### namedtuple
https://dbader.org/blog/writing-clean-python-with-namedtuples  
*A good way to view them is to think that namedtuples are a 
memory-efficient shortcut to defining an immutable class in 
Python manually.*
```
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
```
https://stackoverflow.com/questions/40632750/whats-the-difference-between-enum-and-namedtuple
mentioned the benefits of namedtuple, which is used for many objects with same type. object
attributes can be accessed by name, instead of by index. point.x, vs point[0] 

#### deque
a generalization of stack and queue, deque, double-ended queue, support append/pop for either side of the deque with O(1) performance.  
* append() add to right side
* pop() remove from right side
* appendleft() add to the left side
* popleft() remove from left side

#### itertools module
* itertools.groupby(iterable, key=None), sort data first  
  https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
  ```
  groups = []
  uniquekeys = []
  data = sorted(data, key=keyfunc)
  for k, g in groupby(data, keyfunc):
      groups.append(list(g))      # Store group iterator as a list
      uniquekeys.append(k)
  ```


### lambda
https://realpython.com/python-lambda/
just amonymous function

### function
#### all
example, to check if an array a is palindromic:  
```  
return all(a[i] == a[-i] for i in range(len(a) // 2))
```
function all() takes a single parameter with iterable type, 
the above generator expression is a generator, which
is always an iterator and an iterator is always an iterable objec

#### reduce
import functools
functools.reduce(
    lambda x, ele: x + ele,
    iterable,
    init_value
)
like:
x = init_value
for ele in iterable:
    x += ele

#### f function
https://realpython.com/python-f-strings/

### class
```
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
```
to make sure two variables are referring to the same object, using "is", for reference equality testing
```
f1 = Foo()
f2 = Foo()
print f1 is f2
```