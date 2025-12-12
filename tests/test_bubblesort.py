from src.sorting.bubblesort import bubblesort


def test1():
   assert bubblesort([0, 10, 8, 9, 3, 4]) == [0, 3, 4, 8, 9, 10]


def test2():
   assert bubblesort([1, 5, 4, 3, 8, 7]) == [1, 3, 4, 5, 7, 8]


def test3():
   assert bubblesort([10, -1, 8]) == [-1, 8, 10]


def test_empty():
    assert bubblesort([]) == []


def test_one_elm():
    assert bubblesort([1]) == [1]


def test_negative_elm():
    assert bubblesort([-1, -2, -3]) == [-3, -2, -1]


def test_large_elm():
    assert bubblesort([1000000000, 2000000000]) == [1000000000, 2000000000]


def test_none():
    assert bubblesort(None) is None