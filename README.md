# ExifPhotosPy
A simple Python program to view photos with EXIF metadata. ExifPhotos provides flexible UI and extensible metadata extraction.
* Flexible - customize your own list of tags to display
* Extensible - customize your own metadata mapping to extract
* Configurable UI

Currently, ExifPhotos uses exifread to extract EXIF from file. The data quality of exifread is not as good as ExifTool but it is good enough to view most important EXIF info.

# Getting Started
1. Install dependencies
	* Kivy (https://kivy.org/doc/stable/gettingstarted/installation.html)
    * exifread (https://github.com/ianare/exif-py): pip install exifread
2. Get ExifPhotosPy code from https://github.com/rphuang/ExifPhotosPy.
3. Run ExifPhotos in Windows (see Notes for running in Android)
    * run the command from the folder: python exifMain.py
    * Click "Open" to navigate to the folder with photos and click "Load". See Configuration to set default folder to start.

# Configuration

## exifMainConfig.txt file
* Window.top - set the top position for the ExifPhotos window
* Window.left - set the left position for the ExifPhotos window
* Window.width - set the width for the ExifPhotos window
* Window.height - set the height for the ExifPhotos window
* ShowFullFilePath - set True to display full path name of the image file
* OverrideGridFontSize - set True to override the font size in the exif data grid
* GridFontSize - specify the font size when OverrideGridFontSize is True
* TagMappingFiles - specify comma separated list of files that define tag mapping
* DefaultFolder - specify the default folder to open when ExifPhotos start 
* IncludeSubfolder - set to True to include all photos from sub-folders
* DisplayTags - specify comma separated list of tag names to be displayed

## Custom Tag Mappings
The TagMapping-Std.txt and TagMapping-Maker.txt contain the standard mappings and custom mappings for Nikon. New mappings can be added or to override the existing ones.
* One line per mapping with format "TagKey = exifreadTagKey" where
    * TagKey is the key and display tag name
    * exifreadTagKey is the key used by exifread
* Comment line starts with #
* Empty lines are ignored

Examples:
```
Image Width=EXIF ExifImageWidth
Lens Model=MakerNote LensType
```

## Custom UI
The UI is based on Python Kivy, so custom UI can be done by changing the exifMain.kv file. In the folder, there are two versions of .kv files. Just copy the version of files to exifMain.kv and exifMainConfig.txt.
* exifMain-wide.kv - this defines UI for a wide screen. It goes along with exifMainConfig-wide.txt.
* exifMain-vertical.kv - this defines UI for a small screen. It goes along with exifMainConfig-vertical.txt.

# Issues, Notes, and ToDos
* To support swipe gesture.
* Run ExifPhotos in Android with Pydroid 3:
    * install Pydroid 3
    * copy the ExifPhotos files to Pydroid program folder (should be under internal storage Android/data/...). It errors out when using folders outside.
    * copy the files from either android-landscape or android-portrait to the ExifPhotos folder
    * from Pydroid 3, open exifMain.py and run
* Leverage ExifTool to support more metadata (at least on Windows version)
* Save the rotated photos (currently, the rotated image is saved in temp folder and only used for image display) 
 
