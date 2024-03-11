import cv2 as cv
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('black',blank)

cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)