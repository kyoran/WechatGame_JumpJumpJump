# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

import cv2

meth = eval("cv2.TM_CCORR_NORMED")
chesstemplate = cv2.imread('.\\pic\\chesstemplate.jpg', cv2.IMREAD_GRAYSCALE)
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
    # 在图片中标注出棋子位置
    cv2.circle(img, (chess_x, chess_y), 1, (0, 255, 255), -1)
    cv2.line(img, (chess_x, chess_y-chess_h//2), (chess_x, chess_y+chess_bottom_y_base_bias),
             (255, 0, 0), 1)
    cv2.line(img, (chess_x-chess_w//2, chess_y), (chess_x+chess_w//2, chess_y),
             (255, 0, 0), 1)
    return img, chess_x, chess_y
