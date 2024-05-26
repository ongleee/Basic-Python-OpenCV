import cv2

img = cv2.imread("image/boy.jpg")

#อ่านไฟล์สำหรับ classification
face_casecade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)#ทำภาพเป็นขาวดำ

#จำแนกใบหน้า
face_detect = face_casecade.detectMultiScale(gray_img , scaleFactor=1.1 , minNeighbors=3)

# scaleFactor ความแม่นยำ minNeighbors ทำซำ้กี่รอบที่เจอใบหน้า

#แสดงตำแหน่งที่เจอใบหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , 3)
0
cv2.imshow("Original" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()