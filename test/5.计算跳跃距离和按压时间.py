# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

import cv2
import numpy as np
import pyautogui
from time import sleep
from math import sqrt
####
# 找棋子
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
    chess_x = int(topx + chess_w / 2) - chess_bottom_x_base_bias
    chess_y = topy + chess_h - chess_bottom_y_base_bias
    # 在图片中标注出棋子位置
    cv2.circle(img, (chess_x, chess_y), 1, (0, 255, 255), -1)
    cv2.line(img, (chess_x, chess_y - chess_h // 2), (chess_x, chess_y + chess_bottom_y_base_bias),
             (255, 0, 0), 1)
    cv2.line(img, (chess_x - chess_w // 2, chess_y), (chess_x + chess_w // 2, chess_y),
             (255, 0, 0), 1)
    return img, chess_x, chess_y


# 找棋子结束
####
####
# 边缘检测
def blurcanny(img):
    # 原始图
    # game_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # 高斯滤波后的图
    game_img_blur = cv2.GaussianBlur(img, (3, 3), 4)
    # 高斯滤波后边缘提取后的图
    game_img_blur_canny = cv2.Canny(game_img_blur, 25, 30)
    # 将图片边框去掉
    game_img_blur_canny[:, 0:12] = 0
    game_img_blur_canny[:, -12:game_img_blur_canny.shape[1]] = 0
    # 返回结果
    return game_img_blur_canny


# 边缘检测结束
####
####
# 寻找目标位置
def find_goal(img):
    # 遍历起点为分数下沿
    board_y_top = under_game_score_y
    board_x_top = 0
    board_x_centers = [];
    board_x_center = 0;  # 跳板的中心
    board_y_center = under_game_score_y

    down_space = 0
    up_space = down_space

    calc_board_x_centers_count = 0  # 计算5个x中心点，求平均值
    for i in img[under_game_score_y:]:

        # 每次往下遍历一行
        board_y_center += 1
        # 找x的中心点
        if calc_board_x_centers_count != 5:
            condition = (i == 255)  # 黑色是0，白色是255
            # print(np.extract(condition, i))
            if len(np.extract(condition, i)) > 4:  # 避免图中无关的像素点干扰，大于4代表匹配成功
                left_location = 0;
                right_location = i.shape[0];  # 左右两边的横坐标
                for left in i[0:]:
                    # 从左侧（0）到右边
                    left_location += 1
                    if left == 255:
                        break
                    # print(left, end=",")
                for right in reversed(i[: i.shape[0]]):
                    # 从右侧（i.shape[0]）到中间（i.shape[0]//2）
                    right_location -= 1
                    # print(right, end=".")
                    if right == 255:
                        break
                board_x_centers.append((left_location + right_location) // 2)  # 计算左右两边的平均值
                calc_board_x_centers_count += 1
                board_x_center = np.mean(board_x_centers).astype(np.int32)
        else:
            # 找y的中心点
            llocation = board_x_center;
            rlocation = board_x_center;
            up_space = down_space
            # 从跳板中心往左
            for left in reversed(i[:board_x_center]):
                llocation -= 1
                if left == 255:
                    break
            # 从跳板中心往右
            for right in i[board_x_center:]:
                rlocation += 1
                if right == 255:
                    break
            # 计算横坐标的跨度
            down_space = rlocation - llocation
            if up_space - down_space > 3:  # 误差是3
                break
    # 画出顶点的坐标示意图
    cv2.line(img, (board_x_center - 20, board_y_center), (board_x_center + 20, board_y_center),
             (255, 0, 0), 1)
    cv2.line(img, (board_x_center, board_y_center - 20), (board_x_center, board_y_center + 20),
             (255, 0, 0), 1)
    return img, board_x_center, board_y_center
# 寻找目标位置结束
####

####
# 计算距离和按压时间
dis2presstime_rate = 0.0045
def calc_distantce_presstime(*locs):
    # 1.计算距离
    distance = int(sqrt(abs(locs[2]-locs[0])**2+abs(locs[3]-locs[1])**2))
    print("distance =", distance)
    # 2.计算按压时间
    press_time = dis2presstime_rate * distance
    print("press time =", press_time)
    # 3.控制鼠标按压
    sleep(1)
    dim_x = pyautogui.position()[0]
    dim_y = pyautogui.position()[1]
    #pyautogui.click(dim_x, dim_y)
    pyautogui.mouseDown(x=dim_x, y=dim_y, button='left')
    sleep(press_time)
    pyautogui.mouseUp(x=dim_x, y=dim_y, button='left')

if __name__ == '__main__':
    under_game_score_y = 180  # 截图中刚好低于分数显示区域的 Y 坐标

    res_img = cv2.imread(".\\game.jpg", cv2.IMREAD_GRAYSCALE)
    res_img, chess_x, chess_y = find_chess(res_img)
    game_img, goal_x, goal_y = find_goal(blurcanny(res_img))

    print("Chess location: (%d, %d)" % (chess_x, chess_y))
    print("Goal location: (%d, %d)" % (goal_x, goal_y))

    calc_distantce_presstime(chess_x, chess_y, goal_x, goal_y)

    cv2.imshow("hello", game_img)
    cv2.waitKey(0)