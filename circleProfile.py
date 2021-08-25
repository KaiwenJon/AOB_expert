
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
from ball_detection import findCircles
from ball_identify import findID, clusterCircle, removeOldTrajectory
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
                removeOldTrajectory(buffer)
                ID = findID(new_circle, circles, height, width)
                circles.append(new_circle)
                if len(circles) >= 150:
                    circles.pop(0)

        for circle in circles:
            # Draw all circles stored in the buffer.
            cv2.circle(frame, (circle.x, circle.y), 1, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 3)
            cv2.putText(frame, str(circle.x) + str(circle.color) + str(circle.y), (circle.x + 5, circle.y + 5), cv2.FONT_HERSHEY_SIMPLEX,  0.5, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        for index, trajectory in enumerate(buffer):
            a, b, c = trajectory.fittingParams
            for circle in trajectory.circles:
                cv2.circle(stats, (circle.x, circle.y), 1, (0, 0, 0), 3)
                cv2.putText(stats, str(index), (circle.x + 5, circle.y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                parabola_y = int(a * circle.x * circle.x + b * circle.x + c)
                cv2.circle(stats, (circle.x, parabola_y), 1, (0, 0, 255), 3)
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