import cv2

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img , (700,700))


#วาดข้อความบนภาพ
# puttext(ภาพ , ข้อความ , พิจัดที่จะแสดง (x,y) ,font , ขนาดข้อความ , สี , ความหนา)

cv2.putText(imgresize , "TIRAWAT" , (50,50) , 4 , 1.5 , (255,0,0) , 4)

cv2.imshow("Output" , imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
