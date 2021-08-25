import matplotlib.pyplot as plt
import numpy as np
from Trajectory import Trajectory
import time
def clusterCircle(buffer, circle):
    hasBeenIncluded = False
    for trajectory in buffer:
        if circle.color != trajectory.getLatestCircle().color:
            # Different color, definitely not in same trajectory.
            continue
        elif abs(np.int16(circle.radius) - np.int16(trajectory.getLatestCircle().radius)) >= 7:
            # Size differs a lot, obviously not in same trajectory.
            continue
        elif abs(np.int16(circle.x) - np.int16(trajectory.getLatestCircle().x)) >= 15 or abs(np.int16(circle.y) - np.int16(trajectory.getLatestCircle().y)) >= 40:
            # Adjacent center cannot be too far.
            continue
        elif not trajectory.withinRange(circle):
            # not within predicted profile
            continue
        else:
            # New circle can be included in this existed trajectory.
            trajectory.includeCircle(circle)
            trajectory.fitCurve()
            hasBeenIncluded = True

    if not hasBeenIncluded:
        # A new trajectory is created.
        trajectory = Trajectory(init_circle=circle)
        buffer.append(trajectory)

def removeOldTrajectory(buffer):
    # Only leave those trajectories whose last update time are not too long ago.
    buffer[:] = [trajectory for trajectory in buffer if not(time.time()-trajectory.lastUpdateTime >= 1)]





def findID(newCircle, historyCircles, height, width):

    # if colorName == 'red':
    #     plt.scatter(1, radius, c=[[R/255, G/255, B/255]])
    # elif colorName == 'blue':
    #     plt.scatter(2, radius, c=[[R / 255, G / 255, B / 255]])
    # elif colorName == 'green':
    #     plt.scatter(3, radius, c=[[R / 255, G / 255, B / 255]])
    # elif colorName == 'yellow':
    #     plt.scatter(4, radius, c=[[R / 255, G / 255, B / 255]])
    # elif colorName == 'purple':
    #     plt.scatter(5, radius, c=[[R / 255, G / 255, B / 255]])
    # plt.scatter(center[0], height-center[1], linewidths=radius/50, c=[[B/255, G/255, R/255]])
    # plt.pause(0.005)
    return 1
# x=0
# for i in range(100):
#     x=x+0.04
#     y = np.sin(x)
#     plt.scatter(x, y)
#     plt.title("Real Time plot")
#     plt.xlabel("x")
#     plt.ylabel("sinx")
#     plt.pause(0.05)
# print("run here")
# plt.show()