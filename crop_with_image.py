import cv2
import numpy as np

img = cv2.imread('lena.jpg')
height, width = img.shape[0:2]

cv2.setMouseCallback(img, cutting)
while True:
    cv2.imshow('img',)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()