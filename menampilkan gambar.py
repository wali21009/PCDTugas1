"muhammad waliyuddin F55121009"
import numpy as np
import cv2

img = cv2.imread('lena.jpg', 0)

cv2.imshow('gambar', img)
cv2.waitKey(0)
cv2.DestroyAllWindows()