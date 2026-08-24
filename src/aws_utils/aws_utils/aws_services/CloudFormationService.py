# aws_utils/aws_services/CloudFormationService.py
# CloudFormation - Infraestrutura como código.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class CloudFormationService:
    def __init__(self, client: AwsClient):
        self.cf = client.client("cloudformation")

    def list_stacks(self):
        """Lista stacks CloudFormation"""
        start = time.time()
        logger.info("Iniciando listagem de stacks CloudFormation")
        response = self.cf.list_stacks()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de stacks em {duration:.2f}s")
        return response.get("StackSummaries", [])

    def create_stack(self, stack_name: str, template_body: str, parameters: list = None):
        """Cria uma stack CloudFormation"""
        start = time.time()
        logger.info(f"Iniciando criação da stack '{stack_name}'")
        response = self.cf.create_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Parameters=parameters or []
        )
        duration = time.time() - start
        logger.info(f"Stack '{stack_name}' criada em {duration:.2f}s")
        return response

    def update_stack(self, stack_name: str, template_body: str, parameters: list = None):
        """Atualiza uma stack CloudFormation"""
        start = time.time()
        logger.info(f"Iniciando atualização da stack '{stack_name}'")
        response = self.cf.update_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Parameters=parameters or []
        )
        duration = time.time() - start
        logger.info(f"Stack '{stack_name}' atualizada em {duration:.2f}s")
        return response

    def delete_stack(self, stack_name: str):
        """Exclui uma stack CloudFormation"""
        start = time.time()
        logger.info(f"Iniciando exclusão da stack '{stack_name}'")
        response = self.cf.delete_stack(StackName=stack_name)
        duration = time.time() - start
        logger.info(f"Stack '{stack_name}' excluída em {duration:.2f}s")
        return response

    def describe_stack(self, stack_name: str):
        """Descreve detalhes de uma stack CloudFormation"""
        start = time.time()
        logger.info(f"Iniciando descrição da stack '{stack_name}'")
        response = self.cf.describe_stacks(StackName=stack_name)
        duration = time.time() - start
        logger.info(f"Descrição da stack '{stack_name}' concluída em {duration:.2f}s")
        return response.get("Stacks", [])
