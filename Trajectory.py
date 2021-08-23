import time

class Trajectory:
    def __init__(self, init_circle):
        self.circles = [init_circle]
        self.predicted_profile = None
        self.lastUpdateTime = time.time()


    def getOldestCircle(self):
        return self.circles[0]

    def getLatestCircle(self):
        return self.circles[-1]

    def includeCircle(self, new_circle):
        self.circles.append(new_circle)
        self.lastUpdateTime = time.time()

    def generateProfile(self):
        def fitCenter(circles):
            pass
        pass
    def withinRange(self, new_circle):
        return True
