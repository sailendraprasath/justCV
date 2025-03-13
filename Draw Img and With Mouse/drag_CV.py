import cv2
import numpy as np

#Variables
#True while mouse button down , False while mouse button up
drawing = False 
ix = -1
iy = -1

#Function
def Draw_Rect(event,x,y,flags,params):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img=img,pt1=(ix,iy),pt2=(x,y),color=(0,255,0),thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img=img,pt1=(ix,iy),pt2=(x,y),color=(0,255,0),thickness=-1)



#Showimg the image
img = np.zeros(shape=(512,512,3)) #it will black clr window
cv2.namedWindow(winname='Drag_CV')
cv2.setMouseCallback('Drag_CV',Draw_Rect)


while True :
    cv2.imshow('Drag_CV',img)

    if cv2.waitKey(1) & 0xff == 27:
        break
cv2.destroyAllWindows()