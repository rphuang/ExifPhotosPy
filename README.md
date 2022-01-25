# ExifPhotosPy
A simple Python program to view photos with EXIF metadata. ExifPhotos provides flexible UI and extensible metadata extraction.
* Flexible - customize your own list of tags to display
* Extensible - customize your own metadata mapping to extract
* Configurable UI
Currently, ExifPhotos uses exifread to extract EXIF from file. The data quality of exifread is not as good as ExifTool but it is good enough to view most important EXIF info.

# Getting Started
1. Install dependencies
	* Kivy (https://kivy.org/#home): pip install kivy[base]
    * exifread (https://github.com/ianare/exif-py): pip install exifread
	* Pillow (https://python-pillow.org/): pip install --upgrade Pillow
2. Get ExifPhotosPy code from https://github.com/rphuang/ExifPhotosPy.
3. In Windows, run the program from the folder: python exifMain.py
4. Click "Open" to navigate to the folder with photos and click "Load". See Configuration to set default folder to start.

# Configuration

## exifMainConfig.txt file
* Window.top - set the top position for the ExifPhotos window
* Window.left - set the left position for the ExifPhotos window
* Window.width - set the width for the ExifPhotos window
* Window.height - set the height for the ExifPhotos window
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

# Issues & Future Development
* To support swipe gesture.
* Does Kivy really support Android? The Kivy Launcher disappeared from the Google Play Store. So, it needs extra efforts to test it in Android!
* Leverage ExifTool to support more metadata (at least on Windows version)
* Save the rotated photos (currently, the rotated image is saved in temp folder and only used for image display) 
 
