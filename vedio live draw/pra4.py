import cv2 

def Draw_Rect(event,x,y,flags,params):
    global pt1,pt2,topleft,bottomright

    if event == cv2.EVENT_LBUTTONDOWN:
        if topleft == True and bottomright == True:
             pt1 = (0,0)
             pt2 = (0,0)
             topleft = False
             bottomright = False
        if topleft == False:
            pt1 = (x,y)
            topleft = True
        elif bottomright == False:
            pt2 = (x,y)
            bottomright = True





pt1 = (0,0)
pt2 = (0,0)
topleft = False
bottomright = False


cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',Draw_Rect)


while True:
    ret,frame = cap.read()

    if topleft:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=4)
    if bottomright:
        cv2.rectangle(frame,pt1=pt1,pt2=pt2,color=(0,0,255),thickness=4)
    
    cv2.imshow('Test',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()
