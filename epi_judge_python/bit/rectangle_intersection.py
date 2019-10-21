import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    x, y, w, h = 0, 0, 0, 0

    if R1.x + R1.width >= R2.x and R2.x + R2.width >= R1.x:
        if R1.y + R1.height >= R2.y and R2.y + R2.height >= R1.y:
            x = max(R1.x, R2.x)
            y = max(R1.y, R2.y)
            w = min(R1.x + R1.width, R2.x + R2.width) - x
            h = min(R1.y + R1.height, R2.y + R2.height) - y
            return Rectangle(x, y, w, h)

    return Rectangle(0, 0, -1, -1)

def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
