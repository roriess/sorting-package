from src.sorting.quicksort import quicksort


def testEmpty():
    assert quicksort([]) == []


def testOneElm():
    assert quicksort([1]) == [1]


def testNegativeElm():
    assert quicksort([-1, -2, -3]) == [-3, -2, -1]


def testLargeElm():
    assert quicksort([1000000000, 2000000000]) == [1000000000, 2000000000]


def testNone():
    assert quicksort(None) is None