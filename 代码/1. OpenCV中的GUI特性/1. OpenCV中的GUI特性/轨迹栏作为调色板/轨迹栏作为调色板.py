import numpy as np
import cv2 as cv


def nothing(x) -> None:
    pass


# 创建黑色图像
img = np.zeros((200, 400, 3), np.uint8)
# 创建一个窗口
winname = 'image'
cv.namedWindow(winname)
# 创建用于颜色更改的轨迹栏
cv.createTrackbar('R', winname, 0, 255, nothing)
cv.createTrackbar('G', winname, 0, 255, nothing)
cv.createTrackbar('B', winname, 0, 255, nothing)
# 为开/关功能创建开关
switch = '0 : OFF \n 1 : ON'
cv.createTrackbar(switch, winname, 0, 1, nothing)
while (1):
    cv.imshow(winname, img)
    k = cv.waitKey(1)
    if k == 27:
        break
    # 获取四个轨迹条的当前位置
    r = cv.getTrackbarPos('R', winname)
    g = cv.getTrackbarPos('G', winname)
    b = cv.getTrackbarPos('B', winname)
    s = cv.getTrackbarPos(switch, winname)
    # 开关关闭
    if s == 0:
        img[:] = 0
    # 开关打开
    else:
        img[:] = [b, g, r]
cv.destroyWindow(winname)
