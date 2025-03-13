import cv2
import numpy as np
import matplotlib.pyplot as plt


blank_img = np.zeros(shape=(512,512,3),dtype=np.uint8)



cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,250),color=(0,255,0),thickness=10)
cv2.rectangle(blank_img,pt1=(380,10),pt2=(500,150),color=(0,250,0),thickness=-1)

cv2.circle(img=blank_img,center=(100,300),radius=50,color=(0,250,255),thickness=10)
cv2.circle(img=blank_img,center=(400,400),radius=50,color=(250,0,0),thickness=-1)


cv2.line(img=blank_img,pt1=(0,0),pt2=(512,512),color=(100,255,200),thickness=3)

plt.imshow(blank_img)

plt.show()