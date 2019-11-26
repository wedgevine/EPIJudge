from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class QueueWithMax:
    def __init__(self):
        self._data = deque()
        self._max = deque()

    def enqueue(self, x):
        self._data.append(x)

        while self._max:
            if self._max[-1] >= x:
                break
            self._max.pop()
            
        # can't modify the deque when iterating it
        # for i in reversed(self._max):
        #     if i < x:
        #         self._max.pop()
        self._max.append(x)
        
    def dequeue(self):
        if not self._data:
            raise IndexError('dequeue: empth queue')

        v = self._data.popleft()
        if v == self._max[0]:
            self._max.popleft()

        return v

    def max(self):
        if self._max:
            return self._max[0]
        raise IndexError('max: empty queue')

class QueueWithMax1:
    def __init__(self):
        self._data = deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
