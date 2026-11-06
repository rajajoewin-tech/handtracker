
class GestureDetector:

    @staticmethod
    def is_index_finger_up(hand_landmarks):

        index_tip = hand_landmarks.landmark[8]
        index_pip = hand_landmarks.landmark[6]

        return index_tip.y < index_pip.y

    @staticmethod
    def is_middle_finger_up(hand_landmarks):

        middle_tip = hand_landmarks.landmark[12]
        middle_pip = hand_landmarks.landmark[10]

        return middle_tip.y < middle_pip.y

    @staticmethod
    def get_gesture(hand_landmarks):

        index_up = GestureDetector.is_index_finger_up(
            hand_landmarks
        )

        middle_up = GestureDetector.is_middle_finger_up(
            hand_landmarks
        )

        if index_up and not middle_up:
            return "DRAW"

        elif index_up and middle_up:
            return "MOVE"

        return "STOP"
