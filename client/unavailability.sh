#!/bin/bash

# Configurações
SERVICE_URL="http://10.43.47.211:52021/api/recommend"  # Substitua pelo IP externo do seu serviço
REQUEST_PAYLOAD='{"songs": ["Yesterday", "Bohemian Rhapsody"]}'
MAX_ATTEMPTS=500  # Número máximo de tentativas
INTERVAL=1        # Intervalo entre requisições (em segundos)
OUTPUT_FILE="availability_results.csv"

# Cabeçalho do arquivo de resultados
echo "timestamp,response_time,status_code" > "$OUTPUT_FILE"

# Função para enviar requisições e registrar respostas
check_service() {
    while true; do
        local start_time=$(date +%s%3N)  # Tempo inicial em milissegundos
        local timestamp=$(date +"%Y-%m-%d %H:%M:%S")

        # Enviar requisição ao serviço
        response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$SERVICE_URL" \
                   -H "Content-Type: application/json" -d "$REQUEST_PAYLOAD")
        local end_time=$(date +%s%3N)  # Tempo final em milissegundos

        # Calcular o tempo de resposta
        local response_time=$((end_time - start_time))

        # Registrar o resultado no arquivo
        echo "$timestamp,$response_time,$response" >> "$OUTPUT_FILE"

        # Exibir log no terminal
        if [ "$response" -eq 200 ]; then
            echo "$timestamp - Service available. Response time: ${response_time}ms"
        else
            echo "$timestamp - Service unavailable. HTTP status: $response"
        fi

        # Esperar antes da próxima requisição
        sleep $INTERVAL
    done
}

# Início do monitoramento
echo "=== Starting service availability check ==="
check_service
