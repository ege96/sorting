def quick_sort(array: list[int]) -> None:
    _quick_sort(array, 0, len(array)-1)


def _quick_sort(array: list[int], start: int, end: int) -> None:
    if start >= end:
        return
    pivot = _partition(array, start, end)
    _quick_sort(array, start, pivot-1)
    _quick_sort(array, pivot+1, end)


def _partition(array: list[int], start: int, end: int) -> int:
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i
