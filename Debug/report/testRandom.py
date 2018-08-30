from Debug.report import module_sample
from Debug.report import module_shuffle
from Debug.report import suite1
import unittest

def suite():
    suiteSample =  module_sample.suite()
    suiteShuffle = module_shuffle.suite()
    suite_suite = suite1.suite()

    tuple_suite = (suiteSample,suiteShuffle,suite_suite)

    suite = unittest.TestSuite(tuple_suite) #(suiteShuffle,suiteSample)
    # suite = unittest.TestSuite((suite_suite))
    # suite.addTests(unittest.TestLoader().load)
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(module_sample.sampleTestCase))
    # suite.addTests(unittest.TestLoader().loadTestsFromModule(module_shuffle))
    return suite

if __name__ =="__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())