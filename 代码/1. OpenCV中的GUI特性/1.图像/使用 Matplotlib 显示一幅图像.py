import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../images/u=3472372044,2573289519&fm=11&gp=0.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
