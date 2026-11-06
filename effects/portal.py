
import cv2
import math


class PortalEffect:

    def __init__(self):
        self.frame_count = 0

    def apply(self, frame, center, radius=70):

        self.frame_count += 1

        overlay = frame.copy()

        pulse = int(
            8 * math.sin(self.frame_count * 0.1)
        )

        for i in range(3):

            current_radius = radius + pulse + (i * 15)

            cv2.circle(
                overlay,
                center,
                current_radius,
                (255, 0, 180),
                2,
                cv2.LINE_AA
            )

        glow = cv2.GaussianBlur(
            overlay,
            (31, 31),
            0
        )

        frame[:] = cv2.addWeighted(
            frame, 0.7,
            glow, 0.8,
            0
        )

        return frame
