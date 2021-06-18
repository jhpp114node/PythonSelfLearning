import cv2
import matplotlib.pyplot as plt
# blending images is nothing more than just adding the images together.
# addWeighted function is being used for blending image
# new_pixel = Alpha * pixel_2 + Beta x Pixel_2 + Y (optional gamma)

img1 = cv2.imread("/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/dog_backpack.png")
# convert into RGB from BGR
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("/Users/junpark/Downloads/Computer-Vision-with-Python/DATA/watermark_no_copy.png")
# convert into RGB from BGR
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# check the shape (size)
print(img1.shape)
print(img2.shape)

# the size are different need to re-format the size of the image
# BLENDING IMAGES OF THE SAME SIZE
img1 = cv2.resize(img1, (1200,1200))
img2 = cv2.resize(img2, (1200, 1200))

# addWeighted function (formula: Alpha * pixel_2 + Beta x Pixel_2 + Y (optional gamma))
# @https://docs.opencv.org/3.4/d5/dc4/tutorial_adding_images.html
blended_image = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)

while True:
    # simply change the src image
    # cv2.imshow("dog_backpage", img1)
    # cv2.imshow("water-mark", img2)
    cv2.imshow('blended-image', blended_image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()