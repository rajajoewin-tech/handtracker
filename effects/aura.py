
import cv2
import numpy as np


class AuraEffect:

    def __init__(self):
        self.color = (255, 0, 180)

    def apply(self, frame, point, radius=25):

        overlay = frame.copy()

        cv2.circle(
            overlay,
            point,
            radius,
            self.color,
            -1,
            cv2.LINE_AA
        )

        glow = cv2.GaussianBlur(overlay, (31, 31), 0)

        frame[:] = cv2.addWeighted(
            frame, 0.7,
            glow, 0.8,
            0
        )

        cv2.circle(
            frame,
            point,
            5,
            (255, 255, 255),
            -1,
            cv2.LINE_AA
        )

        return frame
