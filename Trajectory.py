import time
from fitting import solvePara

class Trajectory:
    def __init__(self, init_circle):
        self.circles = [init_circle]
        self.predicted_profile = None
        self.lastUpdateTime = time.time()
        self.fittingParams = [0, 0, 0]
    def getLatestCircle(self):
        return self.circles[-1]

    def includeCircle(self, new_circle):
        self.circles.append(new_circle)
        self.lastUpdateTime = time.time()

    def fitCurve(self):
        X = [circle.x for circle in self.circles]
        Y = [circle.y for circle in self.circles]
        if len(X) >= 3:
            a, b, c = solvePara(X, Y, self.fittingParams)
            self.fittingParams = [a, b, c]
        elif len(X) == 2:
            m, b = solvePara(X, Y, self.fittingParams)
            self.fittingParams = [0, m, b]
        elif len(X) <= 1:
            return 
    def withinRange(self, new_circle):
        return True
