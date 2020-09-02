import cv2

cap = cv2.VideoCapture(
    'https://vd4.bdstatic.com/mda-khuhakge1k4pj6u2/v1-cae/sc/mda-khuhakge1k4pj6u2.mp4?auth_key=1598678110-0-0-c3851c0b2d9af49ac6b86c9dde38f141&bcevod_channel=searchbox_feed&pd=1&pt=3')
while (True):
    # 一帧一帧捕获
    ret, frame = cap.read()
    # 对帧的操作，转换成灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示结果帧
    cv2.imshow('frame', gray)
    # 输入q退出捕获
    if cv2.waitKey(25) == ord('q'):
        break
# 当一切都完成后，释放捕获
cap.release()
# 销毁窗口
cv2.destroyAllWindows()
