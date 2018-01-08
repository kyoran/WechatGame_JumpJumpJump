# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"


from time import sleep

import pyautogui


sleep(2)

dim_x = pyautogui.position()[0]
dim_y = pyautogui.position()[1]

# pyautogui.doubleClick(x=dim_x, y=dim_y)
# pyautogui.click(x=dim_x, y=dim_y, tween=pyautogui.easeInQuad)
# pyautogui.dragTo(dim_x-10, dim_y, duration=2, button='left')
pyautogui.mouseDown(x=dim_x, y=dim_y, button='left')
sleep(2)
pyautogui.mouseUp(x=dim_x, y=dim_y, button='left')

#m.click(x,y,button,n) #鼠标点击
#x,y #是坐标位置
#button #1表示左键，2表示点击右键
#n –点击次数，默认是1次，2表示双击

# m = PyMouse()
# sleep(1)
# print(m.position())
# # print("screen size =", m.screen_size())
# # sleep(3)
# # print(m.position())
# # m.move(350, 350)
# # m.click(846, 22, 1, 2)
# # m.drag(846, 22)
# #m.click(350, 350, 1, 2)
# m.press(846, 22, 1)
# m.press(846, 22, 1)
# sleep(1)
# m.release(846, 22)
