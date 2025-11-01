def mergesort(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]


arr = [1, 56, 34, 23, 78, 90, 12, -14256, -13]
mergesort(arr)

print(arr)
