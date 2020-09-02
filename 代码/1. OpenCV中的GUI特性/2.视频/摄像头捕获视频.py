import cv2

cap = cv2.VideoCapture(0)
while (True):
    # 一帧一帧捕获
    ret, frame = cap.read()
    # 镜像水平翻转
    frame = cv2.flip(frame, 1)
    # 对帧的操作，转换成灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 显示结果帧
    cv2.imshow('frame', gray)
    # 输入q退出捕获
    if cv2.waitKey(1) == ord('q'):
        break
# 当一切都完成后，释放捕获
cap.release()
# 销毁窗口
cv2.destroyAllWindows()
