from cut_slices import ImageSlicer
from process_image import ImageProcessor
from count import ObjectCounter

# Etapa 1: Cortar fatias
image_path = '/home/carolina/lgcm/dev/dvc-in-action/images/data/raw/volume_lines.tif'
slices_dir = '/home/carolina/lgcm/dev/dvc-in-action/images/data/input'

slicer = ImageSlicer(image_path, slices_dir)
slicer.cut_all_slices()

# Etapa 2: Processar fatias já salvas
processed_dir = '/home/carolina/lgcm/dev/dvc-in-action/images/data/intermediate'

processor = ImageProcessor(slices_dir, processed_dir)
processor.process_all_slices()


input_dir = processed_dir
csv_output_path = '/home/carolina/lgcm/dev/dvc-in-action/images/data/output/objetos_contados.csv'

counter = ObjectCounter(input_dir, csv_output_path)
counter.process_all()