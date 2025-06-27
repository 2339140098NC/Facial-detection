import cv2 as cv

img = cv.imread("new-features-B.jpg")
#transform into grayscale
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)#first element stores the the variable that we want to transform. second parameter is to change the peo
#show grauscale image
cv.imshow('gray',gray_img)
#save the grayscale image
cv.imwrite('gray_face11.jpg', gray_img)


#show the image
cv.imshow('read_img', img)
#wait
cv.waitKey(0)
#free memory
cv.destroyAllWindows()