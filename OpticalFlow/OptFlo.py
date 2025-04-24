import cv2
import numpy as np

# Parameters for ShiTomasi corner detection
corner_track_params = dict(
    maxCorners=100,
    qualityLevel=0.3,
    minDistance=7,
    blockSize=7
)

# Parameters for Lucas-Kanade optical flow
lk_params = dict(
    winSize=(200, 200),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

# Start capturing video
cap = cv2.VideoCapture(0)

# Read the first frame
ret, pre_frame = cap.read()
pre_gray = cv2.cvtColor(pre_frame, cv2.COLOR_BGR2GRAY)

# Detect initial good features to track
prevPts = cv2.goodFeaturesToTrack(pre_gray, mask=None, **corner_track_params)

# Create a mask image for drawing
mask = np.zeros_like(pre_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(pre_gray, frame_gray, prevPts, None, **lk_params)

    # Select good points
    good_new = nextPts[status == 1]
    good_prev = prevPts[status == 1]

    # Draw the tracks
    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()

        # Convert to int for drawing
        x_new, y_new, x_prev, y_prev = int(x_new), int(y_new), int(x_prev), int(y_prev)

        mask = cv2.line(mask, (x_new, y_new), (x_prev, y_prev), (0, 255, 0), 3)
        frame = cv2.circle(frame, (x_new, y_new), 8, (0, 0, 255), -1)

    # Overlay mask on frame
    img = cv2.add(frame, mask)

    cv2.imshow('Lucas-Kanade Optical Flow', img)

    # Exit if ESC is pressed
    if cv2.waitKey(30) & 0xFF == 27:
        break

    # Update previous frame and points
    pre_gray = frame_gray.copy()
    prevPts = good_new.reshape(-1, 1, 2)

# Release resources
cap.release()
cv2.destroyAllWindows()
