import unittest
import sys
# add from symbolic link
from classes.ImageProcessor import ImageProcessor


class TestImageProcessor(unittest.TestCase):
    
    basicTestDir = "../tests/basic/input"

    def test_init(self):
        self.processor = ImageProcessor()
        assert(self.processor)
        print("init passed")

    def test_insert(self):
        """tests basic insert behavior. This depends on tests/basic.."""
        self.processor = ImageProcessor()
        self.processor.processImages(self.basicTestDir)
        result = self.processor.getFrontsStringName(1)
        assert(result == "1-f.png")
        assert(self.processor.getBacksStringName(3) == "3-b.png")
        assert(self.processor.getFrontsStringName(3) == "3-f.png")
        assert(self.processor.getBacksStringName(1) == "1-b.png")
        print("insert passed")
    
    def test_getIntegerTag(self):
        assert(ImageProcessor.getIntegerTag("1-f.png") == 1)
        assert(ImageProcessor.getIntegerTag("124-b.png") == 124)
    
    def test_getAllNumbers(self):
        processor = ImageProcessor()
        processor.processImages(self.basicTestDir)
        processor.processImages("")
        nums = processor.getAllNumbers()
        i = int(1)
        for number in nums:
            assert(i == number)
            i = i + 1

if __name__ == '__main__':
    unittest.main()
