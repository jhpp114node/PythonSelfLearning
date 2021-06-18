#!/usr/bin/env python3

# Task: OPEN the dog_backpack.jpg image and display
import cv2
import numpy as np

def read_image():
    img = cv2.imread('/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/dog_backpack.jpg')
    print(type(img))
    return img


def flip_image():
    img = cv2.imread('/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/dog_backpack.jpg')
    flipped_img = cv2.flip(img, 0)
    return flipped_img


def draw_rectangle_dog_face():
    img = cv2.imread('/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/dog_backpack.jpg')
    return cv2.rectangle(img, pt1=(200, 350), pt2=(600, 750), color=(0,0,255), thickness=10)


# global for mouse event
img = cv2.imread('/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/dog_backpack.jpg')


def draw_circle_mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 25, (0,0,255), 2)


def main():
    # Mouse event
    cv2.namedWindow(winname="dog_backpage")
    cv2.setMouseCallback("dog_backpage", draw_circle_mouse_event)
    # checked pass
    read_img = read_image()
    # checked pass
    flipped_img = flip_image()
    # checked pass
    draw_rec = draw_rectangle_dog_face()
    while True:
        # simply change the src image
        cv2.imshow("dog_backpage", draw_rec)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()