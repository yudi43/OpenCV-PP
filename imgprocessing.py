#import cv2
#import numpy as np
#
#img = cv2.imread('resources/test.jpeg')
#kernel = np.ones((5, 5), np.uint8)
#
#
#imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 0)
#imgCanny = cv2.Canny(img, 100, 100)
#imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)
#imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)
#
#cv2.imshow('Gray image', img)
#cv2.imshow('Gray image', imgGrey)
#cv2.imshow('Blur Image', imgBlur)
#cv2.imshow('Canny image', imgCanny)
#cv2.imshow('img dialation', imgDialation)
#cv2.imshow('img erode', imgEroded)
#cv2.waitKey(0)


import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

print(img.shape)
cv2.line(img, (0, 0), (300, 300), (0, 255, 255), 3)
cv2.imshow('image', img)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 243), 3)
cv2.waitKey(0)