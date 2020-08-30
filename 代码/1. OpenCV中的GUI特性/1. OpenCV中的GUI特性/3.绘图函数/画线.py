import numpy as np
import cv2

# 创建一幅黑色图像
img = np.zeros((200, 200, 3), np.uint8)

# 画一条粗细为5px的蓝色对角线
cv2.line(img, (0, 0), (199, 199), (255, 0, 0), 5)
cv2.imshow('line', img)
cv2.waitKey(0)
