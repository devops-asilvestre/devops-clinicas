import unittest
from unittest.mock import patch
from aws_utils.aws_services.SNSService import SNSService

class TestSNSPublish(unittest.TestCase):

    @patch("aws_utils.aws_services.SNSService.boto3.client")
    def test_publish_message(self, mock_boto_client):
        """
        Testa se a função publish_message do SNSService chama boto3 corretamente.
        """
        # Mock do cliente SNS
        mock_sns = mock_boto_client.return_value
        mock_sns.publish.return_value = {"MessageId": "12345"}

        sns_service = SNSService()
        response = sns_service.publish_message(
            topic_arn="arn:aws:sns:us-east-1:123456789012:ClinicasAtendimentosTopic",
            subject="Teste",
            message="Mensagem de teste"
        )

        # Verifica se boto3.publish foi chamado
        mock_sns.publish.assert_called_once_with(
            TopicArn="arn:aws:sns:us-east-1:123456789012:ClinicasAtendimentosTopic",
            Subject="Teste",
            Message="Mensagem de teste"
        )

        # Verifica se o retorno contém MessageId
        self.assertEqual(response["MessageId"], "12345")

if __name__ == "__main__":
    unittest.main()
