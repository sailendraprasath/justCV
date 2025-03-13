import cv2

cap = cv2.VideoCapture(0)

widith = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while True:
    ret,frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()