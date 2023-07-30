#!/usr/bin/python
from PIL import Image
import os, sys

path = r'E:\JP\M-TECH\dissertation\data\cat emotion\Relaxed'
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((299,299), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()
