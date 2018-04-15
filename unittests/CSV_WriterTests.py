import unittest
import sys
from classes.CSV_Writer import CSV_Writer
from classes.ImageProcessor import ImageProcessor
import os
import shutil

class TestCSV_Writer(unittest.TestCase):
    
    basicTestDir = "../tests/basic/input"
    
    def setUp(self):
        """will be rerun on every test case"""
        self.processor = ImageProcessor()
        self.processor.processImages(self.basicTestDir)
        self.writer = CSV_Writer(self.processor)
    
    def test_generateString(self):
        """checks if string is generated"""
        assert(self.writer.generateRandomImageString())

    def test_combineHTML_Tag(self):
        assert(self.writer.combineToHTML_Tag("hi") == "<img src='hi'/>")

    def test_writeCSV(self):
        testOutputName = str("testOut")
        self.writer.writeCSV(testOutputName, self.basicTestDir)
        assert(os.path.isdir(testOutputName))
        shutil.rmtree(testOutputName)


if __name__ == '__main__':
    unittest.main()
