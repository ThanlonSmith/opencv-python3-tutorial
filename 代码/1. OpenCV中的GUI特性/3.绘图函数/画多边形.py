import numpy as np
import cv2

winname = 'polygon'
cv2.namedWindow(winname)
# 创建一幅黑色图像
img = np.zeros((300, 400, 3), np.uint8)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
"""
pts：
array([[10,  5],
       [20, 30],
       [70, 20],
       [50, 10]], dtype=int32)
"""
# reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的
pts = pts.reshape((-1, 1, 2))
"""
pts：
array([[[10,  5]],
       [[20, 30]],
       [[70, 20]],
       [[50, 10]]], dtype=int32)
"""
cv2.polylines(img, [pts], True, (0, 255, 255))
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyWindow(winname)
