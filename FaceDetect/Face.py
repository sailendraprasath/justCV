import cv2
import numpy as np
import matplotlib.pyplot as plt

sailesh = cv2.imread('Sailesh.png',0)
sailesh2 = cv2.imread('19.JPG',0)
grp_img = cv2.imread('grp.jpg',0) #perfect ah intha img tha face ah detect ah pannuthu

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def Detect_Face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
    return face_img
def adj_Detect_Face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
    return face_img


result = Detect_Face(grp_img)
result2 = adj_Detect_Face(sailesh2)
plt.imshow(result2, cmap='gray')
plt.show()