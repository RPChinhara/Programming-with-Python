import abc

class Sort(abc.ABC):
    @abc.abstractmethod
    def sort(self):
        pass

class SelectionSort(Sort):
    def __init__(self, arr):
        self.array = arr

    def sort(self):
        size = len(self.array)
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
                if self.array[i] < self.array[min_idx]:
                    min_idx = i
            (self.array[step], self.array[min_idx]) = (self.array[min_idx], self.array[step])

data = [-2, 45, 0, 11, -9]
sorted_data = SelectionSort(data)
sorted_data.sort()
print(sorted_data.array)