from get_class_into_test_harness.what_does_chandler_even_do import StatisticalAnalysis
from get_class_into_test_harness.what_does_chandler_even_do import DataReconfiguration
from get_class_into_test_harness.d_global_dependency.transponsterings import StatisticalTransponsterings
from get_class_into_test_harness.d_global_dependency.transponsterings import DataTransponsterings
from get_class_into_test_harness.d_global_dependency.transponsterings import Results
from get_class_into_test_harness.d_global_dependency.transponsterings import ChandlersJob

class Transponster:

    def __init__(self, analysis: StatisticalAnalysis, reconfig: DataReconfiguration):
        self.start_job()
        self._analysis = analysis
        self._reconfig = reconfig
        self._stat_transponstering = StatisticalTransponsterings(analysis)
        self._data_transponstering = DataTransponsterings(reconfig)
        self._results = Results(self._stat_transponstering, self._data_transponstering)
        result = self.should_chandler_switch_jobs()
        if result:
            self.switch_job()

    def start_job(self):
        job = ChandlersJob(name="statistical analysis and data reconfiguration")
        self.job = job

    def switch_job(self):
        self.job.change(name="junior copywriter")

    def should_chandler_switch_jobs(self):
        return self._results.compare()