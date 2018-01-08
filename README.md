# WechatGame_JumpJumpJump
use python+pywin32+opencv to play wechat game
## 所需要的库
- PIL
- pyautogui
- opencv
- numpy
- win32gui
- pyinstaller

## 系统工程概述
- build和dist是使用pyinstaller打包成可执行文件后自动生成的
- pic中存放了系统测试的gif、avi格式的测试结果 和 棋子的匹配图
- test是随编写系统时不断跟进的单元测试样例集合

## 核心代码思路
```python
# 1. 截取游戏界面
game_img = grab()
# 2. 找棋子位置
game_img, chess_x, chess_y = find_chess(game_img)
# 3. 找目标位置
game_img, goal_x, goal_y = find_goal(game_img, chess_x, chess_y, chess_w, chess_h)
# 4. 计算位置并控制鼠标按下
calc_press(chess_x, chess_y, goal_x, goal_y)
# # 5. 休眠1s，用于奖励块的加分
sleep(1)
```

## 运行
- 首先通过360手机助手，打开360演示界面
- 运行python main.py
- 将鼠标移动到360演示界面中即可开始
