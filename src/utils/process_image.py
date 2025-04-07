import os
import numpy as np
import tifffile
import matplotlib.pyplot as plt
import cv2
from skimage.io import imread, imsave

class ImageProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def invert_image(self, image):
        # Certifica que a imagem está no formato correto (uint8)
        if image.dtype != np.uint8:
            image = (image * 255).astype(np.uint8)

        kernel = np.ones((5, 5), dtype="uint8")
        new_image = cv2.dilate(image, kernel, iterations=1)
        return new_image

    def process_all_slices(self):
        for fname in os.listdir(self.input_dir):
            if fname.endswith(".tif"):
                full_input_path = os.path.join(self.input_dir, fname)
                img = imread(full_input_path)

                processed = self.invert_image(img)

                full_output_path = os.path.join(self.output_dir, fname)
                imsave(full_output_path, processed, photometric='minisblack')
