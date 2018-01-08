# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

import argparse
from PIL import ImageGrab
from pymouse import PyMouse
import numpy as np

import win32gui
import win32api

from time import sleep

m = PyMouse()
sleep(2)

# print(m.position())

classname = "CPhoneCtrlFrameWindow"
titlename = "实时演示"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)
print("句柄为：", hwnd)
#获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print("手机投影位置：", left, top, right, bottom)


TX = left+20; TY = top+70;
BX = right+left+40; BY = bottom-60;
BOX = (TX, TY, BX, BY)
# 参数是左上角和右下角
# im = ImageGrab.grab(bbox=BOX)
# print(im.height)
# print(im.width)
# im.save('a.png', 'png')
def grab():
    return np.array(ImageGrab.grab(bbox=BOX).convert('L'))