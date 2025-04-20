import cv2
import numpy as np  
import matplotlib.pyplot as plt

img = cv2.imread('dogImg.png')
edge = cv2.Canny(img,threshold1=127,threshold2=127)
med_val = np.median(img)

lower = int(max(0,0.7*med_val))
upper = int(min(255,1.3*med_val))

edge2 = cv2.Canny(img,lower,upper+100)

blur_img = cv2.blur(edge2,(5,5))

edge3 = cv2.Canny(blur_img,lower,upper+50)
plt.imshow(edge3)

plt.show()