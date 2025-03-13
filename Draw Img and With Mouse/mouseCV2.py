import cv2
import numpy as np

def Draw_Circle(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img=img,center=(x,y),radius=100,color=(0,255,0),thickness=-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img=img,center=(x,y),radius=100,color=(255,0,0),thickness=-1)



cv2.namedWindow('My_Draw')
cv2.setMouseCallback('My_Draw',Draw_Circle)
img = np.zeros(shape=(512,512,3))

while True:
    cv2.imshow('My_Draw',img)

    if cv2.waitKey(20) & 0xff == 27:
        break

cv2.destroyAllWindows()