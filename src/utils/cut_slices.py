import os
import numpy as np
import tifffile
import matplotlib.pyplot as plt
from skimage.io import imread, imsave

class ImageSlicer:
    def __init__(self, image_path, save_dir):
        self.image_path = image_path
        self.save_dir = save_dir
        self.image = self.load_image()
        self.basename = os.path.splitext(os.path.basename(image_path))[0]

    def load_image(self):
        try:
            return tifffile.imread(self.image_path)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            return None

    def save_slice(self, z_num, slice_data):
        filename = os.path.join(self.save_dir, f"{self.basename}_z{z_num}.tif")
        imsave(filename, slice_data, photometric='minisblack')

    def cut_all_slices(self):
        if self.image is None:
            return

        os.makedirs(self.save_dir, exist_ok=True)
        for z_num in range(self.image.shape[0]):
            slice_data = self.image[z_num]
            self.save_slice(z_num, slice_data)

    def show_slice(self, z_index):
        if self.image is not None:
            plt.figure(figsize=(5, 5))
            plt.imshow(self.image[z_index], cmap='gray')
            plt.axis('off')
            plt.show()
