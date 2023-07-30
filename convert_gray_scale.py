import os,cv2
import sys
path = r'E:\JP\M-TECH\dissertation\data\cat emotion\Relaxed'
dstpath = r'E:\JP\M-TECH\dissertation\data\cat emotion gray image dataset\Relaxed' # Destination Folder



try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in asme folder")

# Folder won't used
files = os.listdir(path)

for image in files:
    img = cv2.imread(os.path.join(path,image))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(dstpath,image),gray)
