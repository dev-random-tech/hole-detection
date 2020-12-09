import cv2
import numpy as np

im = cv2.imread('./TestImages/hole5.jpg')

gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
gray=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)[1]
cv2.imshow('gray',gray)

image,contours,hierarchy = cv2.findContours(gray,cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE)
count =0
for cnt in contours:
    area = cv2.contourArea(cnt)

    if area>100 and area<1500:
        cv2.drawContours(im,[cnt],0,(255,0,0),5)
        count = count+1
print(count)
cv2.imshow('im',im)
cv2.waitKey()
