import cv2
import numpy as np
"""
print "begin"
img = cv2.imread('img1.jpg')

print 'a'
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print 'b'
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
print 'c'

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print 'd'
cnt = contours[0]
print 'e'
x, y, w, h = cv2.boundingRect(cnt)
print 'f'
crop = img[y:y+h,x:x+w]
print 'g'
cv2.imwrite('img_.jpg', crop)
print 'h'
"""
from PIL import Image, ImageChops
import os
import sys
def trim(im):
	bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
	diff = ImageChops.difference(im, bg)
	diff = ImageChops.add(diff, diff, 2.0, -100)
	bbox = diff.getbbox()
	if bbox:
		return im.crop(bbox)
im = Image.open('image2.jpg')
im = trim(im)
im.show()
im.save('img_out.jpg')
