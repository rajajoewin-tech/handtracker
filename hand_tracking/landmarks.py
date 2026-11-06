
class HandLandmarks:

    WRIST = 0

    THUMB_TIP = 4

    INDEX_FINGER_MCP = 5
    INDEX_FINGER_PIP = 6
    INDEX_FINGER_TIP = 8

    MIDDLE_FINGER_PIP = 10
    MIDDLE_FINGER_TIP = 12

    RING_FINGER_TIP = 16

    PINKY_TIP = 20

    @staticmethod
    def get_point(results, frame_shape, hand_no=0):

        if not results.multi_hand_landmarks:
            return None

        if hand_no >= len(results.multi_hand_landmarks):
            return None

        hand = results.multi_hand_landmarks[hand_no]

        height, width = frame_shape[:2]

        index_tip = hand.landmark[
            HandLandmarks.INDEX_FINGER_TIP
        ]

        x = int(index_tip.x * width)
        y = int(index_tip.y * height)

        return x, y
