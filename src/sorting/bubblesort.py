def bubblesort(arr):
    lenArr = len(arr)

    for i in range(1, lenArr):
        flag = 0
        for j in range(0, lenArr - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1

        if flag == 0: break