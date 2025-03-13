import cv2

# Call back function 
def Draw_rect(event,x,y,flags,params):
    global pt1,pt2,topLeft_clicked,bottomRight_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # rest the rectangle
        if topLeft_clicked == True and bottomRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False
            
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
        elif bottomRight_clicked == False:
            pt2 = (x,y)
            bottomRight_clicked = True


# Global variables
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
bottomRight_clicked = False

# Connect to the call back
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',Draw_rect)
while True:
    ret,frame = cap.read()

    # Drawing on the frame based off the global variable
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame,pt1=pt1,pt2=pt2,color=(0,0,255),thickness=4)

    cv2.imshow('Test',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
