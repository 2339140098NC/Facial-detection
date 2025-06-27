import cv2 as cv
img = cv.imread("new-features-B.jpg")

#fix the size
resize_img = cv.resize(img, dsize = (200,200))
#show the original image
cv.imshow('resize_img', resize_img)
#show the one that has been fixed
print("unmodified", img.shape)
#print the size of the one that been modified
print("modified", resize_img.shape)

//press q to quit
while True:
    if ord('q')==cv.waitKey(0):
        break

#free ram
cv.destroyAllWindows()