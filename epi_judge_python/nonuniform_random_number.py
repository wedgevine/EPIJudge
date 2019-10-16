import collections
import functools
import math
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook

# consider drop a needle to [0, 1), each probability represent a line segment
# longer line segment has bigger chance to be punched by the needle
def first(values, probabilities):

    p = random.uniform(0, 1)
    size = len(values)
    s = 0

    for i in range(size):
        s += probabilities[i]
        if p < s:
            return values[i]

def nonuniform_random_number_generation(values, probabilities):
    return first(values, probabilities)


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda : [nonuniform_random_number_generation(values, probabilities) for _ in range(N)])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "nonuniform_random_number.py", 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
