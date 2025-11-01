from src.sorting.heapsort import heapsort

def testEmpty():
    assert heapsort([]) == []

def testOneElm():
    assert heapsort([1]) == [1]

def testNegativeElm():
    assert heapsort([-1, -2, -3]) == [-3, -2, -1]

def testLargeElm():
    assert heapsort([1000000000, 2000000000]) == [1000000000, 2000000000]


def testNone():
    assert heapsort(None) is None