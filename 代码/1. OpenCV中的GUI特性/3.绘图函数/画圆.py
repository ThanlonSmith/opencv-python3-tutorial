import numpy as np
import cv2

# 创建一幅黑色图像
img = np.zeros((300, 400, 3), np.uint8)
# 起点坐标： (299, 0)，终点坐标：(399, 99)，颜色：(0, 255, 0)，线条粗细：1
cv2.rectangle(img, (299, 0), (399, 99), (0, 255, 0), 1)
# 圆心坐标：(300, 63),半径：150,颜色： (0, 0, 255)，粗细：1（如果是-1表示填充）
cv2.circle(img, (150, 150), 148, (0, 0, 255), 2)
cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()