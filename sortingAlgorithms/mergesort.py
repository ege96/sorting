def merge_sort(array: list[int]) -> None:
    if len(array) <= 1:
        return
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def merge_sort_2(array: list[int]) -> None:
    _merge_sort_2(array, 0, len(array)-1)


def _merge_sort_2(array: list[int], start: int, end: int) -> None:
    if start >= end:
        return
    mid = (start + end) // 2
    _merge_sort_2(array, start, mid)
    _merge_sort_2(array, mid + 1, end)
    i = start
    j = mid + 1
    temp = []
    while i <= mid and j <= end:
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= mid:
        temp.append(array[i])
        i += 1
    while j <= end:
        temp.append(array[j])
        j += 1
    array[start:end+1] = temp


def merge_sort_bottom_up(array: list[int]) -> None:
    n = len(array)
    size = 1
    while size < n:
        for start in range(0, n, 2*size):
            midpoint = start + size - 1
            end = min(start + 2*size - 1, n-1)
            merge(array, start, midpoint, end)
        size *= 2


def merge(array: list[int], start: int, mid: int, end: int) -> None:
    left = array[start:mid+1]
    right = array[mid+1:end+1]
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
