import cv2
import numpy as np
import matplotlib.pyplot as plt

# variable
# True while mouse button down, False while mouse button up
drawing = False
ix = -1
iy = -1


def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # set the ix and iy to x and y position
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x,y), (0,255,0) -1)


img = np.zeros((525,525, 3))
cv2.namedWindow(winname="Blank_img")
cv2.setMouseCallback("Black_img", draw_rectangle)
while True:
    cv2.imshow("Blank_img", img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()