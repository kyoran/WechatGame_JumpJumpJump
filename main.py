# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

from lib.grab import grab
from lib.find_chess import find_chess, chess_w, chess_h
from lib.find_goal import find_goal
from lib.calc_press import calc_press
from time import sleep
from matplotlib import pyplot as plt
import cv2

if __name__ == '__main__':

    while True:
        try:
            # 1. 截取游戏界面
            game_img = grab()
            # cv2.imshow("game_img", game_img)
            # cv2.waitKey(0)
            # 2. 找棋子位置
            game_img, chess_x, chess_y = find_chess(game_img)
            # 3. 找目标位置
            game_img, goal_x, goal_y = find_goal(game_img, chess_x, chess_y, chess_w, chess_h)
            # 4. 计算位置并控制鼠标按下
            calc_press(chess_x, chess_y, goal_x, goal_y)
            # # plt.imshow(game_img)
            # # plt.show()
            #
            # # 5. 休眠2s
            # cv2.imshow("game", game_img)
            # cv2.waitKey(0)
            sleep(1)
        except KeyboardInterrupt:
            print("Game is over!")
            break



