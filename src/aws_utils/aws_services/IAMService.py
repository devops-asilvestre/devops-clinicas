# aws_utils/aws_services/IAMService.py
# IAM - Gerenciamento de identidades e permissões.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class IAMService:
    def __init__(self, client: AwsClient):
        self.iam = client.client("iam")

    def list_roles(self):
        """Lista todas as roles IAM"""
        start = time.time()
        logger.info("Iniciando listagem de roles IAM")
        response = self.iam.list_roles()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de roles IAM em {duration:.2f}s")
        return response.get("Roles", [])

    def create_role(self, role_name: str, assume_policy: str):
        """Cria uma role IAM"""
        start = time.time()
        logger.info(f"Iniciando criação da role '{role_name}'")
        response = self.iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=assume_policy
        )
        duration = time.time() - start
        logger.info(f"Role '{role_name}' criada em {duration:.2f}s")
        return response

    def delete_role(self, role_name: str):
        """Exclui uma role IAM"""
        start = time.time()
        logger.info(f"Iniciando exclusão da role '{role_name}'")
        response = self.iam.delete_role(RoleName=role_name)
        duration = time.time() - start
        logger.info(f"Role '{role_name}' excluída em {duration:.2f}s")
        return response
