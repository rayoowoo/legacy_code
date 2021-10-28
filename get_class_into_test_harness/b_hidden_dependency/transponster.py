from get_class_into_test_harness.what_does_chandler_even_do import StatisticalAnalysis
from get_class_into_test_harness.what_does_chandler_even_do import DataReconfiguration

class Transponster:

    def __init__(self):
        self._analysis = StatisticalAnalysis([1, 2, 3, 4, 5])
        self._reconfig = DataReconfiguration()
        assert self._analysis is not None

    def do_stuff(self):
        return True