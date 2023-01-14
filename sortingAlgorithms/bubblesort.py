def bubble_sort(array: list[int]) -> None:
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def bubble_sort_optimized(array: list[int]) -> None:
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            return
