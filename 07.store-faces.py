import cv2

#read cam
cap = cv2.VideoCapture(0)

falg = 1
num = 1

while(cap.isOpened()):#detect cam's status
    ret_flag, Vshow = cap.read()#read image
    cv2.imshow('Capture_test', Vshow)
    k = cv2.waitKey(1) & 0xFF #keyjudgement
    if k == ord('s'):#保存
        cv2.imwrite("D:/opencv/trainer/faces/" + str(num) + ".name" + ".jpg" , Vshow)#store the face of that person in a file
        print("success to save " + str(num) + ".jpg")
        print("----------")
        num += 1
    elif k == ord(" "):
        break

#free camera
cap.release()
#free ram
cv2.destroyAllWindows()