import cv2

img = cv2.imread('../../images/roi.jpg')
print(img.shape, img.size, img.dtype)  # (280, 450, 3) 378000 uint8
cv2.imshow('img1', img)
ball = img[231:270, 88:130]  # 第一个参数是高度范围，第二个参数是宽度范围，(88,231)(130,270)
# 显示选择的ROI部分
img[220:259, 10:52] = ball  # 高度范围和宽度范围要一致，(10,220)(52,259)
cv2.imshow('ball', ball)
cv2.imshow('img2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
