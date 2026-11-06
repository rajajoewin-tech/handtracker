
import cv2


class TextRenderer:

    def __init__(self):
        self.title = "AI MAGIC DRAWING"
        self.status = "READY"
        self.instruction = "Use your hand to draw"

    def draw_text(self, frame, text, position,
                  color=(255, 255, 255), scale=0.7):

        cv2.putText(
            frame,
            text,
            position,
            cv2.FONT_HERSHEY_SIMPLEX,
            scale,
            color,
            2,
            cv2.LINE_AA
        )

    def draw(self, frame):

        height, width = frame.shape[:2]

        # Project title
        self.draw_text(
            frame,
            self.title,
            (width - 300, 45),
            (255, 100, 255),
            0.8
        )

        # Status
        self.draw_text(
            frame,
            "STATUS: " + self.status,
            (20, height - 50),
            (0, 255, 150)
        )

        # Instructions
        self.draw_text(
            frame,
            self.instruction,
            (20, height - 20),
            (255, 255, 255),
            0.5
        )

    def set_status(self, status):
        self.status = status

    def set_instruction(self, instruction):
        self.instruction = instruction
