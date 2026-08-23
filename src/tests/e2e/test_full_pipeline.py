import unittest
from unittest.mock import patch
from devops-clinicas.lambdas import process_event, validar_probono, atualizar_relatorio

class TestFullPipeline(unittest.TestCase):

    @patch("aws_utils.aws_services.DynamoDBService.DynamoDBService.put_item")
    @patch("aws_utils.aws_services.DynamoDBService.DynamoDBService.query_items")
    @patch("aws_utils.aws_services.RDSService.RDSService.execute_query")
    @patch("aws_utils.aws_services.SNSService.SNSService.publish_message")
    def test_full_pipeline(
        self,
        mock_publish_message,
        mock_execute_query,
        mock_query_items,
        mock_put_item
    ):
        """
        Testa o fluxo completo: SNS → Lambdas → DynamoDB → RDS → SNS Alerts.
        """

        # Mock DynamoDB inserção
        mock_put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

        # Mock DynamoDB consulta
        mock_query_items.return_value = [
            {"tipoAtendimento": "pro-bono", "valor": 0.0},
            {"tipoAtendimento": "pago", "valor": 500.0}
        ]

        # Mock RDS execução
        mock_execute_query.return_value = {"status": "success"}

        # Mock SNS alerta
        mock_publish_message.return_value = {"MessageId": "ALERT-001"}

        # Evento SNS simulado
        event = {
            "Records": [
                {
                    "Sns": {
                        "Message": """{
                            "clinicaId": "CLINICA-001",
                            "atendimentoId": "ATT-99999",
                            "pacienteId": "PAC-11111",
                            "tipoAtendimento": "pro-bono",
                            "valor": 0.0,
                            "status": "concluido",
                            "timestamp": "2026-08-22T22:00:00Z"
                        }"""
                    }
                }
            ]
        }

        # 1. Processar evento → DynamoDB
        response_process = process_event.lambda_handler(event, None)
        self.assertEqual(response_process["statusCode"], 200)

        # 2. Validar pro-bono → SNS alerta
        response_validar = validar_probono.lambda_handler({}, None)
        self.assertEqual(response_validar["statusCode"], 200)
        mock_publish_message.assert_called()

        # 3. Atualizar relatório → RDS
        response_relatorio = atualizar_relatorio.lambda_handler({}, None)
        self.assertEqual(response_relatorio["statusCode"], 200)
        mock_execute_query.assert_called()

if __name__ == "__main__":
    unittest.main()
