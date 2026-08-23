# 🔍 O que esse código faz
# Recebe evento SNS → a Lambda é acionada quando o tópico SNS recebe uma mensagem.
# Lê JSON → extrai dados como clinicaId, atendimentoId, pacienteId, tipoAtendimento.
# Grava no DynamoDB → insere o atendimento na tabela Atendimentos.
# Log → imprime no console para auditoria.

# 📌 Conclusão
# Com essa Lambda, garantimos que cada atendimento publicado no SNS seja persistido automaticamente no DynamoDB, criando a base para relatórios e monitoramento.

import json
import boto3
from datetime import datetime

# Cliente DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def lambda_handler(event, context):
    """
    Função Lambda que consome o evento SNS e grava no DynamoDB
    """
    try:    
        # O SNS entrega amensagem em Records
        for record in event['Records']:
            sns_message = record['Sns']['Message']
            data = json.loads(sns_message)
            
            # Extrai dados do evendo
            clinica_id = data.get("clinicaId")
            paciente_id = data.get("pacienteId")
            atendimento_id = data.get("atendimentoId")
            tipo_atendimento = data.get("tipoAtendimento")
            valor = data.get("valor", 0.0)
            status = data.get("status", "concluido")
            timestamp = data.get("timestamp", datetime.utcnow().isoformat()  )
            
            #Inserir no dynamodb
            table.put_item(
                Item={
                    "clinicaId": clinica_id,
                    "pacienteId": paciente_id,
                    "atendimentoId": atendimento_id,
                    "tipoAtendimento": tipo_atendimento,
                    "valor": valor,
                    "status": status,
                    "dataHora": timestamp
                }
            )
            print(f"Atendimento {atendimento_id} registrado para a clínica {clinica_id}.")
        return {"StatusCode": 200, "body": json.dumps("Evento processado com sucesso.") }
    
    except Exception as e:
            print(f"Erro ao processar o evento: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps('Erro ao processar o evento.')
            }