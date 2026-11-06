
import cv2
import numpy as np

from ui.toolbar import Toolbar
from ui.text import TextRenderer

WIDTH = 1280
HEIGHT = 720

toolbar = Toolbar()
text_renderer = TextRenderer()

frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

selected_action = None


def mouse_callback(event, x, y, flags, param):

    global selected_action

    if event == cv2.EVENT_LBUTTONDOWN:

        selected_action = toolbar.handle_click((x, y))

        if selected_action:
            print("Selected:", selected_action)
            text_renderer.set_status(selected_action)


cv2.namedWindow("AI Magic Drawing - UI")

cv2.setMouseCallback(
    "AI Magic Drawing - UI",
    mouse_callback
)

while True:

    frame[:] = (15, 5, 25)

    toolbar.draw(frame)

    text_renderer.draw(frame)

    cv2.imshow("AI Magic Drawing - UI", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows()
