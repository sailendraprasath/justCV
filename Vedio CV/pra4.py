import cv2

cap = cv2.VideoCapture(0)

widith = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('secounvedio.mp4',cv2.VideoWriter_fourcc(*'DIVX'),fps=20,frameSize=(widith,height))


while True:
    ret,frame = cap.read()

    writer.write(frame)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()