import cv2


def generate_image():
    img = cv2.imread('test.png', 0)
    return img
