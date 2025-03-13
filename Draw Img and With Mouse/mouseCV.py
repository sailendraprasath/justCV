import cv2
import numpy as np

##############
## FUNCTION ##
##############

def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,center=(x,y),radius=100,color=(155,135,111),thickness=-1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

################################
### SHOWING IMG WITH OPEN CV ###
################################

img = np.zeros((512,512,3),dtype=np.int8)

while True:
    cv2.imshow('my_drawing',img)

    if cv2.waitKey(20) & 0xFF == 27 :
        break
cv2.destroyAllWindows()