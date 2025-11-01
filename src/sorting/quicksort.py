def quicksort(arr):
    if len(arr) <= 1: return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


arr = [23, 24, 3456, 345, -1342536, 15, 213465276387, -34]
arr = quicksort(arr)
print(arr)
