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



