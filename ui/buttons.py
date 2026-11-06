
import cv2


class Button:

    def __init__(self, x, y, width, height, label,
                 color=(180, 0, 255)):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.color = color

    def draw(self, frame):

        cv2.rectangle(
            frame,
            (self.x, self.y),
            (self.x + self.width, self.y + self.height),
            self.color,
            2,
            cv2.LINE_AA
        )

        cv2.putText(
            frame,
            self.label,
            (self.x + 12, self.y + 32),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

    def is_clicked(self, point):

        px, py = point

        return (
            self.x <= px <= self.x + self.width
            and self.y <= py <= self.y + self.height
        )
