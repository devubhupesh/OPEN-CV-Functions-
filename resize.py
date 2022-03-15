#def from tkinter import Frame
from turtle import width


import cv2 as cv

img = cv.imread('PHOTOS\dog.jpeg')
cv.imshow('cat',img)
cv.waitKey(0)  

#for live video straeming resize method
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)


# this can be sued for static videos ie saved video files resizing
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

cv.waitKey(0)

capture = cv.VideoCapture('VIDEOS/cat.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale= 0.2)
    cv.imshow('video',frame)
    cv.imshow('videoResized', frame_resized)
    if cv.waitKey(0) & 0xFF ==ord('d'):
        break
    capture.release()
    cv.destroyAllWindows