import cv2
import numpy as np


drawing = False
ix = -1
iy = -1

def Draw_Rect(event,x,y,flags,params):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img=img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img=img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=-1)
    

img = np.zeros(shape=(512,512,3))
cv2.namedWindow("My_Draw")
cv2.setMouseCallback("My_Draw",Draw_Rect)


while True:
    cv2.imshow('My_Draw',img)

    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
