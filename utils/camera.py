import cv2
import config


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(config.CAMERA_ID)

        if not self.cap.isOpened():
            raise RuntimeError("Unable to open webcam!")

        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            config.FRAME_WIDTH
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            config.FRAME_HEIGHT
        )

    def read(self):

        success, frame = self.cap.read()

        if not success:
            return None

        if config.MIRROR_CAMERA:
            frame = cv2.flip(frame, 1)

        return frame

    def release(self):

        if self.cap is not None:
            self.cap.release()