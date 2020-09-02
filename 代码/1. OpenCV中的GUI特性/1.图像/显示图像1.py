import cv2

img = cv2.imread('../images/u=625783906,2390041116&fm=11&gp=0.jpg')
cv2.imshow('jubaobao_first', img)
cv2.imshow('jubaobao_second', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
