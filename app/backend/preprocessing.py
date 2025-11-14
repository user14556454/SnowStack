import cv2
import numpy as np
from PIL import Image

def read_image(uploaded_file):
    image = Image.open(uploaded_file)
    image = image.convert("RGB")       
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def binarize(gray_img):
    _, bw = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)
    return bw

def remove_noise(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return cv2.medianBlur(image, 3)

def run_preprocessing(uploaded_file):
    original = read_image(uploaded_file)
    gray = to_grayscale(original)
    bw = binarize(gray)
    noise = remove_noise(bw)

    return {
        "original": original,
        "gray": gray,
        "binary": bw,
        "denoised": noise
    }
