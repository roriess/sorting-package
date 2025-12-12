def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sift_down(arr, i, upper):
    while True:
        left_index = 2*i + 1
        right_index = 2*i + 2

        if max(left_index, right_index) < upper:
            if arr[i] >= max(arr[left_index], arr[right_index]): break
            elif arr[left_index] > arr[right_index]:
                swap(arr, left_index, i)
                i = left_index
            else:
                swap(arr, right_index, i)
                i = right_index

        elif left_index < upper:
            if arr[left_index] > arr[i]:
                swap(arr, left_index, i)
                i = left_index
            else: break

        elif right_index < upper:
            if arr[right_index] > arr[i]:
                swap(arr, right_index, i)
                i = right_index
            else: break

        else: break


def heapsort(arr):
    if arr is None: 
        return None
    
    res = arr
    len_arr = len(arr)

    for i in range((len_arr - 2) // 2, -1, -1):
        sift_down(res, i, len_arr)
    
    for j in range(len_arr - 1, 0, -1):
        swap(res, 0, j)
        sift_down(res, 0, j)

    return res
