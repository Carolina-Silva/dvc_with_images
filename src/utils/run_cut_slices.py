import yaml
from cut_slices import ImageSlicer

# Lê os parâmetros do arquivo
with open("params.yaml") as f:
    params = yaml.safe_load(f)


# Pega os caminhos definidos para a etapa de corte
image_path = params["slicer"]["raw_data"]
save_dir = params["slicer"]["input_dir"]

# Executa o corte
slicer = ImageSlicer(image_path, save_dir)
slicer.cut_all_slices()
