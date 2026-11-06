
import cv2

from hand_tracking.detector import HandDetector
from hand_tracking.gesture import GestureDetector
from hand_tracking.landmarks import HandLandmarks


detector = HandDetector()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not detected")
    detector.close()
    exit()

while True:

    success, frame = cap.read()

    if not success:
        print("Failed to capture frame")
        break

    frame = cv2.flip(frame, 1)

    frame, results = detector.detect_hands(
        frame,
        draw=True
    )

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        point = HandLandmarks.get_point(
            results,
            frame.shape
        )

        gesture = GestureDetector.get_gesture(hand)

        if point:
            cv2.circle(
                frame,
                point,
                12,
                (255, 0, 180),
                cv2.FILLED
            )

        cv2.putText(
            frame,
            f"Gesture: {gesture}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 180),
            2
        )

    cv2.imshow("AI Magic Drawing - Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
detector.close()
cv2.destroyAllWindows()
