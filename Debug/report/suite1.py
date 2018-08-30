from Debug.report import module_shuffle
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(module_shuffle.shuffleTestCase))

    return suite