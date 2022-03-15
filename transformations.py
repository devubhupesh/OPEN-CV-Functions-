import cv2 as cv
from cv2 import warpAffine
import numpy as np

img = cv.imread('PHOTOS/lab.jpeg')
cv.imshow('lab',img)
#tranlation of images to one corner
def translate(img, x, y) :
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -X --> left
# -y --> up
# x --> right      
# y --> down
translated = translate(img, -50,50)
cv.imshow('translated',translated)


#rotation

def rotate(img, angle, rotPoint=None) :
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensons = (width,height)

    return cv.warpAffine(img, rotMat, dimensons)
rotated = rotate(img , 60)
cv.imshow('roated', rotated)

rotated_img= rotate(rotated , -45)
cv.imshow('rotated img',rotated_img)


#resizing
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized', resized)
#interpolation = INTER_CUBIC is used for enlarging img

#flipping
flip = cv.flip(img, 0) # 0= flipping vertically
cv.imshow('flip',flip)
# flip value set to 1= horizontal, -1 = flip horizontal & vertically.

#cropping
cropped = resized[100:300, 200:400]
cv.imshow('crop',cropped)
cv.waitKey(0)