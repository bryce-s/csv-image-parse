import sys
import csv
import os
import uuid
import shutil
from classes.ImageProcessor import ImageProcessor


class CSV_Writer(object):
    """responsible for writing out the CSVs through processor interface"""

    def __init__(self, processor: ImageProcessor):
        self.imageProcess = processor
        self.lineNumbers = self.imageProcess.getAllNumbers()

    def combineToHTML_Tag(self, tag: str):
        front = str("<img src='")
        back = str("'>")
        return front + tag + back

    def generateRandomImageString(self):
        """returns a random string for the image-name"""
        return str(uuid.uuid4)

    def writeCSV(self, outputDirectoryName, inputDirectoryName):
        """takes filenames from input dir adt, copies to output dir, renames, and
           logs in csv file"""
        if not os.path.exists(outputDirectoryName):
            os.makedirs(outputDirectoryName)
        with open(outputDirectoryName + '/output.csv', 'rb') as csvFile:
            writer = csv.writer(csvFile, delimiter=',')
            for number in self.lineNumbers:
                frontString = self.imageProcess.getFrontsStringName(number)
                backString = self.imageProcess.getBacksStringName(number)
                shutil.copy2(
                    inputDirectoryName + '/' + frontString,
                    outputDirectoryName)
                shutil.copy2(
                    inputDirectoryName + '/' + backString,
                    outputDirectoryName)
                frontStringRandomized = self.generateRandomImageString()
                backStringRandomized = self.generateRandomImageString()
                os.rename(
                    outputDirectoryName + '/' + frontString,
                    frontStringRandomized + '.png')
                os.rename(
                    outputDirectoryName + '/' + backString,
                    backStringRandomized + 'png')

                writer.writerow(
                    self.combineToHTML_Tag(frontStringRandomized),
                    self.combineToHTML_Tag(backStringRandomized))
                # copy the original image, too..
