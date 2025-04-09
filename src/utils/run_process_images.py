import yaml
from process_image import ImageProcessor

# Lê os parâmetros
with open("params.yaml") as f:
    params = yaml.safe_load(f)

input_dir = params["processor"]["input_dir"]
output_dir = params["processor"]["intermediate_dir"]

# Processa todas as fatias
processor = ImageProcessor(input_dir, output_dir)
processor.process_all_slices()
