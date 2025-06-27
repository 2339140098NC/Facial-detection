import cv2 as cv

def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    faces = face_detect.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

# Replace the 0 with your video file path
cap = cv.VideoCapture('D:/opencv/trainer/199623-910995789_tiny.mp4')  # 👈 change to your actual video file path

while True:
    flag, frame = cap.read()
    if not flag:  # if video ends or cannot read frame
        break
    face_detect_demo(frame)  # detect human faces in current frame
    if ord('q') == cv.waitKey(30):  # adjust delay as needed (30ms ~ 33fps)
        break

# release resources
cap.release()
cv.destroyAllWindows()