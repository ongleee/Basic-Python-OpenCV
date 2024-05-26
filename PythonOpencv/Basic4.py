import cv2
img = cv2.imread("image/cat.jpg",0) #กำหนดรูปแบบภาพ
imgresize = cv2.resize(img , (400,400))#ปรับขนาดภาพ

#แสดงภาพ
cv2.imshow("Output" , imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()