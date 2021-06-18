#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import cv2

# this will automatically convert the image into arrays
# Image.open is no longer required
def get_image():
    try:
        image_file = cv2.imread("/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg")
        if type(image_file) == 'NoneType':
            raise TypeError
        return image_file
    except TypeError as image_type_error:
        print("Fail to open the image")
        print(image_type_error)


def display_image(image_arr):
    """
        Matplotlib -> RGB
        OpenCV -> BGR
    :param image_arr:
    :return: display image
    """
    # transform to adjust it into matplot
    # Blue Green Red => Red Green Blue
    fixed_image = cv2.cvtColor(image_arr, cv2.COLOR_BGR2RGB)
    plt.imshow(fixed_image)
    plt.show()


def image_gray_scale():
    img_gray = cv2.imread("/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg", cv2.IMREAD_GRAYSCALE)
    # if it is gray no need to have 3 channels
    # plt.imshow(img_gray, cmap='gray')
    # plt.show()
    return img_gray


# resizing image
# takes a param: image_array
def resize_image(width, height):
    gray_scale_img = image_gray_scale()
    resized_image = cv2.resize(gray_scale_img, (width, height))

    # flip image
    # up and down -1
    # left and right 1
    flipped_image = cv2.flip(resized_image, 1)
    # save the image file
    cv2.imwrite("flipped_image.jpg", flipped_image)
    # display image
    plt.imshow(resized_image, cmap='gray')
    plt.show()
    plt.imshow(flipped_image, cmap="gray")
    plt.show()



def main():
    image_array = get_image()
    # display_image(image_array)
    # display gray scale image
    # image_gray_scale()
    # resize image
    resize_image(1000, 500)


if __name__ == "__main__":
    main()