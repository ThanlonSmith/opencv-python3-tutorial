import cv2 as cv

img = cv.imread('../images/u=3126408186,2598873524&fm=15&gp=0.jpg')
# 图像的形状
print(img.shape)
"""
(400, 400, 3)
"""
# 像素总数
print(img.size)
"""
480000
"""
# 图像数据类型
print(img.dtype)
"""
uint8
"""
