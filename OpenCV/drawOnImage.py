#!/usr/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt


def write_text(target_image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(target_image, text="hello world", org=(0,100), fontFace=font, fontScale= 2,
                color=(255,255,255), thickness=3, lineType=cv2.LINE_AA)


def draw_circle(target_image):
    # first circle top-left, bottom-right
    cv2.circle(target_image, center=(250,250), radius=50, color=(0,0,255), thickness=5)
    # second circle
    cv2.circle(target_image, center=(250,250), radius=10, color=(255,0,0), thickness=-1)


def draw_rectangle(target_image):
    # first rectangle
    cv2.rectangle(black_img, pt1=(384,10), pt2=(500, 100), color=(0,255,0), thickness=10)
    # second rectangle
    cv2.rectangle(target_image, pt1=(10,400), pt2=(100,500), color=(255,0,0), thickness=10)
    draw_circle(target_image)
    write_text(target_image)
    plt.imshow(target_image)
    plt.show()


# create a blank image with 512x512 with 3 rgb channel
black_img = np.zeros(shape=(512,512,3), dtype=np.int16)
# print(black_img)
# plt.imshow(black_img)
# plt.show()
draw_rectangle(black_img)


