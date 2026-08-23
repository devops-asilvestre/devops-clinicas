# aws_utils/aws_services/LambdaService.py
# Lambda - Funções serverless.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class LambdaService:
    def __init__(self, client: AwsClient):
        self.lambda_client = client.client("lambda")

    def list_functions(self):
        """Lista todas as funções Lambda"""
        start = time.time()
        logger.info("Iniciando listagem de funções Lambda")
        response = self.lambda_client.list_functions()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de funções Lambda em {duration:.2f}s")
        return response.get("Functions", [])

    def invoke_function(self, function_name: str, payload: dict):
        """Invoca uma função Lambda"""
        start = time.time()
        logger.info(f"Invocando função Lambda '{function_name}'")
        response = self.lambda_client.invoke(
            FunctionName=function_name,
            Payload=str(payload)
        )
        duration = time.time() - start
        logger.info(f"Função '{function_name}' invocada em {duration:.2f}s")
        return response
