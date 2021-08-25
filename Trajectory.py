import time
from fitting import solvePara
import numpy as np

class Trajectory:
    def __init__(self, init_circle):
        self.circles = [init_circle]
        self.predicted_profile = None
        self.lastUpdateTime = time.time()
        self.fittingParams = [0, 0, 0]
        self.xDirection = 0
        self.lastYDirection = 0
        self.yDirection = 0
        self.onGround = False
    def getLatestCircle(self):
        return self.circles[-1]

    def includeCircle(self, new_circle):
        self.xDirection = np.sign(np.int16(new_circle.x) - np.int16(self.getLatestCircle().x))
        self.yDirection = np.sign(np.int16(new_circle.y) - np.int16(self.getLatestCircle().y))
        # print(self.yDirection, self.lastYDirection)
        if self.yDirection * self.lastYDirection < 0 and self.getLatestCircle().y > 530 - self.getLatestCircle().radius:
            self.onGround = True
        self.lastYDirection = self.yDirection
        self.circles.append(new_circle)
        self.lastUpdateTime = time.time()

    def fitCurve(self):
        X = [circle.x for circle in self.circles]
        Y = [circle.y for circle in self.circles]
        if len(X) >= 3:
            a, b, c = solvePara(X, Y, self.fittingParams)
            self.fittingParams = [a, b, c]
        elif len(X) <= 2:
            return 
    def withinRange(self, new_circle):
        return True
