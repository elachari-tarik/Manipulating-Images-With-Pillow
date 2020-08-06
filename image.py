#!/usr/bin/env python3

import os
from PIL import Image

def transformImage(img,angle,width,height,extension):
    if img != '.DS_Store' and img.endswith(".py") != True:
        im = Image.open(img)
        rgb_im = im.convert('RGB')
        img_name = str(os.path.basename(img))+"."+str(extension)
        rgb_im.rotate(angle).resize((width,height)).save(img_name)



for img in os.listdir(os.getcwd()):
    transformImage(img,-90,128,128,"jpeg")

