
import cv2
import random
import math


class LightningEffect:

    def apply(self, frame, start, end):

        overlay = frame.copy()

        x1, y1 = start
        x2, y2 = end

        points = []

        segments = 12

        for i in range(segments + 1):

            t = i / segments

            x = int(x1 + (x2 - x1) * t)
            y = int(y1 + (y2 - y1) * t)

            if i != 0 and i != segments:
                x += random.randint(-10, 10)
                y += random.randint(-10, 10)

            points.append((x, y))

        for i in range(len(points) - 1):

            cv2.line(
                overlay,
                points[i],
                points[i + 1],
                (255, 0, 180),
                3,
                cv2.LINE_AA
            )

        glow = cv2.GaussianBlur(
            overlay,
            (21, 21),
            0
        )

        frame[:] = cv2.addWeighted(
            frame, 0.7,
            glow, 0.8,
            0
        )

        return frame
