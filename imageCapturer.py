
import numpy as np
import cv2
import time
from ball_detection import findCircles

cap = cv2.VideoCapture('AOB.mp4')
play = 1
cnt = 0
while(cap.isOpened()):
    if (play):
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
    if(play):
        findCircles(frame, show=False)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(10)
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