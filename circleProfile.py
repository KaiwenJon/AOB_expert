
import numpy as np
import cv2
import time
from ball_detection import findCircles
cap = cv2.VideoCapture('AOB.mp4')
play = 1
cnt = 0
circles = []
while(cap.isOpened()):
    if (play):
        ret, frame = cap.read()
        height, width = frame.shape[:2]
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        new_circles = findCircles(frame, show=False)
        if new_circles is not None:
            for new_circle in new_circles:
                circles.append(new_circle)
                if len(circles) >= 150:
                    circles.pop(0)
        for circle in circles:
            # draw profile of centers.
            center = (circle['pos'][0], circle['pos'][1])
            radius = circle['pos'][2]
            R = circle['color'][0]
            G = circle['color'][1]
            B = circle['color'][2]
            print((R, G, B))
            cv2.circle(frame, center, 1, (R, G, B), 3)
            cv2.putText(frame, str(circle['pos'][2]), (circle['pos'][0] + 5, circle['pos'][1] + 5), cv2.FONT_HERSHEY_SIMPLEX,  0.5, (R, G, B), 1, cv2.LINE_AA)
    cv2.imshow('frame', frame)
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

cap.release()
cv2.destroyAllWindows()