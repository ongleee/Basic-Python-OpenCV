import cv2

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img , (700,700))


#วาดวงกลม
# circle (ภาพ, จุดศูนย์กลางของวงกลม (x,y) , รัศมี ,สี ,ความหนา)

cv2.circle(imgresize , (350,350) , 100 , (0,255,0), -1)

cv2.imshow("Output" , imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
