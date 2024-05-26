import cv2

cap = cv2.VideoCapture("image/Mark.mp4")

#อ่านไฟล์สำหรับ classification
eye_casecade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        #จำแนกใบหน้า
        eye_detect = eye_casecade.detectMultiScale(gray_img , scaleFactor=1.1 , minNeighbors=4)
        #แสดงตำแหน่งที่เจอใบหน้า
        for (x,y,w,h) in eye_detect:
            cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , 3)
            cv2.imshow("Output" , frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()