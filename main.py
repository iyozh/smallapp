import copy


def sort_with_bubble(lst):
    arr = copy.copy(lst)
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(sort_with_bubble([1, 6, 7, 23, 4, 6]))
