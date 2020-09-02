import cv2
from matplotlib import pyplot as plt

RED = [255, 0, 0]
img1 = cv2.imread('../../images/u=857048284,4213054229&fm=26&gp=0.jpg')
constant = cv2.copyMakeBorder(img1, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=RED)  # 添加恒定的彩色边框,需要用到value参数
reflect = cv2.copyMakeBorder(img1, 50, 100, 50, 50, cv2.BORDER_REFLECT)  # 边框将是边框元素的镜像
reflect101 = cv2.copyMakeBorder(img1, 50, 50, 50, 50,
                                cv2.BORDER_REFLECT_101)  # 或者使用cv.BORDER_DEFAULT，边框将是边框元素的镜像，但略有变化
replicate = cv2.copyMakeBorder(img1,50, 50, 50, 50, cv2.BORDER_REPLICATE)  # 最后一个元素被复制
wrap = cv2.copyMakeBorder(img1, 50, 50, 50, 50, cv2.BORDER_WRAP)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(236), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.show()
