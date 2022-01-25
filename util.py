#!/usr/bin/python3
# File name   : util.py
# Description : utility functions

import os
import tempfile
from PIL import Image

def getFiles(folder, fileList = [], fileType = None, includeSubfolder = False):
    """ get all the files in the folder. returns list of absolute file path. """
    fileTypeLower=fileType
    if fileTypeLower is not None:
        fileTypeLower=fileType.lower()
    for root, folders, files in os.walk(folder, topdown=True):
        for item in files:
            if fileTypeLower == None or fileTypeLower in item.lower():
                fileList.append(os.path.join(root, item))
        if not includeSubfolder:
            break

def copyFiles(sourceFolder, targetFolder, fileType = None, excludeList = None):
    """ copy all the files from sourceFolder to targetFolder for files with fileType (None - copy all) """
    for root, folders, files in os.walk(sourceFolder):
        print ('Copying folder: %s' %root)
        for item in files:
            if fileType == None or fileType in item:
                source = os.path.join(root, item)
                target = os.path.join(targetFolder, item)
                if os.path.exists(target):
                    pass
                elif isExcluded(item, excludeList):
                    pass
                else:
                    shutil.copy(source, target)

def transposeImage(path, exifdata):
    """ transpose the image if the exifdata's Orientation indicates and then return a temp file path """
    if not exifdata.hasKey('Orientation'):
        return path

    orientation = exifdata.getValue("Orientation")
    val = orientation.values
    if 3 in val:
        #logging.debug("Rotating by 180 degrees.")
        path = transposeAndSave(path, Image.ROTATE_180)
    elif 4 in val:
        #logging.debug("Mirroring horizontally.")
        path = transposeAndSave(path, Image.FLIP_TOP_BOTTOM)
    elif 6 in val:
        #logging.debug("Rotating by 270 degrees.")
        path = transposeAndSave(path, Image.ROTATE_270)
    elif 8 in val:
        #logging.debug("Rotating by 90 degrees.")
        path = transposeAndSave(path, Image.ROTATE_90)
    return path

def transposeAndSave(path, trans):
    tmp = path
    with Image.open(path) as img:
        img = img.transpose(trans)
        tmp = tempfile.gettempdir()
        tmp = os.path.join(tmp, 'transposed.jpg')
        img.save(tmp)
    return tmp

