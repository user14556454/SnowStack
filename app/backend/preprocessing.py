import cv2

# Used to show the image


image_file = "dummy.jpg"
img = cv2.imread(image_file)


# cv2.imshow("original image", img)
# cv2.waitKey(0)

# to invert the image 
# inv_img = cv2.bitwise_not(img)
# cv2.imwrite("Inverted.jpg", inv_img)
# cv2.imshow("Inverted.jpg", inv_img)
# cv2.waitKey(0)

# binarization of image then also to reduce noise and stuff


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey_image = grayscale(img)
cv2.imwrite("Greyscale.jpg",grey_image)
thresh, im_bw = cv2.threshold(grey_image, 150, 200, cv2.THRESH_BINARY)
cv2.imwrite("bw.jpg",im_bw)


def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

no_noice = noise_removal(im_bw)
cv2.imwrite("no_noice.jpg", no_noice)
cv2.imshow("bw.jpg",im_bw)
cv2.waitKey(0)
