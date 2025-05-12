# import cv2
# from util import get_limits
# from PIL import Image

# cap = cv2.VideoCapture(0)
# yellow = [0,255,255] #yellow in BGR color space
# while True:
#     ret, frame = cap.read()
    

#     hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     lowerlimit, upperlimit = get_limits(color=yellow)

#     mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)
#     mask_ = Image.fromarray(mask)
#     bbox = mask_.getbbox()
#     if bbox is not None:
#         x1, y1, x2, y2 = bbox
#         frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)
       
#     cv2.imshow('Frame',frame)

#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
from util import get_limits
from PIL import Image

cap = cv2.VideoCapture(0)
yellow = [0,255,255] #yellow in BGR color space
while True:
    ret, frame = cap.read()
    

    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerlimit, upperlimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)
       
    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

