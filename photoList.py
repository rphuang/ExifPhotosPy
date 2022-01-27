#!/usr/bin/python3
# File name   : photoList.py
# Description : encapsulates list of photos in a folder

from util import getFiles

class PhotoList():
    """ encapsulates list of photos in a folder being displayed """
    def __init__(self):
        self.photos=[]
        self.index=0
        self.folder=None
        self.markLists = {}
        pass

    def openFolder(self, folderPath, includeSubfolder = False):
        """ open a folder and get the photo files """
        self.folder=folderPath
        self.photos.clear()
        self.index=0
        self.markLists.clear()
        getFiles(folderPath, fileList = self.photos, fileType = '.jpg', includeSubfolder = includeSubfolder)

    def currentPhoto(self):
        """ currently displayed photo"""
        if len(self.photos) > 0:
            return self.photos[self.index]
        else:
            return None

    def prev(self):
        """ prev photo """
        if len(self.photos) > 1 and self.index > 0:
            self.index -= 1
            return self.photos[self.index]
        else:
            return None

    def next(self):
        """ next photo """
        if len(self.photos) > self.index+1:
            self.index += 1
            return self.photos[self.index]
        else:
            return None

    def goto(self, index):
        """ move to specified index move to the last photo if index is < 0 or > max """
        if index < 0 or index >= len(self.photos):
            self.index = len(self.photos) - 1
        else:
            self.index = index
        return self.photos[self.index]

    def markPhoto(self, category, context):
        """ mark current folder with the category and context info """
        filePath = self.currentPhoto()
        if filePath is not None:
            key = category + context
            if key in self.markLists:
                marklist = self.markLists[key]
            else:
                marklist = [category, context, []]
                self.markLists[key] = marklist
            cat, ctx, files = marklist
            files.append(filePath)

    def saveMarkLists(self, filePath):
        """ save marklists to file """
        with open(filePath, "w") as f:
            for marklist in self.markLists.values():
                category, context, files = marklist
                for file in files:
                    f.write('%s %s %s\n' %(category, file, context) )
