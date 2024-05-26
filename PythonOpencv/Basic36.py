#Sobel Method
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/currency.jpg" , 0)

SobelX = cv2.Sobel(img , -1 , 1 , 0)
SobelY = cv2.Sobel(img , -1 , 0 , 1)
SobelXY = cv2.bitwise_or(SobelX , SobelY)

titles = ["Original" , "SobelX" , "SobelY" , "SobelXY"]
images = [img , SobelX , SobelY , SobelXY]

for i in range(len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i] , cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
