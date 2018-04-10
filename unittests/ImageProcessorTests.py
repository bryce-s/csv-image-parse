import unittest
import sys
# add from symbolic link
from classes.ImageProcessor import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    
    def test_init(self):
        self.processor = ImageProcessor()
        assert(self.processor)
        print("init passed")    
    
    def test_insert(self):
        """tests basic insert behavior"""
        self.processor = ImageProcessor()
        self.processor.processImages("../tests/basic/input")
        assert(self.processor.getFrontsStringName(1) == "1-f.png")
        assert(self.processor.getBacksStringName(3) == "3-b.png")
        assert(self.processor.getFrontsStringName(3) == "3-f.png")
        assert(self.processor.getBacksStringName(1) == "1-b.png")
        print("insert passed")


if __name__ == '__main__':
    unittest.main()
