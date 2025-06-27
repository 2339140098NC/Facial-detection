import cv2 as cv

img = cv.imread("new-features-B.jpg")

#cordinate
x,y,w,h = 100, 100, 100, 100
#draw the rectangle
cv.rectangle(img,(x,y,x+w,y+h), color=(0,0,255),thickness = 1)
#draw the circle
cv.circle(img, center=(x+w,y+h), radius = 100, color=(255,0,0), thickness = 2 )
#display
cv.imshow('re_img', img)

while True:
    if ord('q')==cv.waitKey(0):
        break
#free memory
cv.destroyAllWindows()