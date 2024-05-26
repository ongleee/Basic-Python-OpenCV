import cv2

cap = cv2.VideoCapture("image/Mark.mp4")

#อ่านไฟล์สำหรับ classification
face_casecade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        #จำแนกใบหน้า
        face_detect = face_casecade.detectMultiScale(gray_img , scaleFactor=1.5 , minNeighbors=5)
        #แสดงตำแหน่งที่เจอใบหน้า
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , 3)
            cv2.imshow("Output" , frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()