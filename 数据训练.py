import os
import cv2
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    #存储人脸数据
    faceSamples = []
    #存储姓名数据
    ids = []
    #存储图片信息
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    #加载分类器
    face_detector = cv2.CascadeClassifier("D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml")
    #遍历列表中的图片
    for imagePath in imagePaths:
        #打开图片，灰度化PIL有九种不同模式： 1,L,P,RGB,RGBA,CMYK,YCbCr,I,F.
        PIL_img = Image.num(imagePath).convert('L')
        #将图像转换为数组， 以黑白深浅
        img_numpy = np.array(PIL_img,'uint8')
        #获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
        #获取每张照片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.'))
        #预防无面容照片
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
    print('id: ', id)
    print('fs: ', facesSamples)
    return facesSamples,ids

if __name__ == '__main__':
    #图片路径
    path='D:/opencv/trainer/faces'
    #获取图像数组和id标签数组和姓名
    faces,ids = getImageAndLabels(path)
    #加载识别器
    recognizer = cv2.face.LBPHFFaceRecognizer_create()
    #训练s
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('trainer/trainer.yml')

























