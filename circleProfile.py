
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
from ball_detection import findCircles
from ball_identify import findID, clusterCircle
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
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        new_circles = findCircles(frame)  # return found circles' position and their color in current frame.
        if new_circles is not None:
            for new_circle in new_circles:
                # Add new found circles to buffer.
                # clusterCircle(buffer, new_circle)
                ID = findID(new_circle, circles, height, width)
                circles.append(new_circle)
                if len(circles) >= 400:
                    circles.pop(0)
        for circle in circles:
            # Draw all circles stored in the buffer.
            cv2.circle(frame, (circle.x, circle.y), 1, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 3)
            cv2.putText(frame, str(circle.x) + str(circle.color) + str(circle.y), (circle.x + 5, circle.y + 5), cv2.FONT_HERSHEY_SIMPLEX,  0.5, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 1, cv2.LINE_AA)
            cv2.circle(gray, (circle.x, circle.y), 1, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 3)
            cv2.putText(gray, str(1), (circle.x + 5, circle.y + 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (circle.rgb['B'], circle.rgb['G'], circle.rgb['R']), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.imshow('statistics', gray)
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