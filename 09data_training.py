import os
import cv2
import sys
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    facesSamples=[]
    ids=[]
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #detecing human face
    face_detector = cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    #print the list imagePaths
    print('data arrangement：',imagePaths)
    #traverse all pics in the list
    for imagePath in imagePaths:
        #open the pic, convert to B&W
        PIL_img=Image.open(imagePath).convert('L')
        #convert the image to list
       # PIL_img = cv2.resize(PIL_img, dsize=(400, 400))
        img_numpy=np.array(PIL_img,'uint8')
        #get the features of human face
        faces = face_detector.detectMultiScale(img_numpy)
        #get the ids and names of each image
        id = int(os.path.split(imagePath)[1].split('.')[0])
        #avoid no human face
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
        #print facial features and name
        #print('fs:', facesSamples)
        print('id:', id)
        #print('fs:', facesSamples[id])
    print('fs:', facesSamples)
    #print('脸部例子：',facesSamples[0])
    #print('身份信息：',ids[0])
    return facesSamples,ids

if __name__ == '__main__':
    #image path
    path='D:/opencv/trainer/faces'
    #get the image list and id labels list and names and name
    faces,ids=getImageAndLabels(path)
    #Get the training objects
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    #recognizer.train(faces,names)#np.array(ids)
    recognizer.train(faces,np.array(ids))
    #save file
    recognizer.write('trainer/trainer.yml')
    #save_to_file('names.txt',names)




