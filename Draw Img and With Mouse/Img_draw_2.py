import cv2
import numpy as np
import matplotlib.pyplot as plt


blank_img = np.zeros(shape=(512,512,3),dtype=np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text="AI MERN developer sailendra",org=(10,500),fontFace=font,fontScale=1,color=(241,155,111),thickness=3,lineType=cv2.LINE_4)


font2 = cv2.FONT_HERSHEY_PLAIN
cv2.putText(blank_img,text="i'am unstoppable",org=(10,100),fontFace=font2, fontScale=3,color=(255,255,255),thickness=2,lineType=cv2.LINE_8)

font3 = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(blank_img,text="i can do",org=(10,250),fontFace=font3,fontScale=3,color=(0,255,0),thickness=3,lineType=cv2.LINE_AA)


plt.imshow(blank_img)
plt.show()

