# Essa função será responsável por validar se cada clínica atingiu os 10 atendimentos pro-bono no mês. 
# Caso não tenha atingido, ela dispara um alerta via SNS para notificar o Sr. Roberto ou a equipe de gestão.

import os
from datetime import datetime
from aws_utils.aws_services.DynamoDBService import DynamoDBService
from aws_utils.aws_services.SNSService import SNSService    

# Inicializar serviçp via AWS Utils
dynamodb_service = DynamoDBService(table_name=os.environ['DYNAMODB_TABLE_NAME'])
sns_service = SNSService()

SNS_TOPIC_ARN = os.environ['SNS_ALERT_TOPIC_ARN']

def lambda_handler(event, context):
    """
    Valida se cada clínica atingiu os 10 atendimentos pro-bono no mês. Caso não tenha atingido, dispara um alerta via SNS.
    Caso contrário, dispara alerta via SNS.
    """
    try:
        # Lógica de validação dos atendimentos pro-bono
        mes_atual = datetime.utcnow().strftime("%Y-%m")
        
        # Lista de clínicas (pode vir de outra tabela ou config)
        clinicas = ["CLINICA-001", "CLINICA-002", "CLINICA-003", "CLINICA-004"]  # Exemplo de IDs de clínicas
        for clinica_id in clinicas:
            # Usando DynamoDBService para buscar atendimentos
            items = dynamodb_service.query_items(
                filter_expression="clinicaId = :c AND tipoAtendimento = :t AND begins_with(dataHora, :m)",
                expression_values={
                    ":c": clinica_id,
                    ":t": "pro-bono",
                    ":m": mes_atual
                }
            )
            total_probono = len(items)
            
            if total_probono < 10:
                mensagem = {
                    "clinicaId": clinica_id,
                    "mesReferencia": mes_atual,
                    "totalProBono": total_probono,
                    "alerta": f"A clínica {clinica_id} não atingiu os 10 atendimentos pro-bono no mês {mes_atual}. Total realizado: {total_probono}."
                }
                # Usando SNSServices para publicar alerta
                sns_service.publish_message(
                    topic_arn=SNS_TOPIC_ARN,
                    message=str(mensagem),
                    subject=f"Alerta Pro-Bono: Clínica {clinica_id} não atingiu 10 atendimentos pro-bono"
                )
                
                print(f"⚠️ Alerta enviado para clínica {clinica_id}: apenas {total_probono} atendimentos pro-bono.")
                 
        return {"statusCode": 200, "body": "Validação concluída"}
   
    except Exception as e:
        print(f"Erro ao validar atendimentos pro-bono: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Erro ao validar atendimentos pro-bono: {str(e)}"
        }
    
