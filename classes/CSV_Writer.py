import sys
import csv
import os
import uuid
from classes.ImageProcessor import ImageProcessor


class CSV_Writer(object):
    """responsible for writing out the CSVs through processor interface"""

    def __init__(self, processor: ImageProcessor):
        self.imageProcess = processor
        self.lineNumbers = self.imageProcess.getAllNumbers()

    def generateImageName(self):
        front = str("<img src='")
        back = str("'>")
        tag = str(uuid.uuid4)
        return front + tag + back

    def writeCSV(self, outputDirectoryName):
        with open(outputDirectoryName + '/output.csv', 'rb') as csvFile:
            for number in self.lineNumbers:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(['<img src=213.png>', '<img src=2.png>'])
                # copy the original image, too..
