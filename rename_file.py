import os
import sys
path = r'cat_final\5\\test\\Angry'
files = os.listdir(path)

count = 1
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['angry',str(count), '.jpg'])))
    count += 1
