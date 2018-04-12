import ImageProcessorTests
import CSV_WriterTests
import unittest
import sys

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def runTest(self):
        pass
        
def suite():
    """holds all tests for execution"""
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(ImageProcessorTests.TestImageProcessor))
    tests.addTest(unittest.makeSuite(CSV_WriterTests.TestCSV_Writer))
    return tests

testSuite = suite()
runner = unittest.TextTestRunner()
runner.run(testSuite)