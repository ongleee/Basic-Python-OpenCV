#แสดงพิกัดด้วย Mouse Event
import cv2
img = cv2.imread("image/cat.jpg")

def clickPosition(event, x , y , flags , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        Text = str(x) + "," + str(y)
        cv2.putText(img , Text , (x,y) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , cv2.LINE_4)
        cv2.imshow("Output" , img)

cv2.imshow("Output",img)
#ทำงานกับ Mouse
cv2.setMouseCallback("Output" , clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()