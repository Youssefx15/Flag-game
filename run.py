# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:26:09 2022


"""

import cv2 
import pandas as pd 
import glob
import random 
find=glob.glob('**/*.png')

face_clsfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

source=cv2.VideoCapture(0)
check=True
while(True):
    ret,img=source.read()
    ret=cv2.flip(img,1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_clsfr.detectMultiScale(gray,1.05,20)
    key=cv2.waitKey(1)
    for x,y,w,h in faces:
        
        if check==True:
            w3=w//3
            flag=cv2.imread(random.choice(find))
            flag=cv2.resize(flag,(w3,50))
            img[y-50:y,x+w3:x+2*w3]=flag
        else:
            w3=w//3
            flag=cv2.resize(flag_cop,(w3,50))
            img[y-50:y,x+w3:x+2*w3]=flag
        
        if key==ord('a'):
            flag_cop=flag
            check=False

        if key==ord('w'):
            check=True
        cv2.imshow('LIVE',img)
    if(key==27):
        break
cv2.destroyAllWindows()
source.release()


