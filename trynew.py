import os
from PIL import Image, ImageDraw, ImageChops
from images2gif import writeGif
import dlib
import cv2
import numpy
import sys


def trim(im):
	bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
                return im.crop(bbox)
im = Image.open('/home/sakshi/Documents/work/imgFolder/allFrames/image1.jpg')
im = trim(im)
im.save('/home/sakshi/Documents/work/imgFolder/selectFrames/image1.jpg')

im = Image.open('/home/sakshi/Documents/work/imgFolder/allFrames/image3.jpg')
im = trim(im)
im.save('/home/sakshi/Documents/work/imgFolder/selectFrames/image3.jpg')

im = Image.open('/home/sakshi/Documents/work/imgFolder/allFrames/image5.jpg')
im = trim(im)
im.save('/home/sakshi/Documents/work/imgFolder/selectFrames/image5.jpg')




img_list = ['/home/sakshi/Documents/work/imgFolder/selectFrames/image1.jpg', '/home/sakshi/Documents/work/imgFolder/selectFrames/image3.jpg', '/home/sakshi/Documents/work/imgFolder/selectFrames/image5.jpg']
os.system('convert -loop 0 %s /home/sakshi/Documents/work/imgFolder/gifCreated/anime_1_1.gif' % ' '.join(img_list))






