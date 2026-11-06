
import cv2
import os
from pathlib import Path

# Hand tracking
from hand_tracking.detector import HandDetector
from hand_tracking.landmarks import HandLandmarks
from hand_tracking.gesture import GestureDetector

# Drawing
from drawing.canvas import DrawingCanvas
from drawing.brush import Brush
from drawing.colors import (
    PURPLE, BLUE, GREEN, BLACK, DEFAULT_COLOR
)
from drawing.smoother import PositionSmoother

# Effects
from effects.blur import GlowEffect
from effects.aura import AuraEffect
from effects.particles import ParticleEffect
from effects.portal import PortalEffect
from effects.lightning import LightningEffect

# UI
from ui.toolbar import Toolbar
from ui.text import TextRenderer


# -----------------------------------
# CONFIGURATION
# -----------------------------------

WIDTH = 1280
HEIGHT = 720

PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "output" / "drawings"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------------
# INITIALIZE MODULES
# -----------------------------------

detector = HandDetector()

drawing_canvas = DrawingCanvas(WIDTH, HEIGHT)

brush = Brush(
    color=DEFAULT_COLOR,
    thickness=8
)

smoother = PositionSmoother(alpha=0.35)

glow = GlowEffect(intensity=1.5)
aura = AuraEffect()
particles = ParticleEffect()
portal = PortalEffect()
lightning = LightningEffect()

toolbar = Toolbar()
text_renderer = TextRenderer()


# -----------------------------------
# APPLICATION STATE
# -----------------------------------

drawing_enabled = False
selected_action = None

previous_point = None


# -----------------------------------
# MOUSE CALLBACK
# -----------------------------------

def mouse_callback(event, x, y, flags, param):

    global selected_action

    if event == cv2.EVENT_LBUTTONDOWN:

        selected_action = toolbar.handle_click((x, y))


# -----------------------------------
# SAVE DRAWING
# -----------------------------------

def save_drawing():

    filename = OUTPUT_DIR / "magic_drawing.png"

    cv2.imwrite(
        str(filename),
        drawing_canvas.get_canvas()
    )

    print(f"Drawing saved: {filename}")


# -----------------------------------
# HANDLE TOOLBAR ACTIONS
# -----------------------------------

def handle_toolbar_action(action):

    global selected_action

    if action == "CLEAR":

        drawing_canvas.clear()
        brush.reset()
        print("Canvas cleared")

    elif action == "ERASER":

        brush.set_color(BLACK)
        print("Eraser selected")

    elif action == "SAVE":

        save_drawing()

    elif action == "PURPLE":

        brush.set_color(PURPLE)

    elif action == "BLUE":

        brush.set_color(BLUE)

    elif action == "GREEN":

        brush.set_color(GREEN)

    selected_action = None


# -----------------------------------
# MAIN APPLICATION
# -----------------------------------

def main():

    global drawing_enabled, previous_point

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        print("ERROR: Webcam not detected")
        detector.close()
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    window_name = "AI MAGIC DRAWING"

    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)

    print("AI MAGIC DRAWING STARTED")
    print("Press Q to quit")
    print("Press C to clear")
    print("Press S to save")

    try:

        while True:

            success, frame = cap.read()

            if not success:
                print("Camera frame not received")
                break

            frame = cv2.resize(frame, (WIDTH, HEIGHT))
            frame = cv2.flip(frame, 1)

            # -------------------------------
            # HAND DETECTION
            # -------------------------------

            frame, results = detector.detect_hands(
                frame,
                draw=True
            )

            point = None
            gesture = "STOP"

            if results.multi_hand_landmarks:

                hand = results.multi_hand_landmarks[0]

                point = HandLandmarks.get_point(
                    results,
                    frame.shape
                )

                gesture = GestureDetector.get_gesture(hand)

            # -------------------------------
            # DRAWING LOGIC
            # -------------------------------

            if point:

                point = smoother.smooth(point)

                aura_result = aura.apply(
                    frame,
                    point,
                    radius=30
                )

                if aura_result is not None:
                    frame = aura_result

                particles.emit(point, count=2)

                if gesture == "DRAW":

                    drawing_enabled = True

                    brush.draw(
                        drawing_canvas.get_canvas(),
                        point
                    )

                    previous_point = point

                else:

                    drawing_enabled = False
                    previous_point = None

                # Portal effect when both fingers are raised
                if gesture == "MOVE":

                    portal_result = portal.apply(
                        frame,
                        center=point,
                        radius=70
                    )

                    if portal_result is not None:
                        frame = portal_result

            else:

                drawing_enabled = False
                previous_point = None
                smoother.reset()

            # -------------------------------
            # PARTICLE EFFECT
            # -------------------------------

            particle_result = particles.update(frame)

            if particle_result is not None:
                frame = particle_result

            # -------------------------------
            # DRAW CANVAS ON CAMERA
            # -------------------------------

            drawing_canvas.show_on_frame(frame)

            # -------------------------------
            # GLOW EFFECT
            # -------------------------------

            glow_result = glow.apply(frame)

            if glow_result is not None:
                frame = glow_result

            # -------------------------------
            # UI
            # -------------------------------

            toolbar.draw(frame)

            text_renderer.set_status(gesture)

            text_renderer.draw(frame)

            # -------------------------------
            # HANDLE MOUSE ACTIONS
            # -------------------------------

            if selected_action:

                handle_toolbar_action(selected_action)

            # -------------------------------
            # DISPLAY
            # -------------------------------

            cv2.imshow(window_name, frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            elif key == ord("c"):

                drawing_canvas.clear()
                print("Canvas cleared")

            elif key == ord("s"):

                save_drawing()

    finally:

        cap.release()
        detector.close()

        cv2.destroyAllWindows()

        print("AI Magic Drawing closed")


# -----------------------------------
# START APPLICATION
# -----------------------------------

if __name__ == "__main__":
    main()
