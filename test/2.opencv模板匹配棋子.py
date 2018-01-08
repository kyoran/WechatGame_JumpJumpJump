# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

import cv2
import numpy as np

meth = eval("cv2.TM_CCORR_NORMED")
chesstemplate = cv2.imread('.\\chesstemplate.jpg', cv2.IMREAD_GRAYSCALE)
chess_w, chess_h = chesstemplate.shape[::-1]
chess_bottom_x_base_bias = 5
chess_bottom_y_base_bias = 10

def find_chess(img):
    res = cv2.matchTemplate(img, chesstemplate, meth)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    topx, topy = max_loc  # 最大值左上角的左边
    # 修正为棋子底盘的中心坐标
    chess_x = int(topx + chess_w/2) - chess_bottom_x_base_bias
    chess_y = topy + chess_h - chess_bottom_y_base_bias

    img[chess_x: chess_x+chess_w][chess_y: chess_y+chess_h] = 255

    return img, chess_x, chess_y

# 读取游戏界面
# game_img = cv2.imread(".\\game.jpg", cv2.IMREAD_GRAYSCALE)
game_img = cv2.imread(".\\game.jpg", cv2.IMREAD_GRAYSCALE)

# 找到棋子的位置
game_img, chess_x, chess_y = find_chess(game_img)
print(chess_x, chess_y)

# 显示棋子的位置，图中用黑色的圆标出了
cv2.circle(game_img, (chess_x, chess_y), 1, (0, 255, 255), -1)
cv2.line(game_img, (0, chess_y), (1000, chess_y),
         (255, 0, 0), 1)
cv2.line(game_img, (chess_x, 0), (chess_x, 1000),
         (255, 0, 0), 1)
cv2.imshow("hello", game_img)
cv2.waitKey(0)

