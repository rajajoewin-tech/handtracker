
import cv2

from ui.buttons import Button


class Toolbar:

    def __init__(self):

        self.buttons = [

            Button(20, 20, 110, 45, "CLEAR"),
            Button(145, 20, 110, 45, "ERASER"),
            Button(270, 20, 110, 45, "SAVE"),

            Button(405, 20, 100, 45, "PURPLE"),
            Button(520, 20, 100, 45, "BLUE"),
            Button(635, 20, 100, 45, "GREEN")
        ]

    def draw(self, frame):

        cv2.rectangle(
            frame,
            (0, 0),
            (frame.shape[1], 85),
            (35, 15, 45),
            -1
        )

        for button in self.buttons:
            button.draw(frame)

    def handle_click(self, point):

        for button in self.buttons:

            if button.is_clicked(point):
                return button.label

        return None
