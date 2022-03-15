#to draw shapes on images
import cv2 as cv
import numpy as np
 
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

#blank[200:300,300:400] = 0,255,0
#cv.imshow('green',blank)

#to draw rectangle
#cv.rectangle(blank,(0,0),(250,500),(255,255,0),thickness=2)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(200,152,0),-1
)
cv.imshow('Rectangle',blank)

#draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40, (0,255,0),thickness=3)
cv.imshow('circle',blank)
#draw line
cv.line(blank,(0,0),(250,300),(0,0,255),5)
cv.imshow('line',blank)
#text
cv.putText(blank,'heyyy, how are uu?',(150,200),cv.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),2)
cv.imshow('Text',blank)

cv.waitKey(0)
