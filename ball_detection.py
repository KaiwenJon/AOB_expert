import numpy as np
import cv2
import time
from Circle import Circle

def findCircles(src):
    height, width = src.shape[:2]
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=40,
                               minRadius=30, maxRadius=120)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        output_circles = []
        for position in circles[0, :]:
            if position[1] >= height or position[0] >= width:
                continue
            x = position[0]
            y = position[1]
            radius = position[2]
            B = int(src[position[1]][position[0]][0])
            G = int(src[position[1]][position[0]][1])
            R = int(src[position[1]][position[0]][2])

            new_circle = Circle(x, y, radius, B, G, R)
            output_circles.append(new_circle)
        return output_circles


if __name__ == '__main__':
    img = cv2.imread("test.jpg")
    findCircles(img, show=True)

    print("Press any key to continue.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()