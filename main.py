import cv2

import config

from utils.camera import Camera
from utils.fps import FPSCounter


class MagicDrawingApp:

    def __init__(self):

        self.camera = Camera()
        self.fps_counter = FPSCounter()

        self.running = True

    def draw_interface(self, frame, fps):

        # Application title
        cv2.putText(
            frame,
            "AI MAGIC DRAWING",
            (30, 50),
            cv2.FONT_HERSHEY_DUPLEX,
            1.2,
            config.PURPLE,
            2
        )

        # FPS counter
        if config.SHOW_FPS:

            cv2.putText(
                frame,
                f"FPS: {fps}",
                (30, 95),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                config.GREEN,
                2
            )

        # Instructions
        cv2.putText(
            frame,
            "Press ESC to Exit",
            (30, frame.shape[0] - 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            config.WHITE,
            2
        )

        return frame

    def run(self):

        print("AI Magic Drawing Started!")
        print("Press ESC to exit.")

        try:

            while self.running:

                frame = self.camera.read()

                if frame is None:
                    print("Unable to read webcam frame.")
                    break

                fps = self.fps_counter.update()

                frame = self.draw_interface(frame, fps)

                cv2.imshow(config.WINDOW_NAME, frame)

                key = cv2.waitKey(1) & 0xFF

                if key == 27:
                    self.running = False

        finally:

            self.camera.release()

            cv2.destroyAllWindows()

            print("AI Magic Drawing Closed.")


if __name__ == "__main__":

    app = MagicDrawingApp()

    app.run()