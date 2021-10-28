from time import sleep

class StatisticalAnalysis:

    def __init__(self, stats):
        print("can this analysis BE any slower")
        sleep(10)
        self._stats = [1, 2, 3, 4, 5]

    def get_result(self):
        return self._stats

class DataReconfiguration:

    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def reconfigure(self):
        self._data = [5, 4, 3, 2, 1]

    def data(self):
        return self._data