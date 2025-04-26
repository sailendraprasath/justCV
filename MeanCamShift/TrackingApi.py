import cv2

def ask_for_tacker():
    print("Welcome! What Tracker API would you like to use?")
    print("Enter 0 for BOOSTING")
    print("Enter 1 for MIL")
    print("Enter 2 for KCF")
    print("Enter 3 for TLD")
    print("Enter 4 for MEDIANFLOW")
    choice = input("Please select your tracker: ")

    if choice == '0':
        tracker = cv2.legacy.TrackerBoosting_create()
    elif choice == '1':
        tracker = cv2.legacy.TrackerMIL_create()
    elif choice == '2':
        tracker = cv2.legacy.TrackerKCF_create()
    elif choice == '3':
        tracker = cv2.legacy.TrackerTLD_create()
    elif choice == '4':
        tracker = cv2.legacy.TrackerMedianFlow_create()
    else:
        print("Invalid choice! Defaulting to MIL.")
        tracker = cv2.legacy.TrackerMIL_create()

    return tracker

tracker = ask_for_tacker()
tracker_name = str(tracker).split()[0][1:]

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

roi = cv2.selectROI("Frame", frame, False)
tracker.init(frame, roi)

while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)

    (x, y, w, h) = tuple(map(int, roi))

    if success:
        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)
    else:
        cv2.putText(frame, "Tracking Failure", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    cv2.putText(frame, tracker_name, (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.imshow("Tracking", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
