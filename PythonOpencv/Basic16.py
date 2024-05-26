#แสดงพิกัดด้วย Mouse Event
import cv2
img = cv2.imread("image/cat.jpg")

def clickPosition(event, x , y , flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        Text = str(blue) + "," + str(green) + "," + str(red)
        cv2.putText(img , Text , (x,y) , cv2.FONT_HERSHEY_COMPLEX , 0.8 , (0,255,0) , cv2.LINE_4)
        cv2.imshow("Output" , img)

cv2.imshow("Output",img)
#ทำงานกับ Mouse
cv2.setMouseCallback("Output" , clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()