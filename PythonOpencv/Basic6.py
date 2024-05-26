#การเปิดกล้อง
import cv2

cap = cv2.VideoCapture(0)

while (True):
    check , frame = cap.read()#รับภาพจากกล้อง
    cv2.imshow("Output" , frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):#กดตัวeปิด
        break

cap.release()
cv2.destroyAllWindows()