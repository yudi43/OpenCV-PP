import cv2


img = cv2.imread('resources/test.jpeg')

cv2.imshow('output', img)
cv2.waitKey(0)
