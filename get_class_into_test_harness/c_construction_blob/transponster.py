from get_class_into_test_harness.what_does_chandler_even_do import StatisticalAnalysis
from get_class_into_test_harness.what_does_chandler_even_do import DataReconfiguration
from get_class_into_test_harness.c_construction_blob.transponsterings import StatisticalTransponsterings
from get_class_into_test_harness.c_construction_blob.transponsterings import DataTransponsterings
from get_class_into_test_harness.c_construction_blob.transponsterings import Results

class Transponster:

    def __init__(self, analysis: StatisticalAnalysis, reconfig: DataReconfiguration):
        self._analysis = analysis
        self._reconfig = reconfig
        self._stat_transponstering = StatisticalTransponsterings(analysis)
        self._data_transponstering = DataTransponsterings(reconfig)
        self._results = Results(self._stat_transponstering, self._data_transponstering)
        assert self._analysis is not None

    def do_stuff(self):
        return True