
from PIL import Image
from glob import glob
import os

# source path where all your tif/tiff/png images present
path=os.getcwd()+'/PutHereFileName/'
#this will make new folder in current working directory /jpgImage
os.makedirs(os.getcwd()+'/jpgImage/')
#glob will help us to read all the file inside folder which have extension .tif/.tiff/.png
for file in glob(path+'*.tif'):
    try:
        #reading the Image
        im=Image.open(file)
        #just removing the .tiff from backward
        file=str(file).rstrip(".tif")
        #split and get your filename 
        filename=file.split('/')[-1]
        #now put image in new folder jpgImage
        im.save(os.getcwd()+'/jpgImage/'+filename+'.jpg','JPEG')
    except:
        continue
print("Conversion from tif to jpg completed!")

#from this you can convert .png/.tif/.tiff just changing line 11,16 