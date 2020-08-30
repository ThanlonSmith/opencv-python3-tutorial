import cv2

img = cv2.imread('../images/u=2423156162,3851369683&fm=26&gp=0.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:  # 如果按下ESC按键退出不保存
    cv2.destroyAllWindows()
elif k == ord('s'):  # 按下’s’键保存后退出
    cv2.imwrite('jubaobao.jpg', img)
    cv2.destroyAllWindows()
