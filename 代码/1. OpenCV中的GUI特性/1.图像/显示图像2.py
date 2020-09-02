import cv2

img = cv2.imread('../images/u=814827906,2707114620&fm=26&gp=0.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()