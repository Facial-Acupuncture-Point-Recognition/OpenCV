#numpy 與圖片關係，和切割圖片 opencv中的顏色順序: 藍b、綠g、紅r
import cv2
import numpy as np
import random

img = cv2.imread('hornets.jpg')
# print(img.shape)

# img = np.empty((300, 300, 3), np.uint8)    np.empty() 創建一個多維陣列；  np.uint8:  uint = 正整數， 8 = 電腦二進制，所以0-255是8個bits

# for row in range(300):
#     for col in range(img.shape[1]):     img.shape[1]圖片寬度
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
#random.randint() 隨機顏色， 會變成馬賽可
newImg = img[400:650,:500]  #切割圖片， []陣列中， 切割(y軸，向下為正)400到650像素， 切割(x軸，向右為正)0到500像素

cv2.imshow('img', img)
cv2.imshow('newImg', newImg)
cv2.waitKey(0)
