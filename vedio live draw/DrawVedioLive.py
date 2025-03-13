import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Top left corner 
x = width // 2
y = height // 2

# width and height of rectangle
w = width // 4
h = height // 4

# Bottom right corner x+w , y+h

while True:
    ret,frame = cap.read()

    cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=4)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()