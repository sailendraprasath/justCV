import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)

vertices = np.array([[100,300],[200,200],[400,300],[200,400]],dtype=np.int32)
# # vertices = np.array([[100,300],[200,200],[400,300],[200,400],[100,300]],dtype=np.int32)

pts =vertices.reshape((-1,1,2))

cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=5)
# # cv2.polylines(blank_img,[pts],isClosed=False,color=(255,0,0),thickness=5)



#ithula namma isClosed=false kuduthu 5 array eduthu kuda polygonal shape konduvaralam

plt.imshow(blank_img)
plt.show()

