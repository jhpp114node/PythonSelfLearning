#!/usr/bin/env python3

import numpy as np
import cv2
import matplotlib.pyplot as plt

####################
###### Function ####
####################
def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255,0.0), -1)


cv2.namedWindow(winname='my_drawing')
# call back function
cv2.setMouseCallback('my_drawing', draw_circle)
#################################
###### Showing image with OPENCV#
#################################

# blank images
img = np.zeros((512,512,3), np.int8)

while True:
    cv2.imshow('my_drawing', img)
    # if to break out from the loop
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()