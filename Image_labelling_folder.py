import os
from PIL import Image
path = 'images'

folder = [os.path.join(path, f) for f in os.listdir(path)]

for fol in folder:

    image_paths = [os.path.join(fol, fi) for fi in os.listdir(fol)]
         # images will contains face images
    images = []
         # labels will contains the label that is assigned to the image
    labels = []
    i = 1
    p = fol.split("\\")
    #print(p[1])
    print(fol)
    for image_path in image_paths:
        os.rename(image_path,  fol + "\\" + p[1] + "." +str(i)+".jpg")
        i+=1;
