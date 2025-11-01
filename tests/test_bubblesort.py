from src.sorting.bubblesort import bubblesort


def testEmpty():
    assert bubblesort([]) == []


def testOneElm():
    assert bubblesort([1]) == [1]


def testNegativeElm():
    assert bubblesort([-1, -2, -3]) == [-3, -2, -1]


def testLargeElm():
    assert bubblesort([1000000000, 2000000000]) == [1000000000, 2000000000]


def testNone():
    assert bubblesort(None) is None