import sys
import os


class ImageProcessor(object):
    """Image name-processing module for scheme n-(f/b).png"""

    def __init__(self):
        self.fronts = dict()
        self.backs = dict()

    def __frontsInsert(self, imageID: int, filename: str):
        if imageID not in self.fronts:
            self.fronts[imageID] = filename
        else:
            print("trying to insert multiple images with same number")
            exit()

    def __backsInsert(self, imageID: int, filename: str):
        if imageID not in self.backs:
            self.backs[imageID] = filename
        else:
            print("trying to insert multiple images with same number")
            exit()

    @staticmethod
    def getIntegerTag(fileName: str):
        result = fileName.split('-')
        return int(result[0])

    def __checkImageIntegerTagValidity(self):
        """make sure our dictionary key sets match"""
        front_keys = set(self.fronts.keys())
        back_keys = set(self.backs.keys())
        intersection = front_keys & back_keys
        if len(intersection) != len(front_keys):
            print("an image doesn't have a match")
        if len(intersection) != len(back_keys):
            print("an image doesn't have a match")

    def processImages(self, directoryName: str):
        for root, dirs, files in os.walk(directoryName):
            for file in files:
                if file.endswith("-f.png"):
                    self.__frontsInsert(self.getIntegerTag(file), file)
                elif file.endswith("-b.png"):
                    self.__backsInsert(self.getIntegerTag(file), file)
                else:
                    print("Image failed to meet naming scheme N-(f/b).png")
        self.__checkImageIntegerTagValidity()
