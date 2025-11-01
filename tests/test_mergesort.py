from src.sorting.mergesort import mergesort


def testEmpty():
    assert mergesort([]) == []


def testOneElm():
    assert mergesort([1]) == [1]


def testNegativeElm():
    assert mergesort([-1, -2, -3]) == [-3, -2, -1]


def testLargeElm():
    assert mergesort([1000000000, 2000000000]) == [1000000000, 2000000000]


def testNone():
    assert mergesort(None) is None