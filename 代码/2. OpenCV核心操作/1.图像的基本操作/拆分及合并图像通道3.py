import cv2

img = cv2.imread('../../images/u=946077695,626131535&fm=26&gp=0.jpg')
cv2.imshow('img1', img)
img[:, :, 2] = 0  # 红色通道值
cv2.imshow('img2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
