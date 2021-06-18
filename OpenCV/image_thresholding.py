import cv2

def regular_gray_scale():
    img = cv2.imread('/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/rainbow.jpg', 0)
    return img


def threshold_img():
    # any value that is less than threshold becomes 0
    # any value that is bigger than threshold becomes max
    pass


def main():
    img = regular_gray_scale()
    while True:
        cv2.imshow('gray-scale', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()