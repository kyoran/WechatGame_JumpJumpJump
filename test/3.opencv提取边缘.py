# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

import cv2

def blurcanny(img):
    # 原始图
    game_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # 高斯滤波后的图
    game_img_blur = cv2.GaussianBlur(game_img, (3, 3), 5)
    # 高斯滤波后边缘提取后的图
    game_img_blur_canny = cv2.Canny(game_img_blur, 26, 30)
    # 返回结果
    return game_img_blur_canny

game_img = blurcanny(".\\game.jpg")

cv2.imshow("game_img", game_img)
# cv2.imshow("game_img_blur", game_img_blur)
# cv2.imshow("game_img_blur_canny", game_img_blur_canny)

cv2.waitKey(0)

