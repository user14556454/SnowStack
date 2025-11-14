import cv2
import numpy as np
from PIL import Image
import io

def read_image_from_bytes(file_bytes):
    pil = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    arr = np.array(pil)                      
    bgr = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    return bgr

def to_grayscale(bgr_img):
    return cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

def binarize(gray_img, thresh_val=150):
    _, bw = cv2.threshold(gray_img, thresh_val, 255, cv2.THRESH_BINARY)
    return bw

def remove_noise(img):
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.medianBlur(img, 3)
    return img

def cv2_to_bytes(img, fmt=".jpg"):
    is_success, buffer = cv2.imencode(fmt, img)
    if not is_success:
        raise RuntimeError("Could not encode image to bytes")
    return buffer.tobytes()

def run_preprocessing(file_bytes):
    bgr = read_image_from_bytes(file_bytes)
    gray = to_grayscale(bgr)
    bw = binarize(gray)
    denoised = remove_noise(bw)

    return {
        "original": cv2_to_bytes(bgr),
        "gray": cv2_to_bytes(gray),
        "binary": cv2_to_bytes(bw),
        "denoised": cv2_to_bytes(denoised)
    }
