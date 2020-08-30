import cv2

cap = cv2.VideoCapture(0)
# 定义编解码器并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    # 一帧一帧捕获
    ret, frame = cap.read()
    if ret:
        # 镜像水平翻转
        frame = cv2.flip(frame, 1)
        # 写翻转的帧
        out.write(frame)
        # 显示结果帧
        cv2.imshow('frame', frame)
        # 输入q退出捕获
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break
#  如果工作完成了就释放一切
cap.release()
out.release()
cv2.destroyAllWindows()
