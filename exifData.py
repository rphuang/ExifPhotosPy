#!/usr/bin/python3
# File name   : exifData.py
# Description : exif data class

import exifread
from config import Config

class Exifdata():
    """ encapsulate the EXIF data by using a standard tag keys (and displayable) regardless where the section is stored """
    def __init__(self, mappingFile = None):
        self.tags = {}
        self.mapping = {}
        if mappingFile is not None:
            self.addMapping(mappingFile)

    def getExifdata(self, filePath):
        """ get exif metadata from a file """
        self.tags.clear()
        f=open(filePath, 'rb')
        tags=exifread.process_file(f, details=True)
        for key, value in tags.items():
            if key in self.mapping:
                self.tags[self.mapping[key]] = value
        f.close()

    def getValue(self, key):
        """ get the exif data value """
        return self.tags[key]

    def hasKey(self, key):
        """ check a key exists in the  """
        return key in self.tags

    def addMapping(self, filePath):
        """ add tag mappings from file. the format of each mapping is: 'tag key = tag name in exifread'. Examples:
        Image Width=EXIF ExifImageWidth
        Lens Model=MakerNote LensType
        """
        settings = Config(filePath, autoSave = False).settings
        for key, value in settings.items():
            self.mapping[value] = key

