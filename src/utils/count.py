import os
import csv
from skimage.io import imread
from skimage.measure import label


class ObjectCounter:
    def __init__(self, input_dir, csv_output_path):
        self.input_dir = input_dir
        self.csv_output_path = csv_output_path

    def count_objects_in_image(self, image):
        # Conta componentes conectados (0 é fundo)
        labeled = label(image)
        return labeled.max() + 1

    def process_all(self):
        resultados = []

        for fname in os.listdir(self.input_dir):
            if fname.endswith(".tif"):
                path = os.path.join(self.input_dir, fname)
                img = imread(path)

                count = self.count_objects_in_image(img)
                resultados.append((fname, count))

        self.save_csv(resultados)

    def save_csv(self, data):
        with open(self.csv_output_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["arquivo", "quantidade_objetos"])
            writer.writerows(data)
