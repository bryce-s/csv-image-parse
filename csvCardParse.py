import sys
import csv
import os
# ADTs folow:
from classes.ImageProcessor import ImageProcessor
from classes.CSV_Writer import CSV_Writer


def cliErrorChecking():
    if len(sys.argv) != 3:
        print("USAGE:  csvCardParse.py inputDir outputDir")
        exit()
    if not os.path.isdir(sys.argv[1]):
        print("Input dir not found.")


def main():
    cliErrorChecking()
    myProcessor = ImageProcessor()
    myProcessor.processImages(sys.argv[1])
    writer = CSV_Writer(myProcessor)
    writer.writeCSV(sys.argv[2], sys.argv[1])


main()
