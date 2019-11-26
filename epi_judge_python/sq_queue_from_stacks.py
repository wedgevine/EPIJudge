from test_framework import generic_test

class Queue:
    def __init__(self):
        self._enque, self._deque = [], []

    def enqueue(self, x):
        self._enque.append(x)

    def dequeue(self):
        if not self._deque:
            while self._enque:
                self._deque.append(self._enque.pop())
        
        if not self._deque:
            raise IndexError('dequeue: empty queue')
        
        return self._deque.pop()

class Queue1:
    def __init__(self):
        self._enque = []
        self._deque = []

    def enqueue(self, x):
        self._enque.append(x)

    def dequeue(self):
        self._deque.clear()
        while self._enque:
            self._deque.append(self._enque.pop())
        if self._deque:
            v = self._deque.pop()
            while self._deque:
                self._enque.append(self._deque.pop())
            return v

        raise IndexError('dequeue: empty queue')

def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
