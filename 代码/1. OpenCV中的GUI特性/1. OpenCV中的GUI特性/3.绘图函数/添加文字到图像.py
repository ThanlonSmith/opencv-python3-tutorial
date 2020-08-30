import cv2

win_name = 'OpenCV-Python'
# cv2.namedWindow('OpenCV-Python',cv2.WINDOW_NORMAL)
cv2.namedWindow(win_name)
img = cv2.imread('../images/u=3938089569,3100006972&fm=26&gp=0.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
lineType = cv2.LINE_AA
# img：图像
# OpenCV-Python：要添加的文字
# (20, 110)：起始坐标
# font：字体
# 1：字体比例
# (255, 255, 255)：字的颜色
# 4：字的粗细
# lineType：线的类型：
cv2.putText(img, 'OpenCV-Python', (20, 110), font, 1, (255, 255, 255), 4, lineType)
cv2.imshow(win_name, img)
cv2.waitKey(0)
cv2.destroyWindow(win_name)
