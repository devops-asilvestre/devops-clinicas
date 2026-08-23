# Essa Lambda será responsável por consolidar os dados do DynamoDB e gravar no RDS (MySQL/PostgreSQL), gerando relatórios mensais de cada clínica.
# garantimos que os dados em tempo real do DynamoDB sejam consolidados em relatórios mensais no RDS, permitindo que o Sr. Roberto acompanhe a performance financeira e o cumprimento da regra pro-bono em cada clínica.

import os
from datetime import datetime
from aws_utils.aws_services.DynamoDBService import DynamoDBService
from aws_utils.aws_services.RDSService import RDSService

# Inicializar serviços via AWS Utils
dynamodb_service = DynamoDBService(table_name="Atendimentos")
rds_service = RDSService(
    host=os.environ.get("RDS_HOST"),
    user=os.environ.get("RDS_USER"),
    password=os.environ.get("RDS_PASSWORD"),
    database=os.environ.get("RDS_DATABASE")
)

def lambda_handler(event, context):
    """
    Consolida dados do DynamoDB e grava relatório mensal no RDS.
    """
    try:
        mes_atual = datetime.utcnow().strftime("%Y-%m")

        # Lista de clínicas (poderia vir de outra tabela ou config)
        clinicas = ["CLINICA-001", "CLINICA-002", "CLINICA-003"]

        for clinica_id in clinicas:
            # Buscar atendimentos da clínica no mês atual
            items = dynamodb_service.query_items(
                filter_expression="clinicaId = :c AND begins_with(dataHora, :m)",
                expression_values={
                    ":c": clinica_id,
                    ":m": mes_atual
                }
            )

            total_atendimentos = len(items)
            total_probono = sum(1 for i in items if i.get("tipoAtendimento") == "pro-bono")
            total_pagos = total_atendimentos - total_probono
            receita_total = sum(float(i.get("valor", 0)) for i in items)

            # Inserir ou atualizar relatório no RDS
            query = """
                INSERT INTO RelatoriosMensais (clinicaId, mesReferencia, totalAtendimentos, totalProBono, totalPagos, receitaTotal)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    totalAtendimentos = VALUES(totalAtendimentos),
                    totalProBono = VALUES(totalProBono),
                    totalPagos = VALUES(totalPagos),
                    receitaTotal = VALUES(receitaTotal);
            """

            params = (clinica_id, mes_atual, total_atendimentos, total_probono, total_pagos, receita_total)
            rds_service.execute_query(query, params)

            print(f"📊 Relatório atualizado para clínica {clinica_id} ({mes_atual})")

        return {"statusCode": 200, "body": "Relatórios mensais atualizados com sucesso"}

    except Exception as e:
        print(f"Erro ao atualizar relatório: {str(e)}")
        return {"statusCode": 500, "body": "Erro interno"}
