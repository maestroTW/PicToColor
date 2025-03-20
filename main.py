import PIL
from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import cv2

def make_coloring_page(image_path):
    # open
    img = Image.open(image_path)

    # improve quality
    contrast_enhancer = ImageEnhance.Contrast(img)
    high_contrast_img = contrast_enhancer.enhance(1.5)
    brightness_enhancer = ImageEnhance.Brightness(high_contrast_img)
    brighter_img = brightness_enhancer.enhance(1.2)

    # Canny Edge Detection
    array = np.array(brighter_img)
    canny_edges = cv2.Canny(array, 100, 200)
    canny_edges = Image.fromarray(canny_edges)

    # inverted
    inverted_edges = PIL.ImageOps.invert(canny_edges)

    return inverted_edges
