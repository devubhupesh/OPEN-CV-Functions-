from asyncore import read
import cv2 as cv
img = cv.imread('PHOTOS\dog.jpeg')
cv.imshow('cat',img)
cv.waitKey(0)
capture = cv.VideoCapture('VIDEOS/kitty.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
    capture.release()
    cv.destroyAllWindows