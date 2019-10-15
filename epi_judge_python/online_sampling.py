import functools
import itertools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

# need to familar with how to deal with stream with itertools
def first(stream, k):

    # Stores the first k elements.
    running_sample = list(itertools.islice(stream, k))
    current_list_len = k

    for i in stream:
        current_list_len += 1
        p = random.randrange(0, current_list_len)
        if p < k:
            running_sample[p] = i
    
    return running_sample

# Assumption: there are at least k elements in the stream.
def online_random_sample(stream, k):
    return first(stream, k)


@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(lambda : [online_random_sample(iter(stream), k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0)
             for result in results], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_sampling.py",
                                       "online_sampling.tsv",
                                       online_random_sample_wrapper))
