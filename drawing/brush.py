
import cv2


class Brush:

    def __init__(self, color=(255, 0, 180), thickness=8):

        self.color = color
        self.thickness = thickness
        self.previous_point = None

    def draw(self, canvas, point):

        if self.previous_point is not None:

            cv2.line(
                canvas,
                self.previous_point,
                point,
                self.color,
                self.thickness,
                cv2.LINE_AA
            )

        cv2.circle(
            canvas,
            point,
            self.thickness // 2,
            self.color,
            -1,
            cv2.LINE_AA
        )

        self.previous_point = point

    def reset(self):

        self.previous_point = None

    def set_color(self, color):

        self.color = color

    def set_thickness(self, thickness):

        self.thickness = thickness

