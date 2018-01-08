# -*- coding: utf-8 -*-
"""description:xxx"""
__author__ = "kyoRan"

import cv2
import numpy as np

under_game_score_y = 170  # 截图中刚好低于分数显示区域的 Y 坐标

def blurcanny(img):
    """
    模糊+边缘检测
    :param img:
    :return:
    """
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


def find_step(img, chess_x, chess_y, chess_w, chess_h):
    """
    找到目标位置
    1.模糊边缘检测
    2.去掉棋子
    3.找目标
    :param img:
    :param chess_x:
    :param chess_y:
    :param chess_w:
    :param chess_h:
    :return:
    """
    img = blurcanny(img)
    # img[chess_y - chess_h // 7 * 6: chess_y + 10] \
    # [chess_x - chess_w // 2: chess_x + chess_w // 2] = 255
    img[chess_y-chess_h//7*6:chess_y+10, chess_x-chess_w//2:chess_x+chess_w//2] = 0
    # cv2.imshow("chess", img)
    # cv2.waitKey(0)
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
    # cv2.line(img, (board_x_center - 20, board_y_center), (board_x_center + 20, board_y_center),
    #          (255, 0, 0), 1)
    # cv2.line(img, (board_x_center, board_y_center - 20), (board_x_center, board_y_center + 20),
    #          (255, 0, 0), 1)
    return img, board_x_center, board_y_center


def find_goal(img, chess_x, chess_y, chess_w, chess_h):
    goal_xs = []
    goal_ys = []
    # for _ in range(5):
    game_img, goal_x, goal_y = find_step(
        img, chess_x, chess_y, chess_w, chess_h
    )
    goal_xs.append(goal_x)
    goal_ys.append(goal_y)

    # goal_x = sum(goal_xs) // len(goal_xs)
    # goal_y = sum(goal_ys) // len(goal_ys)

    return img, goal_x, goal_y
