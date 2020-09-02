import numpy as np
import cv2 as cv

drawing = False  # 如果按下鼠标则为真
mode = True  # 如果为真，则绘制矩形。按“m”切换到曲线
ix, iy = -1, -1


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    # 按下鼠标
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 移动鼠标
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing is True:
            if mode is True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 10, (0, 0, 255), -1)
    # 鼠标离开
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode is True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 10, (0, 0, 255), -1)


# 创建一个黑色图像，一个窗口
img = np.zeros((300, 400, 3), np.uint8)
winname = 'image'
cv.namedWindow(winname)
# 将函数绑定到窗口
cv.setMouseCallback(winname, draw_circle)
while (1):
    cv.imshow(winname, img)
    # 按esc按键退出
    k = cv.waitKey(27)
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyWindow(winname)
