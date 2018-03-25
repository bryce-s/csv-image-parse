import sys
import csv
import os
import random
# ADTs folow:
from classes.ImageProcessor import ImageProcessor


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


main()
