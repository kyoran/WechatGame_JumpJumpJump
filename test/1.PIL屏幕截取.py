# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

from PIL import ImageGrab

# 手机分辨率是1080*1920
TX=50; TY=154; BX=456; BY=850
BOX = (TX, TY, BX, BY)

# 参数是左上角和右下角
im = ImageGrab.grab(bbox=BOX)
print(im.height)
print(im.width)
im.save('a.png', 'png')