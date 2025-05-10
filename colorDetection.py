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
import numpy as np
from PIL import Image

cap = cv2.VideoCapture(0)

# HSV range for blue color
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for blue
    mask = cv2.inRange(hsvImage, lower_blue, upper_blue)

    # Get bounding box using PIL
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('Blue Detection', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
