import os
import csv
import json
from skimage.io import imread
from skimage.measure import label


class ObjectCounter:
    def __init__(self, input_dir, csv_output_path):
        self.input_dir = input_dir
        self.csv_output_path = csv_output_path

    def count_objects_in_image(self, image):
        # Conta componentes conectados (0 é fundo)
        labeled = label(image)
        return labeled.max()

    def process_all(self):
        resultados = []

        for fname in os.listdir(self.input_dir):
            if fname.endswith(".tif"):
                path = os.path.join(self.input_dir, fname)
                img = imread(path)

                count = self.count_objects_in_image(img)
                resultados.append((fname, count))

        self.save_csv(resultados)
        self.save_metrics_json(resultados)
        print(f"Resultados salvos em {self.csv_output_path}")
        print(f"Contagem de objetos concluída para {len(resultados)} imagens.")

    def save_csv(self, data):
        save_url = os.path.join(self.csv_output_path, "results.csv")
        with open(save_url, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["arquivo", "quantidade_objetos"])
            writer.writerows(data)
    
    def save_metrics_json(self, data):
        total = sum(int(row[1]) for row in data)
        metrics = {
            "quantidade_total_objetos": total,
            "arquivos_processados": len(data)
        }
        with open(os.path.join(self.csv_output_path, "metrics.json"), "w") as f:
            json.dump(metrics, f, indent=4)        
