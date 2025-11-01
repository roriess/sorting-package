from src.sorting.mergesort import mergesort


def test1():
   assert mergesort([0, 10, 8, 9, 3, 4]) == [0, 3, 4, 8, 9, 10]


def test2():
   assert mergesort([1, 5, 4, 3, 8, 7]) == [1, 3, 4, 5, 7, 8]


def test3():
   assert mergesort([10, -1, 8]) == [-1, 8, 10]


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