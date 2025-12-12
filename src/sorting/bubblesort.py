def bubblesort(arr):
    if arr is None: return None

    len_arr = len(arr)

    for i in range(1, len_arr):
        flag = 0
        for j in range(0, len_arr - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1

        if flag == 0: break

    return arr
