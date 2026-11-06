
class PositionSmoother:

    def __init__(self, alpha=0.35):
        self.alpha = alpha
        self.previous_point = None

    def smooth(self, current_point):

        if self.previous_point is None:
            self.previous_point = current_point
            return current_point

        x = int(
            self.alpha * current_point[0] +
            (1 - self.alpha) * self.previous_point[0]
        )

        y = int(
            self.alpha * current_point[1] +
            (1 - self.alpha) * self.previous_point[1]
        )

        self.previous_point = (x, y)

        return x, y

    def reset(self):
        self.previous_point = None
