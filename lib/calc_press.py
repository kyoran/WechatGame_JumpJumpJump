# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

import pyautogui
from time import sleep
from math import sqrt

# 计算距离和按压时间
dis2presstime_rate = 0.0042
def calc_press(*locs):
    print("Chess location: (%d, %d)" % (locs[0], locs[1]))
    print("Goal location: (%d, %d)" % (locs[2], locs[3]))
    # 1.计算距离
    distance = int(sqrt(abs(locs[2]-locs[0])**2+abs(locs[3]-locs[1])**2))
    print("Distance =", distance)
    # 2.计算按压时间
    press_time = dis2presstime_rate * distance# - 0.02
    print("Press time =", press_time)
    print()
    # 3.控制鼠标按压
    sleep(1)
    dim_x = pyautogui.position()[0]
    dim_y = pyautogui.position()[1]
    # pyautogui.click(dim_x, dim_y)
    pyautogui.mouseDown(x=dim_x, y=dim_y, button='left')
    sleep(press_time)
    pyautogui.mouseUp(x=dim_x, y=dim_y, button='left')