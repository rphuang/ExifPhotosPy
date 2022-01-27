import sys

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty
from kivy.core.window import Window

from exifData import Exifdata
from config import Config
from photoList import PhotoList
from util import transposeImage

class MainWidget(BoxLayout):
    """ The main/root widget for the ExifPhotos. The UI is defined in .kv file """
    def __init__(self, config):
        super(MainWidget, self).__init__()
        self.config = config
        # load tag mappings defined in config
        self.exifdata = Exifdata()
        mappingFileList = config.getOrAdd('TagMappingFiles', 'StdTagMapping.txt').split(',')
        for item in mappingFileList:
            self.exifdata.addMapping(item.strip())
        # load display tags
        self.displayTags = []
        tags = config.getOrAdd('DisplayTags', 'Image Width, Image Height, Date Taken').split(',')
        for item in tags:
            self.displayTags.append(item.strip())
        # create PhotoList with starting folder
        self.defaultFolder = config.getOrAdd('DefaultFolder', '') 
        self.includeSubfolder = config.getOrAddBool('IncludeSubfolder', False)
        self.photos = PhotoList()
        self.openFolder(self.defaultFolder)

    def openDialog(self):
        """ popup dialog to select folder """
        content = FolderPickerDialog(self)
        content.ids.filechooser.path=self.photos.folder
        if Window.width > 900:
            sizehint=(0.4, 0.6)
        else:
            sizehint=(0.8, 0.6)
        self._popup = Popup(title="Folder Picker", content=content, auto_dismiss=False, size_hint=sizehint)
        self._popup.open()
        pass

    def dismissDialog(self):
        """ dismiss the pop up dialog """
        self._popup.dismiss()

    def openFolder(self, folder):
        """ populate all files from the folder and display the first file """
        self.photos.openFolder(folder, self.includeSubfolder)
        self.displayFile(self.photos.currentPhoto())

    def displayFile(self, filePath):
        """ display file's name, image, and exif data """
        if filePath is not None:
            self.displayExifGrid(filePath)
            self.ids.ImageLabel.text = filePath
            if 'PhotoIndex' in self.ids:
                self.ids.PhotoIndex.text = '%i' %(self.photos.index+1)
                self.ids.PhotoCountLabel.text = '%i' %(len(self.photos.photos))
            # if orientation is not normal then transpose the image in a temporary file
            srcPath = transposeImage(filePath, self.exifdata)
            self.ids.PhotoImage.source = srcPath
            if not srcPath == filePath:
                # reload from the temp file since it's the same file and will be cached by Image
                self.ids.PhotoImage.reload()

    def nextPhoto(self):
        """ move to next photo if available """
        self.displayFile(self.photos.next())

    def prevPhoto(self):
        """ move to prev photo if available """
        self.displayFile(self.photos.prev())

    def goto(self, number):
        """ move to specified number (index + 1). move to the last photo if number is < 1 or > max """
        self.displayFile(self.photos.goto(int(number)-1))

    def displayExifGrid(self, filePath):
        """ display exif data """
        self.exifdata.getExifdata(filePath)
        grid = self.ids.exifGrid
        grid.clear_widgets()
        for key in self.displayTags:
            if self.exifdata.hasKey(key):
                self.displayTag(key, self.exifdata.getValue(key))

    def displayTag(self, name, value):
         grid = self.ids.exifGrid
         label = Label(text=str(name))
         grid.add_widget(label)
         label = Label(text=str(value))
         grid.add_widget(label)

    #def on_touch_down(self, touch):
    #    print(touch)

class FolderPickerDialog(FloatLayout):
    def __init__(self, mainWidget):
        super(FolderPickerDialog,self).__init__()
        self.mainWidget = mainWidget
    def cancel(self):
        self.mainWidget.dismissDialog()
    def open(self, path):
        self.mainWidget.dismissDialog()
        self.mainWidget.openFolder(path)

# we are defining the Base Class of our Kivy App
class exifMainApp(App):
    def __init__(self, displayTagsFile):
        super(exifMainApp,self).__init__()
        self.displayTagsFile = displayTagsFile

    def build(self):
        # return a MainWidget() as a root widget
        self.mainWidget = MainWidget(self.displayTagsFile)
        return self.mainWidget

if __name__ == '__main__':
    configFile='exifMainConfig.txt'
    if len(sys.argv) > 1:
        configFile = sys.argv[1]
    # apply config settings
    config = Config(configFile, autoSave = False)
    if config.getOrAddBool('Window.fullscreen', False):
        Window.fullscreen = True
    else:
        Window.size = (config.getOrAddInt('Window.width', 1600), config.getOrAddInt('Window.height', 1000))
        Window.top = config.getOrAddInt('Window.top', 40)
        Window.left = config.getOrAddInt('Window.left', 100)
    app = exifMainApp(config)
    app.run()

