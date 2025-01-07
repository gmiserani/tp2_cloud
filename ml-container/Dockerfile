# Usar uma imagem base com Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências para o contêiner
COPY requirements.txt .
# COPY ~datasets/spotify .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o script e o dataset para o contêiner
COPY ./part1.py .

RUN mkdir -p /model

# Definir o comando padrão para rodar o script
CMD ["python", "./part1.py"]
