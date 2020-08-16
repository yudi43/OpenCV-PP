import cv2
import numpy as np

img = cv2.imread('resources/test.jpeg')
kernel = np.ones((5, 5), np.uint8)


imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)

cv2.imshow('Gray image', img)
cv2.imshow('Gray image', imgGrey)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('img dialation', imgDialation)
cv2.imshow('img erode', imgEroded)

cv2.waitKey(0)
