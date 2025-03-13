import cv2
import numpy as np
import matplotlib.pyplot as plt

#empty img code
blank_img = np.zeros(shape=(512,.512,3),dtype=np.int16)

#polygonal shape code with color
vertices = np.array([[250,100],[350,10],[400,100],[310,400]],dtype=np.int32)
pts = vertices.reshape([-1,1,2])
cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=3)


# img with shape show code 
plt.imshow(blank_img)
plt.show()