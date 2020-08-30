import numpy as np
import cv2

# 创建一幅黑色图像
img = np.zeros((300, 400, 3), np.uint8)
# 起点坐标： (299, 0)，终点坐标：(399, 99)，颜色：(0, 255, 0)，线条粗细：1
cv2.rectangle(img, (299, 0), (399, 99), (0, 255, 0), 1)
cv2.imshow('line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
