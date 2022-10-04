from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

import os
from datetime import datetime
import shutil


def imgload(pathdir, Filename):
    imgFilename = pathdir + '\\' + Filename
    ngFilename = _ngDirname + '\\' + Filename
    okFilename = _okDirname + '\\' + Filename
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(imgFilename)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    ok = prediction.T[0]
    ng = prediction.T[1]

    # print(prediction)
    if  (ok < ng) and (ng > 0.9)  : 
        print(imgFilename + ' : ng', ng)
        shutil.copyfile(imgFilename, ngFilename)
        # with open(savefilename, mode='a', encoding='utf-8') as file:
        #     file.write('{0} {1} \n'.format(imgFilename , ng))        
    elif (ok > ng) and (ok < 0.6):
        print(imgFilename + ' : ok', ok)
        shutil.copyfile(imgFilename, okFilename)

def loadImg(path):
    # path = r'C:\Users\jslee\Desktop\새 폴더\세방이미지\현대신형-L70\Right'
    list = os.listdir(path)
    # savefilename = 'test_' + str(datetime.now())[0:10] + '.txt'

    for i in range(len(list)):
        if list[i].find('.jpg') > 0 :  
            imgload(path, list[i])




########### Main ############
loadDir = r'C:\Users\jslee\Desktop\새 폴더\세방이미지'
_ngDirname = r'C:\Users\jslee\Desktop\새 폴더\NG'
_okDirname = r'C:\Users\jslee\Desktop\새 폴더\OK' 
if not os.path.exists(_ngDirname): os.mkdir(_ngDirname)
if not os.path.exists(_okDirname): os.mkdir(_okDirname)


model = load_model('keras_model.h5')
for (path, dir, files) in os.walk(loadDir):
    for dirname in dir:        
        loadImg(path + '\\' + dirname)

