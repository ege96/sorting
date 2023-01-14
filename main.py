import sortingAlgorithms
from exceptions import *

import random
import time
from inspect import getmembers, isfunction


all_funcs = [func for func in getmembers(sortingAlgorithms) if isfunction(func[1])]


class Tester:
    all_sorting_functions = {i[0]: i[1] for i in all_funcs}

    def __init__(self, sort_function: str):
        self.array_size = 1000
        self.min_value = 0
        self.max_value = 100
        self.sort_function_name = sort_function
        self.sort_function = self.all_sorting_functions[sort_function]

    def test(self) -> float:
        array = self._generateRandomArray()
        start_time = time.perf_counter()
        self.sort_function(array)
        end_time = time.perf_counter()
        if self._isSorted(array):
            return end_time - start_time
        else:
            raise BadSortingAlgorithmError(
                f"YOUR {self.sort_function_name} ALGORITHM IS BAD")

    def setArraySize(self, array_size) -> None:
        self.array_size = array_size

    def getArraySize(self) -> int:
        return self.array_size

    def setMinValue(self, min_value) -> None:
        self.min_value = min_value

    def getMinValue(self) -> int:
        return self.min_value

    def setMaxValue(self, max_value) -> None:
        self.max_value = max_value

    def getMaxValue(self) -> int:
        return self.max_value

    def _generateRandomArray(self) -> list[int]:
        return [random.randint(self.min_value, self.max_value) for _ in range(self.array_size)]

    def _isSorted(self, array) -> bool:
        if len(array) in [0, 1]:
            return True

        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                return False
        return True


if __name__ == "__main__":

    allSorters = [i[0] for i in all_funcs]

    avgs = {}
    for sorter in allSorters:
        tester = Tester(sorter)
        times = []
        for _ in range(10):
            times.append(tester.test())
        avgs[sorter] = sum(times)/len(times)

    sortedAvgs = sorted(avgs.items(), key=lambda x: x[1])

    for i in sortedAvgs:
        name = i[0]
        avgValue = i[1]
        print(name.ljust(22), "|", round(avgValue, 5))
