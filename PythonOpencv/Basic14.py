#แสดงวันเวลาในกล้อง/วิดิโอ
import cv2
import datetime

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read()#รับภาพจากวิดิโอ

    if check == True:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame , currentDate , (10,30) , 2 , 1 , (0,0,0) , 4)
        cv2.imshow("Output" , frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
        