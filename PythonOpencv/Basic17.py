#แสดงพิกัดด้วย Mouse Event
import cv2
import numpy
img = cv2.imread("image/cat.jpg")

def clickPosition(event, x , y , flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        imgcolor = numpy.zeros([300,300,3] , numpy.uint8)
        imgcolor[:] = [blue,green,red]
        cv2.imshow("Result" , imgcolor)

cv2.imshow("Output",img)
#ทำงานกับ Mouse
cv2.setMouseCallback("Output" , clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()