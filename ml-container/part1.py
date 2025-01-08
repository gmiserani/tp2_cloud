import os
import pandas as pd
from fpgrowth_py import fpgrowth
import pickle
from pathlib import Path


# Carregar o dataset com o header especificado
# df = pd.read_csv("/app/datasets/spotify/2023_spotify_ds1.csv", header=0)

dataset_name = os.getenv("DATASET_NAME", "ds1.csv")  # Valor padrão caso a variável não esteja definida
dataset_base_path = os.getenv("DATASET_BASE_PATH", "/app/datasets/spotify/")

dataset_path = Path(dataset_base_path) / dataset_name

df = pd.read_csv(dataset_path, header=0)

# Selecionar as colunas relevantes: agruparemos por 'pid' e coletaremos os nomes das músicas
transactions = df.groupby("pid")["track_name"].apply(list).tolist()
# Gerar regras de associação usando FP-Growth
min_support = 0.1  # Suporte mínimo ajustável
min_confidence = 0.5  # Confiança mínima ajustável
freq_itemsets, rules = fpgrowth(transactions, minSupRatio=min_support, minConf=min_confidence)

# Exibir algumas regras geradas para verificação
print("Exemplos de Regras:")
for rule in rules[:5]:  # Mostrar as primeiras 5 regras
    antecedent, consequent, confidence = rule
    print(f"Se {antecedent}, então {consequent} (confiança: {confidence:.2f})")

# Salvar as regras em um arquivo pickle
output_path = Path('/model/recommendation_rules.pkl')
with open(output_path, "wb") as f:
    pickle.dump(rules, f)

print(f"Regras salvas em {output_path}")
