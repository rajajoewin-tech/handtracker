
import cv2

from drawing.canvas import DrawingCanvas
from drawing.brush import Brush
from drawing.colors import DEFAULT_COLOR

canvas = DrawingCanvas(1280, 720)
brush = Brush(DEFAULT_COLOR, 8)

def mouse_draw(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        brush.reset()

    elif event == cv2.EVENT_MOUSEMOVE:

        if flags & cv2.EVENT_FLAG_LBUTTON:
            brush.draw(canvas.get_canvas(), (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        brush.reset()


cv2.namedWindow("Drawing Test")
cv2.setMouseCallback("Drawing Test", mouse_draw)

while True:

    cv2.imshow("Drawing Test", canvas.get_canvas())

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        canvas.clear()
        brush.reset()

    elif key == ord('q'):
        break

cv2.destroyAllWindows()

