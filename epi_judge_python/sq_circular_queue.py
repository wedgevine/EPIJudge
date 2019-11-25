from test_framework import generic_test
from test_framework.test_failure import TestFailure


# from book, simpler
class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self.data = [None] * capacity
        self.count = self.head = self.tail = 0

    def size(self):
        return self.count

    def dequeue(self):
        if not self.count:
            raise IndexError('dequeue: empty queue')
    
        value = self.data[self.head]
        self.count -= 1
        self.head = (self.head + 1) % len(self.data)

        return value
    
    def enqueue(self, x):
        if self.count == len(self.data):
            self.data = self.data[self.head:] + self.data[:self.head]
            self.head, self.tail = 0, len(self.data)
            self.data += [None] * (len(self.data) * Queue.SCALE_FACTOR - len(self.data))

        self.data[self.tail] = x
        self.tail = (self.tail + 1) % len(self.data)
        self.count += 1



class Queue1:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [0] * capacity
        self._head = self._tail = -1

    def enqueue(self, x):
        # print('enqueue: ', self._data, x)
        if self.size() == self._capacity:
            if self._head > self._tail:
                self._data = self._data[self._head:] + self._data[:self._head] + [0] * self._capacity
            else:
                self._data = self._data + [0] * self._capacity
            self._head, self._tail = 0, self._capacity - 1
            self._capacity *= 2
        elif self.size() == 0:
            self._head = 0

        self._tail += 1
        if self._tail >= self._capacity:
            self._tail %= self._capacity
        self._data[self._tail] = x
        # print('enqueue: size {}, head {}, tail {}, cap {}'.format(self.size(), self._head, self._tail, self._capacity))

    def dequeue(self):
        # print('dequeue: ', self._data)
        if self.size() == 0:
            raise IndexError('dequeue(): empty queue')
        if self.size() == 1:
            v = self._data[self._head]
            self._head = self._tail = -1
        else:
            v = self._data[self._head]
            self._head += 1
            if self._head >= self._capacity:
                self._head %= self._capacity

        # print('dequeue: size {}, head {}, tail {}'.format(self.size(), self._head, self._tail))
        return v

    def size(self):
        head, tail = self._head, self._tail
        if tail == -1:
            return 0
        if tail < head:
            tail += self._capacity
        return tail - head + 1


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
