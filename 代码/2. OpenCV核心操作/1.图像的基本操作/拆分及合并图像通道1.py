import cv2

img = cv2.imread('../../images/u=946077695,626131535&fm=26&gp=0.jpg')
# print(img.shape, img.size, img.dtype)  # (400, 400, 3) 480000 uint8
cv2.imshow('img1', img)
b, g, r = cv2.split(img)  # cv.split()是一项昂贵的操作（就时间而言）。因此，仅在必要时使用它。否则请进行Numpy索引。
img = cv2.merge((b, g, r))
cv2.imshow('img2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()