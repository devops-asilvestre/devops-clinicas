# aws_utils/aws_services/SQSService.py
# SQS - Fila de mensagens.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class SQSService:
    def __init__(self, client: AwsClient):
        self.sqs = client.client("sqs")

    def list_queues(self):
        """Lista filas SQS"""
        start = time.time()
        logger.info("Iniciando listagem de filas SQS")
        response = self.sqs.list_queues()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de filas em {duration:.2f}s")
        return response.get("QueueUrls", [])

    def create_queue(self, queue_name: str):
        """Cria uma fila SQS"""
        start = time.time()
        logger.info(f"Iniciando criação da fila '{queue_name}'")
        response = self.sqs.create_queue(QueueName=queue_name)
        duration = time.time() - start
        logger.info(f"Fila '{queue_name}' criada em {duration:.2f}s")
        return response

    def delete_queue(self, queue_url: str):
        """Exclui uma fila SQS"""
        start = time.time()
        logger.info(f"Iniciando exclusão da fila '{queue_url}'")
        response = self.sqs.delete_queue(QueueUrl=queue_url)
        duration = time.time() - start
        logger.info(f"Fila '{queue_url}' excluída em {duration:.2f}s")
        return response

    def send_message(self, queue_url: str, message_body: str):
        """Envia uma mensagem para a fila SQS"""
        start = time.time()
        logger.info(f"Enviando mensagem para fila '{queue_url}'")
        response = self.sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
        duration = time.time() - start
        logger.info(f"Mensagem enviada em {duration:.2f}s")
        return response

    def receive_message(self, queue_url: str, max_messages: int = 1, wait_time: int = 0):
        """Recebe mensagens da fila SQS"""
        start = time.time()
        logger.info(f"Recebendo até {max_messages} mensagens da fila '{queue_url}'")
        response = self.sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=max_messages,
            WaitTimeSeconds=wait_time
        )
        duration = time.time() - start
        logger.info(f"Mensagens recebidas em {duration:.2f}s")
        return response.get("Messages", [])

    def delete_message(self, queue_url: str, receipt_handle: str):
        """Exclui uma mensagem da fila SQS"""
        start = time.time()
        logger.info(f"Excluindo mensagem da fila '{queue_url}'")
        response = self.sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        duration = time.time() - start
        logger.info(f"Mensagem excluída em {duration:.2f}s")
        return response
