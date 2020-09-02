import cv2 as cv
import numpy as np


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 50, 255, -1)


# 创建一个黑色图像，一个窗口
img = np.zeros((300, 400, 3), np.uint8)
winname = 'image'
cv.namedWindow(winname)
# 将函数绑定到窗口
cv.setMouseCallback(winname, draw_circle)
while (1):
    cv.imshow(winname, img)
    # 按esc按键退出
    if cv.waitKey(20) == 27:
        break
cv.destroyWindow(winname)
