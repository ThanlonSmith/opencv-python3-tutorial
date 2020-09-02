import cv2

img = cv2.imread('../../images/u=946077695,626131535&fm=26&gp=0.jpg')
cv2.imshow('img1', img)
b = img[:, :, 0]  # 获取蓝色通道值
g = img[:, :, 1]  # 获取绿色通道值
r = img[:, :, 2]  # 获取红色通道值
img = cv2.merge((b, g, r))
cv2.imshow('img2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
