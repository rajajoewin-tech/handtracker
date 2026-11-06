
import numpy as np
import cv2


class DrawingCanvas:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.canvas = np.zeros(
            (height, width, 3),
            dtype=np.uint8
        )

    def clear(self):

        self.canvas[:] = 0

    def get_canvas(self):

        return self.canvas

    def show_on_frame(self, frame):

        return cv2.add(frame, self.canvas)

