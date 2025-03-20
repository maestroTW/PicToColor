import PIL
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import numpy as np
import cv2


def make_coloring_page(image_path):
    # open
    img = Image.open(image_path)

    # Canny Edge Detection
    array = np.array(img)
    canny_edges = cv2.Canny(array, 100, 200)
    canny_edges = Image.fromarray(canny_edges)

    # inverted
    inverted_edges = PIL.ImageOps.invert(canny_edges)

    return inverted_edges


image_path = 'test.jpg'
coloring_page = make_coloring_page(image_path)
coloring_page.show()