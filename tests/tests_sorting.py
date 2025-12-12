import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.sorting.bubble_sort import bubble_sort
from src.sorting.heap_sort import heap_sort
from src.sorting.merge_sort import merge_sort
from src.sorting.quick_sort import quick_sort

import pytest

@pytest.mark.parametrize(
    ["n", "expected"], 
    [([0, 10, 8, 9, 3, 4], [0, 3, 4, 8, 9, 10]), 
     ([1, 5, 4, 3, 8, 7], [1, 3, 4, 5, 7, 8]), 
     ([10, -1, 8], [-1, 8, 10]), 
     ([], []), 
     ([1], [1]), 
     ([-1, -2, -3], [-3, -2, -1]),
     ([1000000000, 2000000000], [1000000000, 2000000000]),
     ]
)


@pytest.mark.parametrize(
    "algorithm",
    [bubble_sort, heap_sort, merge_sort, quick_sort]
)


def test_all_sorting_algorithms(algorithm, n, expected):
    assert algorithm(n) == expected
