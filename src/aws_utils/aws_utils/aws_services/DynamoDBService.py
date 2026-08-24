# aws_utils/aws_services/DynamoDBService.py
# DynamoDB - Banco NoSQL totalmente gerenciado.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class DynamoDBService:
    def __init__(self, client: AwsClient):
        self.dynamodb = client.client("dynamodb")

    def list_tables(self):
        """Lista todas as tabelas DynamoDB"""
        start = time.time()
        logger.info("Iniciando listagem de tabelas DynamoDB")
        response = self.dynamodb.list_tables()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de tabelas DynamoDB em {duration:.2f}s")
        return response.get("TableNames", [])

    def create_table(self, table_name: str, key_schema: list, attr_definitions: list, throughput: dict):
        """Cria uma tabela DynamoDB"""
        start = time.time()
        logger.info(f"Iniciando criação da tabela '{table_name}'")
        response = self.dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attr_definitions,
            ProvisionedThroughput=throughput
        )
        duration = time.time() - start
        logger.info(f"Tabela '{table_name}' criada em {duration:.2f}s")
        return response

    def delete_table(self, table_name: str):
        """Exclui uma tabela DynamoDB"""
        start = time.time()
        logger.info(f"Iniciando exclusão da tabela '{table_name}'")
        response = self.dynamodb.delete_table(TableName=table_name)
        duration = time.time() - start
        logger.info(f"Tabela '{table_name}' excluída em {duration:.2f}s")
        return response
