
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import math
from ball_detection import findCircles
from ball_identify import findID, clusterCircle, removeTrajectory
cap = cv2.VideoCapture('AOB.mp4')
play = 1
cnt = 0
circles = []
buffer = []
plt.ion()
plt.title("Real Time plot")
plt.xlabel("x")
plt.ylabel("y")
while(cap.isOpened()):

    if (play):
        ret, frame = cap.read()
        height, width = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        stats = frame.copy()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        new_circles = findCircles(frame)  # return found circles' position and their color in current frame.

        if new_circles is not None:
            for new_circle in new_circles:
                # Add new found circles to buffer.
                clusterCircle(buffer, new_circle)
                removeTrajectory(buffer, reason="old")
                removeTrajectory(buffer, reason="onGround")
                ID = findID(new_circle, circles, height, width)
                circles.append(new_circle)
                if len(circles) >= 150:
                    circles.pop(0)

        for circle in circles:
            # Draw all circles stored in the buffer.
            cv2.circle(frame, (circle.x, circle.y), 1, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 3)
            cv2.putText(frame, str(circle.x) + ", " + str(circle.y) + ", r" + str(circle.radius), (circle.x + 5, circle.y + 5), cv2.FONT_HERSHEY_SIMPLEX,  0.5, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        for index, trajectory in enumerate(buffer):
            a, b, c = trajectory.fittingParams
            for circle in trajectory.circles:
                # cv2.circle(stats, (circle.x, circle.y), 1, (0, 0, 0), 3)
                # cv2.putText(stats, str(trajectory.onGround), (circle.x + 5, circle.y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                parabola_y = int(a * circle.x * circle.x + b * circle.x + c)
                # cv2.circle(stats, (circle.x, parabola_y), 1, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 3)

        # show predicted parabola.
        for trajectory in buffer:
            a, b, c = trajectory.fittingParams
            x = trajectory.getLatestCircle().x
            ground_height = 530
            first_bounded_point = (0, 0)
            first_bounded = False
            if trajectory.xDirection > 0:
                hills_cnt = 0
                while x < width:
                    parabola_y = int(a * x * x + b * x + c)
                    x = x + 1
                    if parabola_y > ground_height - trajectory.getLatestCircle().radius:
                        # onBound
                        if not first_bounded:
                            first_bounded_point = (x, parabola_y)
                            first_bounded = True
                        D = b * b - 4 * a * (c - ground_height + trajectory.getLatestCircle().radius)
                        if D < 0:
                            continue
                        hill_distance = (math.sqrt(D))/a
                        hills_cnt = math.floor((x - first_bounded_point[0]) / hill_distance) + 1
                        # hills_cnt = 2
                        parabola_y = int(a * (x-hill_distance * hills_cnt) * (x-hill_distance * hills_cnt) + b * (x-hill_distance * hills_cnt) + c)
                    if parabola_y > height:
                        continue
                    cv2.circle(stats, (x, parabola_y), 1, (trajectory.getLatestCircle().rgb['B'], trajectory.getLatestCircle().rgb['G'], trajectory.getLatestCircle().rgb['R']))
            elif trajectory.xDirection < 0:
                while x > 0:
                    parabola_y = int(a * x * x + b * x + c)
                    x = x - 1
                    if parabola_y > ground_height - trajectory.getLatestCircle().radius:
                        # onBound
                        if not first_bounded:
                            first_bounded_point = (x, parabola_y)
                            first_bounded = True
                        D = b * b - 4 * a * (c - ground_height + trajectory.getLatestCircle().radius)
                        if D < 0:
                            continue
                        hill_distance = (math.sqrt(D)) / a
                        hills_cnt = math.floor((first_bounded_point[0] - x) / hill_distance) + 1
                        # hills_cnt = 2
                        parabola_y = int(a * (x + hill_distance * hills_cnt) * (x + hill_distance * hills_cnt) + b * (x + hill_distance * hills_cnt) + c)
                    if parabola_y > height:
                        continue
                    cv2.circle(stats, (x, parabola_y), 1, (trajectory.getLatestCircle().rgb['B'], trajectory.getLatestCircle().rgb['G'], trajectory.getLatestCircle().rgb['R']))

    cv2.imshow('statistics', stats)

    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:  # Esc
        print('break')
        break
    elif key == 13:  # Enter
        print('play / pause')
        play = play ^ 1
    elif key == 32:  # space
        cv2.imwrite('output%s.jpg' % str(cnt), frame)
        cnt += 1

plt.show()
cap.release()
cv2.destroyAllWindows()