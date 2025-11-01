def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def siftDown(arr, i, upper):
    while True:
        leftIndex = 2*i + 1
        rightIndex = 2*i + 2

        if max(leftIndex, rightIndex) < upper:
            if arr[i] >= max(arr[leftIndex], arr[rightIndex]): break
            elif arr[leftIndex] > arr[rightIndex]:
                swap(arr, leftIndex, i)
                i = leftIndex
            else:
                swap(arr, rightIndex, i)
                i = rightIndex

        elif leftIndex < upper:
            if arr[leftIndex] > arr[i]:
                swap(arr, leftIndex, i)
                i = leftIndex
            else: break

        elif rightIndex < upper:
            if arr[rightIndex] > arr[i]:
                swap(arr, rightIndex, i)
                i = rightIndex
            else: break

        else: break


def heapsort(arr):
    lenArr = len(arr)

    for i in range((lenArr - 2) // 2, -1, -1):
        siftDown(arr, i, lenArr)
    
    for j in range(lenArr - 1, 0, -1):
        swap(arr, 0, j)
        siftDown(arr, 0, j)
    
    return arr


arr = [234, 235, 24, 1, 674, -4, 6]
print(arr)
print(heapsort(arr))




