import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

def third(n, k):

    moved = {}

    for i in range(k):
        chosen = random.randrange(i, n)
        current_value = moved.get(i, i)
        chosen_value = moved.get(chosen, chosen)
        moved[i] = chosen_value
        moved[chosen] = current_value

    return [moved[i] for i in range(k)]

# second is wrong, not considered for i in range(K)
# the i-th element could have been moved, so its value may not be i
# so the value variable maybe hold the wrong value
def second(n, k):

    moved = {}
    result = list(range(k))

    for i in range(k):
        chosen = random.randrange(i, n)
        value = result[i]
        result[i] = moved.get(chosen, chosen)
        # if chosen in moved:
        #     result[i] = moved[chosen]
        # else:
        #     result[i] = chosen
        moved[chosen] = value
        print(i, chosen, result, moved)

    return result

def first(n, k):

    p = list(range(n))
    for i in range(k):
        chosen = random.randrange(i, n)
        p[i], p[chosen] = p[chosen], p[i]

    return p[:k]

def random_subset(n, k):
    # return first(n, k)
    # return second(n, k)
    return third(n, k)


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0)
             for result in results], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("random_subset.py", 'random_subset.tsv',
                                       random_subset_wrapper))
