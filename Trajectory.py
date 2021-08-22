class Trajectory:
    def __init__(self, init_circle):
        self.circles = [init_circle]
        self.predicted_profile = None

    def getRootCircle(self):
        return self.circles[0]

    def includeCircle(self, new_circle):
        self.circles.append(new_circle)

    def generateProfile(self):
        def fitCenter(circles):
            pass
        pass
