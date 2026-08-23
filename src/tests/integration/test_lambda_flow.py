import unittest
from unittest.mock import patch
from devops-clinicas.lambdas import process_event

class TestLambdaFlow(unittest.TestCase):

    @patch("aws_utils.aws_services.DynamoDBService.DynamoDBService.put_item")
    def test_lambda_process_event(self, mock_put_item):
        """
        Testa se a Lambda process_event grava corretamente no DynamoDB
        quando recebe um evento SNS.
        """
        # Mock do retorno do DynamoDB
        mock_put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

        # Evento SNS simulado
        event = {
            "Records": [
                {
                    "Sns": {
                        "Message": """{
                            "clinicaId": "CLINICA-001",
                            "atendimentoId": "ATT-12345",
                            "pacienteId": "PAC-67890",
                            "tipoAtendimento": "pro-bono",
                            "valor": 0.0,
                            "status": "concluido",
                            "timestamp": "2026-08-22T22:00:00Z"
                        }"""
                    }
                }
            ]
        }

        # Executa a Lambda
        response = process_event.lambda_handler(event, None)

        # Verifica se DynamoDB foi chamado
        mock_put_item.assert_called_once()
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["body"], "Eventos processados com sucesso")

if __name__ == "__main__":
    unittest.main()
