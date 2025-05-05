import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Initialize MediaPipe Hands and Drawing utils
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Set up webcam capture
cap = cv2.VideoCapture(0)

# Get screen size
screen_w, screen_h = pyautogui.size()

# Variables for double-click detection
last_click_time = 0
click_threshold = 0.3  # Time threshold for double-click in seconds

# Set up the hand detection module
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image = cv2.flip(image, 1)
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get coordinates of index finger tip (landmark 8) and thumb tip (landmark 4)
                h, w, _ = image.shape
                index_finger_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]

                ix, iy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

                # Draw circles
                cv2.circle(image, (ix, iy), 10, (255, 0, 255), -1)
                cv2.circle(image, (tx, ty), 10, (0, 255, 255), -1)

                # Move mouse with index finger
                screen_x = int(index_finger_tip.x * screen_w)
                screen_y = int(index_finger_tip.y * screen_h)
                pyautogui.moveTo(screen_x, screen_y)

                # Calculate distance between thumb and index finger
                distance = math.hypot(tx - ix, ty - iy)

                # Detect double-click: If distance between thumb and index finger is small
                if distance < 30:
                    current_time = time.time()
                    if current_time - last_click_time < click_threshold:
                        # Double-click detected
                        pyautogui.doubleClick()
                        cv2.putText(image, 'Double Click', (ix, iy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    last_click_time = current_time

        cv2.imshow("Hand Tracking - Double Click", image)

        if cv2.waitKey(1) & 0xFF == 27:  # Press Esc to exit
            break

cap.release()
cv2.destroyAllWindows()
