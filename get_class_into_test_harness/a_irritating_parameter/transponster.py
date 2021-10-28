from get_class_into_test_harness.what_does_chandler_even_do import StatisticalAnalysis
from get_class_into_test_harness.what_does_chandler_even_do import DataReconfiguration

class Transponster:

    def __init__(self, analysis: StatisticalAnalysis, reconfig: DataReconfiguration):
        self._analysis = analysis
        self._reconfig = reconfig
        assert self._analysis is not None

    def do_stuff(self):
        return True