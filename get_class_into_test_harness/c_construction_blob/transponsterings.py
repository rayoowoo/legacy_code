from get_class_into_test_harness.what_does_chandler_even_do import DataReconfiguration
from get_class_into_test_harness.what_does_chandler_even_do import StatisticalAnalysis

class StatisticalTransponsterings:
    def __init__(self, analysis):
        self._analysis = analysis

    def analyze(self):
        return self._analysis.get_result()


class DataTransponsterings:
    def __init__(self, reconfig):
        self._reconfig = reconfig

    def reconfigure(self):
        self._reconfig.reconfigure()
        return self._reconfig


class Results:
    def __init__(self, stat_transponstering, data_transponstering):
        self._stat_transponstering = stat_transponstering
        self._data_transponstering = data_transponstering

    def compare(self):
        return self._stat_transponstering == self._data_transponstering