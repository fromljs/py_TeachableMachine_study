import os
from datetime import datetime
import shutil

loadDir = r'C:\Users\jslee\Desktop\새 폴더\세방이미지'
for (path, dir, files) in os.walk(loadDir):
    for dirname in dir:
        filecount = 0
        print(path + '\\' + dirname)
        for file in files:
            filecount += 1        
        if filecount > 0 :
            print(path + '\\' + dirname + ' ' + str(filecount))
            # loadImg(path + '\\' + dirname)

