#ตัวกรอง Convolution ด้วย filter2d
import cv2
import numpy as np
import matplotlib.pyplot as plt

#originaal
img = cv2.imread("image/noise.png")

#filter
filter2D = cv2.filter2D(img , -1 , np.ones((5,5) , np.float32)/25)

#blur
mean = cv2.blur(img , (5,5))

#median
mblur =  cv2.medianBlur(img , 5)

#Gaussian
gblur = cv2.GaussianBlur(img , (5,5) , 0)

titles = ["ORIGINAL" , "FILTER2D" , "MEAN" , "MEDIAN BLUR" , "GAUSSIAN BLUR"]
images = [img , filter2D , mean , mblur , gblur]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()