# aws_utils/aws_services/StepFunctionsService.py
# Step Functions - Orquestração de workflows.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class StepFunctionsService:
    def __init__(self, client: AwsClient):
        self.sfn = client.client("stepfunctions")

    def list_state_machines(self):
        """Lista todas as state machines"""
        start = time.time()
        logger.info("Iniciando listagem de state machines")
        response = self.sfn.list_state_machines()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de state machines em {duration:.2f}s")
        return response.get("stateMachines", [])

    def create_state_machine(self, name: str, definition: str, role_arn: str):
        """Cria uma state machine"""
        start = time.time()
        logger.info(f"Iniciando criação da state machine '{name}'")
        response = self.sfn.create_state_machine(
            name=name,
            definition=definition,
            roleArn=role_arn
        )
        duration = time.time() - start
        logger.info(f"State machine '{name}' criada em {duration:.2f}s")
        return response

    def start_execution(self, state_machine_arn: str, input_data: str):
        """Inicia execução de uma state machine"""
        start = time.time()
        logger.info(f"Iniciando execução da state machine '{state_machine_arn}'")
        response = self.sfn.start_execution(
            stateMachineArn=state_machine_arn,
            input=input_data
        )
        duration = time.time() - start
        logger.info(f"Execução iniciada em {duration:.2f}s")
        return response
