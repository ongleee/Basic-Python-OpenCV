#Video GrayScale Mode
import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read()#รับภาพจากกล้อง

    if check == True:#เช็คว่าวิดิโอเล่นอยู่มั้ย
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #เปลี่ยนสีวิดิโอ
        cv2.imshow("Output" , gray)
        if cv2.waitKey(1) & 0xFF == ord("e"):#กดตัวeปิด
            break
    else:#ถ้าจบให้ปิด
        break

cap.release()
cv2.destroyAllWindows()