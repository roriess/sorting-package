# tests/tests_sorting.py
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.sorting.bubblesort import bubblesort
from src.sorting.heapsort import heapsort
from src.sorting.mergesort import mergesort
from src.sorting.quicksort import quicksort

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
    [bubblesort, heapsort, mergesort, quicksort]
)


def test_all_sorting_algorithms(algorithm, n, expected):
    assert algorithm(n) == expected
