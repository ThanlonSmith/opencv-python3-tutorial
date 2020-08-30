import cv2 as cv

img = cv.imread('../images/u=2875076343,2172557877&fm=15&gp=0.jpg')
# 通过像素值的行和列坐标来访问图像
px = img[100, 100]
print(px)  # [243 245 253]
# 仅访问蓝色像素
blue = img[100, 100, 0]
print(blue)  # 243
# 修改像素值
img[100, 100] = [255, 255, 255]
print(img[100, 100])  # [255 255 255]
# 更好的像素访问和编辑方法
px = img.item(100, 100, 2)
print(px)  # 255
img.itemset((100, 100, 2), 100)
px = img.item(100, 100, 2)
print(px)  # 100
