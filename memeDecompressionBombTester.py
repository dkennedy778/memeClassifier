#This class checks every image in the validation and training datasets. Currently it is checking for two criteria,

#1. Is the image a valid, openable image?
#2. Will the image trigger PILs decompression bomb protection (see for more https://github.com/python-pillow/Pillow/issues/515). Decompression bombs are small images with large metadatasets.

#Images which meet either of these criteria will crash the Image data generators in the identifier class, and need to be pruned before the program runs. You can delete these programatically using the os class, see https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder
#PILs error handling is pretty good, so all we have to do is open the image and see what exceptions it throws.


from PIL import Image, ImageFile
import os

directories = ['D:/Users/Derek/PostGrad/memeClassifier/validation/memes','D:/Users/Derek/PostGrad/memeClassifier/validation/notMemes','D:/Users/Derek/PostGrad/memeClassifier/train/memes','D:/Users/Derek/PostGrad/memeClassifier/train/notMemes']


for directory in directories:
    for picture in os.listdir(directory):
        try:
            im=Image.open(directory + '/' + picture)
        except OSError:
            print("picture failed to open " + directory + picture)
        except ValueError as VE:
            if str(VE) == "Decompressed Data Too Large":
                print("found a decompression bomb at " + directory + picture)
