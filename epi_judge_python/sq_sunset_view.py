from test_framework import generic_test
from collections import namedtuple

# from book, using NamedTuple
def second(sequence):
    BuildingWithHeight = namedtuple('BuildingWithHeight', ('id', 'height'))
    candidates = []

    for k, v in enumerate(sequence):
        while candidates and v >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(k, v))
        
    return [candidate.id for candidate in reversed(candidates)]

def first(sequence):
    result = []
    for k, v in enumerate(sequence):
        while result and v >= sequence[result[-1]]:
            result.pop()
        result.append(k)

    result.reverse()
    return result

def examine_buildings_with_sunset(sequence):
    # return first(sequence)
    return second(sequence)


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
