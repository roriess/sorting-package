from src.sorting.heapsort import heapsort


def test1():
   assert heapsort([0, 10, 8, 9, 3, 4]) == [0, 3, 4, 8, 9, 10]


def test2():
   assert heapsort([1, 5, 4, 3, 8, 7]) == [1, 3, 4, 5, 7, 8]


def test3():
   assert heapsort([10, -1, 8]) == [-1, 8, 10]


def test_empty():
    assert heapsort([]) == []


def test_one_elm():
    assert heapsort([1]) == [1]


def test_negative_elm():
    assert heapsort([-1, -2, -3]) == [-3, -2, -1]


def test_large_elm():
    assert heapsort([1000000000, 2000000000]) == [1000000000, 2000000000]


def test_none():
    assert heapsort(None) is None