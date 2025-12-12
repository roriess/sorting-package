def bubble_sort(arr):
    if arr is None: return None

    len_arr = len(arr)

    res = arr

    for i in range(1, len_arr):
        flag = 0
        for j in range(0, len_arr - i):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                flag = 1

        if flag == 0: break

    return res
