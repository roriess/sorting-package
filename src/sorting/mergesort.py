def merge_sort(arr):
    if len(arr) <= 1: 
        return arr
    
    mid = len(arr) // 2

    first_part = arr[:mid]
    second_part = arr[mid:]

    first_part = merge_sort(first_part)
    second_part = merge_sort(second_part)

    return merge(first_part, second_part)

def merge(first, second):
    merged = []
    while first and second:
        if first[0] > second[0]:
            merged.append(second.pop(0))
        else:
            merged.append(first.pop(0))
    merged.extend(first or second)
