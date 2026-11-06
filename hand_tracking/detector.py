


import cv2
import mediapipe as mp
import numpy as np

from types import SimpleNamespace
from pathlib import Path

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandDetector:

    CONNECTIONS = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (5, 9), (9, 10), (10, 11), (11, 12),
        (9, 13), (13, 14), (14, 15), (15, 16),
        (13, 17), (17, 18), (18, 19), (19, 20),
        (0, 17)
    ]

    def __init__(
        self,
        static_mode=False,
        max_hands=1,
        detection_confidence=0.7,
        tracking_confidence=0.7
    ):

        model_path = (
            Path(__file__).resolve().parent.parent
            / "models"
            / "hand_landmarker.task"
        )

        if not model_path.exists():
            raise FileNotFoundError(
                f"Hand model not found: {model_path}"
            )

        self.running_mode = (
            vision.RunningMode.IMAGE
            if static_mode
            else vision.RunningMode.VIDEO
        )

        base_options = python.BaseOptions(
            model_asset_path=str(model_path)
        )

        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=self.running_mode,
            num_hands=max_hands,
            min_hand_detection_confidence=detection_confidence,
            min_hand_presence_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

        self.detector = vision.HandLandmarker.create_from_options(
            options
        )

        self.timestamp_ms = 0

    def detect_hands(self, frame, draw=True):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        rgb_frame = np.ascontiguousarray(rgb_frame)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        if self.running_mode == vision.RunningMode.IMAGE:
            results = self.detector.detect(mp_image)
        else:
            self.timestamp_ms += 33

            results = self.detector.detect_for_video(
                mp_image,
                self.timestamp_ms
            )

        # Adapt Tasks API results to the format used by
        # the existing drawing and gesture modules.
        converted_hands = []

        for hand in results.hand_landmarks:

            converted_hands.append(
                SimpleNamespace(landmark=hand)
            )

        compatible_results = SimpleNamespace(
            multi_hand_landmarks=converted_hands
        )

        if draw:
            self.draw_landmarks(frame, compatible_results)

        return frame, compatible_results

    def draw_landmarks(self, frame, results):

        height, width, _ = frame.shape

        for hand in results.multi_hand_landmarks:

            points = []

            for landmark in hand.landmark:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                points.append((x, y))

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (255, 0, 180),
                    cv2.FILLED
                )

            for start, end in self.CONNECTIONS:

                cv2.line(
                    frame,
                    points[start],
                    points[end],
                    (255, 255, 255),
                    2
                )

    def close(self):
        self.detector.close()
