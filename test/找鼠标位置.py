import pyautogui
from time import sleep
#
# sleep(2)
# print(pyautogui.position())

import win32gui
import win32api


classname = "CPhoneCtrlFrameWindow"
titlename = "实时演示"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)
print(hwnd)
#获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)