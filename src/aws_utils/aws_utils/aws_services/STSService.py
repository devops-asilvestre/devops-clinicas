# aws_utils/aws_services/STSService.py
# STS - Segurança e credenciais temporárias.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class STSService:
    def __init__(self, client: AwsClient):
        self.sts = client.client("sts")

    def assume_role(self, role_arn: str, session_name: str):
        """Assume uma role temporária"""
        start = time.time()
        logger.info(f"Iniciando assume_role para '{role_arn}'")
        response = self.sts.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name
        )
        duration = time.time() - start
        logger.info(f"Assume_role concluído em {duration:.2f}s")
        return response

    def get_caller_identity(self):
        """Obtém identidade do chamador"""
        start = time.time()
        logger.info("Iniciando get_caller_identity")
        response = self.sts.get_caller_identity()
        duration = time.time() - start
        logger.info(f"get_caller_identity concluído em {duration:.2f}s")
        return response

    def get_session_token(self, duration_seconds: int = 3600):
        """Obtém token de sessão temporário"""
        start = time.time()
        logger.info("Iniciando get_session_token")
        response = self.sts.get_session_token(DurationSeconds=duration_seconds)
        duration = time.time() - start
        logger.info(f"get_session_token concluído em {duration:.2f}s")
        return response
