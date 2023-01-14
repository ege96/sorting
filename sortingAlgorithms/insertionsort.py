def insertion_sort(array: list[int]) -> None:
    for i in range(1, len(array)):
        t = array[i]
        for j in range(i, -1, -1):
            if array[j-1] > t:
                array[j] = array[j-1]
            else:
                break
        array[j] = t


def insertion_sort_2(array: list[int]) -> None:
    for i in range(1, len(array)):
        t = array[i]
        j = i
        while j > 0 and t < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = t


def insertion_sort_3(array: list[int]) -> None:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break


def insertion_sort_4(array: list[int]) -> None:
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
