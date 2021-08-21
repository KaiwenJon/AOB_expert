import numpy as np
import cv2
import time


def findCircles(src, show=True):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=40,
                               minRadius=30, maxRadius=120)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(src, center, radius, (255, 0, 255), 3)
    if show == True:
        cv2.imshow("detected circles", src)
    if circles is not None:
        return circles[0, :]


if __name__ == '__main__':
    img = cv2.imread("test.jpg")
    findCircles(img, show=True)

    print("Press any key to continue.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()