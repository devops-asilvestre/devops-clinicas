# aws_utils/aws_services/SNSService.py
# SNS - Notificação e mensagens.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class SNSService:
    def __init__(self, client: AwsClient):
        self.sns = client.client("sns")

    def list_topics(self):
        """Lista tópicos SNS"""
        start = time.time()
        logger.info("Iniciando listagem de tópicos SNS")
        response = self.sns.list_topics()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de tópicos em {duration:.2f}s")
        return response.get("Topics", [])

    def create_topic(self, name: str):
        """Cria um tópico SNS"""
        start = time.time()
        logger.info(f"Iniciando criação do tópico '{name}'")
        response = self.sns.create_topic(Name=name)
        duration = time.time() - start
        logger.info(f"Tópico '{name}' criado em {duration:.2f}s")
        return response

    def delete_topic(self, topic_arn: str):
        """Exclui um tópico SNS"""
        start = time.time()
        logger.info(f"Iniciando exclusão do tópico '{topic_arn}'")
        response = self.sns.delete_topic(TopicArn=topic_arn)
        duration = time.time() - start
        logger.info(f"Tópico '{topic_arn}' excluído em {duration:.2f}s")
        return response

    def publish_message(self, topic_arn: str, message: str):
        """Publica uma mensagem em um tópico SNS"""
        start = time.time()
        logger.info(f"Publicando mensagem no tópico '{topic_arn}'")
        response = self.sns.publish(TopicArn=topic_arn, Message=message)
        duration = time.time() - start
        logger.info(f"Mensagem publicada em {duration:.2f}s")
        return response

    def subscribe(self, topic_arn: str, protocol: str, endpoint: str):
        """Cria uma assinatura em um tópico SNS"""
        start = time.time()
        logger.info(f"Assinando tópico '{topic_arn}' com protocolo '{protocol}'")
        response = self.sns.subscribe(
            TopicArn=topic_arn,
            Protocol=protocol,
            Endpoint=endpoint
        )
        duration = time.time() - start
        logger.info(f"Assinatura criada em {duration:.2f}s")
        return response

    def unsubscribe(self, subscription_arn: str):
        """Remove uma assinatura de um tópico SNS"""
        start = time.time()
        logger.info(f"Removendo assinatura '{subscription_arn}'")
        response = self.sns.unsubscribe(SubscriptionArn=subscription_arn)
        duration = time.time() - start
        logger.info(f"Assinatura removida em {duration:.2f}s")
        return response
