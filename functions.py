from asyncore import read
import cv2 as cv
from cv2 import Canny
from cv2 import dilate
from cv2 import INTER_AREA
import numpy as np

img = cv.imread('PHOTOS\cat.jpeg')
cv.imshow('cat',img)
#convert to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

#blur img
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blurredpic',blur)

#edge detection/ canny edge
Canny = cv.Canny(img,125,182)
cv.imshow('Cannyedge',Canny)
#to reduce details and get only borders pass in blur
Canny = cv.Canny(blur,125,175)
cv.imshow('edge',Canny)


dilate = cv.dilate(Canny,(3,3), iterations = 1)
cv.imshow('dilated',dilate)

resize = cv.resize(img, (500,500), interpolation=INTER_AREA) #this fn resizes to smaller dimension
#interpolation = INTER_CUBIC resizes to larger dimension

cropped = img[50:200, 200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)