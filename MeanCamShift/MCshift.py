import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_rects = face_cascade.detectMultiScale(frame)
(face_x, face_y, w, h) = face_rects[0]
track_window = (face_x, face_y, w, h)

roi = frame[face_y:face_y+h, face_x:face_x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
#                        Meanshift 
        # ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # x, y, w, h = track_window
        # img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
#                         Camshift
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        x, y, w, h = track_window
        pts = cv2.boxPoints(ret)
        pts = np.intp(pts)
        img2 = cv2.polylines(frame, [pts], True, (0, 0, 255), 5)
        cv2.putText(img2, "CamShift", (x, y - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#

        
        cv2.imshow("MeanShift", img2)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
