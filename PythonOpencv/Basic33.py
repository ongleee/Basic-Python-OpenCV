#เปรียบเทียบค่า BlockSize
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/map.jpg",0)

#กำหนดขนาด Block
size = [3,5,9,17,33]

plt.subplot(231,xticks=[] , yticks=[])
plt.title("Original")
plt.imshow(img,cmap="gray")

for i in range(len(size)):
    result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY , size[i] , 1)
    plt.subplot(232+i)
    plt.title("%d"%size[i])
    plt.imshow(result,cmap="gray")
    plt.xticks([]),plt.yticks([])


plt.show()
