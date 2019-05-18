import os
from PIL import Image
path = 'Apple_healthy'


image_paths = [os.path.join(path, f) for f in os.listdir(path)]
     # images will contains face images
images = []
     # labels will contains the label that is assigned to the image
labels = []
i = 1
for image_path in image_paths:
    os.rename(image_path,"Apple_healthy/Apple_healthy."+str(i)+".jpg")
    i+=1;
