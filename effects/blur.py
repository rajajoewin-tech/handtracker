
import cv2


class GlowEffect:

    def __init__(self, intensity=1.5, kernel_size=31):
        self.intensity = intensity
        self.kernel_size = kernel_size

    def apply(self, image):

        glow = cv2.GaussianBlur(
            image,
            (self.kernel_size, self.kernel_size),
            0
        )

        result = cv2.addWeighted(
            image, 1.0,
            glow, self.intensity,
            0
        )

        return result
