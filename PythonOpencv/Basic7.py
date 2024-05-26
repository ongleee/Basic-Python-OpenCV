#การวิดิโอ
import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read()#รับภาพจากกล้อง

    if check == True:#เช็คว่าวิดิโอเล่นอยู่มั้ย
        cv2.imshow("Output" , frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):#กดตัวeปิด
            break
    else:#ถ้าจบให้ปิด
        break

cap.release()
cv2.destroyAllWindows()