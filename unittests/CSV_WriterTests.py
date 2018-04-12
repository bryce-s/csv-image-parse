import unittest
import sys
from classes.CSV_Writer import CSV_Writer
from classes.ImageProcessor import ImageProcessor

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

if __name__ == '__main__':
    unittest.main()
