from typing import List
from get_class_into_test_harness.what_does_chandler_even_do import DataReconfiguration
from get_class_into_test_harness.what_does_chandler_even_do import StatisticalAnalysis
from get_class_into_test_harness.singleton import Singleton

class StatisticalTransponsterings:
    def __init__(self, analysis: StatisticalAnalysis):
        self._analysis = analysis

    def analyze(self):
        return self._analysis.get_result()


class DataTransponsterings:
    def __init__(self, reconfig: DataReconfiguration, should_reconfigure: bool = True):
        self._reconfig = reconfig
        self._should_reconfigure = should_reconfigure

    def reconfigure(self) -> List[int]:
        if self._should_reconfigure:
            self._reconfig.reconfigure()
        return self._reconfig


class Results:
    def __init__(self, stat_transponstering: StatisticalTransponsterings, data_transponstering: DataTransponsterings):
        self._stat_transponstering = stat_transponstering
        self._data_transponstering = data_transponstering

    def compare(self) -> bool:
        return self._stat_transponstering == self._data_transponstering


class ChandlersJob(metaclass=Singleton):
    def __init__(self, name: str):
        self.name = name

    def change(self, name: str):
        self.name = name