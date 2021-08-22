import matplotlib.pyplot as plt
import numpy as np

def clusterCircle(buffer, circle):
    for candidate in buffer:
        if circle['colorName'] != candidate['colorName']:
            # Different color, definitely not the same balls.
            continue
        elif abs(circle['radius'] - candidate['radius']) >= 7:
            # Too far way, obviously not the same balls.
            continue
        elif abs(circle['pos'][0] - candidate['pos'][0]) >= 15 or abs(circle['pos'][1] - candidate['pos'][1]) >= 40:
            # Adjacent center cannot be farther than x: 15, y: 40
            continue

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