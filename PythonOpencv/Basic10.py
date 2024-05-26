import cv2

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img , (700,700))


#วาดเส้นตรง
# line (ภาพ , จุดเริ่มต้น (X,Y)) , จุดสุดท้าย (X,Y), สี (BGR) , ความหนา)
cv2.arrowedLine(imgresize , (0,0) , (500,500) , (255,0,0) , 4)
cv2.arrowedLine(imgresize , (100,100) , (0,0) , (0,255,0) , 4)
cv2.arrowedLine(imgresize , (90,0) , (400,200) , (0,0,255) , 4)

cv2.imshow("Output" , imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
