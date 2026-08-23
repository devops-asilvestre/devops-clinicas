import boto3
import time
import concurrent.futures

# Configurações
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:ClinicasAtendimentosTopic"
TOTAL_EVENTOS = 1000   # número de eventos simulados
CONCURRENCY = 50       # número de threads simultâneas

sns_client = boto3.client("sns")

# Função para publicar evento no SNS
def publicar_evento(evento_id):
    mensagem = {
        "ClinicaId": f"SP001",
        "AtendimentoId": f"A{evento_id:04d}",
        "Paciente": f"Paciente{evento_id}",
        "Tipo": "Convênio" if evento_id % 2 == 0 else "ProBono",
        "Valor": 200 if evento_id % 2 == 0 else 0
    }
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=str(mensagem)
    )
    return evento_id

def executar_teste():
    inicio = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        resultados = list(executor.map(publicar_evento, range(1, TOTAL_EVENTOS + 1)))
    fim = time.time()
    print(f"✅ Teste concluído: {len(resultados)} eventos publicados.")
    print(f"⏱️ Tempo total: {fim - inicio:.2f} segundos")
    print(f"⚡ Throughput médio: {TOTAL_EVENTOS / (fim - inicio):.2f} eventos/segundo")

if __name__ == "__main__":
    executar_teste()
