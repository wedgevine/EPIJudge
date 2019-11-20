from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple


class Stack1:

    # class variable shared by all instance of the class
    ElementWithCachedMax = namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max()))
        )

class Stack:

    # MaxCount = namedtuple('MaxCount', ('value', 'count'))
    class MaxCount:
        def __init__(self, value):
            self.value = value
            self.count = 1
        def get_value(self):
            return self.value
        def get_count(self):
            return self.count
        def increase_count(self):
            self.count += 1
        def decrease_count(self):
            self.count -= 1

    def __init__(self):
        self._elements = []
        self._max_list = []
    
    def empty(self):
        return len(self._elements) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._max_list[-1].get_value()

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        self._max_list[-1].decrease_count()
        if self._max_list[-1].get_count() == 0:
            self._max_list.pop()
        return self._elements.pop()
    
    def push(self, x):
        if self.empty() or x > self._max_list[-1].get_value():
            # self._max_list.append(self.MaxCount(x, 1))
            self._max_list.append(self.MaxCount(x))
        else:
            self._max_list[-1].increase_count()
        self._elements.append(x)

def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
