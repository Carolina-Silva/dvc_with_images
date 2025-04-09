import yaml
from count import ObjectCounter

# Lê os parâmetros
with open("params.yaml") as f:
    params = yaml.safe_load(f)

input_dir = params["counter"]["intermediate_dir"]
csv_output = params["counter"]["output_csv"]

# Executa a contagem
counter = ObjectCounter(input_dir, csv_output)
counter.process_all()
