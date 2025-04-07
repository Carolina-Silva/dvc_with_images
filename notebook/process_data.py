import tifffile
import matplotlib.pyplot as plt
import os
import numpy as np

from skimage.io import imread, imsave


image_path ='/home/carolina/lgcm/dev/dvc-in-action/images/data/raw/volume_lines.tif'

save_dir='/home/carolina/lgcm/dev/dvc-in-action/images/data/input'



def load_tifffile(path):
    try:
        imagem = tifffile.imread(path)
        return imagem
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None



image = load_tifffile(image_path)

image.shape[0]


# Fatia 50
plt.figure(figsize=(5, 5))
plt.imshow(image[50], cmap='gray')
plt.axis('off')
plt.show()


def save_slice(basename, z_num, slice_data):
    """Salva uma fatia como TIFF contendo todos os canais."""
    new_filename = os.path.join(save_dir, f"{basename}_z{z_num}.tif")

    imsave(new_filename, slice_data, photometric='minisblack')


def cut_slice(fname, img):
    """Salva todas as fatias Z contendo os três canais juntos."""
    basename = fname.replace(".tif", "")
    num_slices = img.shape[0]

    for z_num in range(num_slices):
        slice_data = img[:, z_num] 
        save_slice(basename, z_num, slice_data)


cut_slice(image_path, image)


def process_image(image):
    """Aplica remoção da adventícia na imagem."""
    image = np.logical_not(image).astype(int)

    return image


def save_slice2(basename, z_num, slice_data):
    """Salva uma fatia como TIFF contendo todos os canais."""
    new_filename = os.path.join(save_dir, f"{basename}_z{z_num}.tif")

    imsave(new_filename, slice_data, photometric='minisblack')
