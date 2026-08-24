# aws_utils/aws_services/EC2Service.py
# EC2 - Máquinas virtuais na nuvem.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class EC2Service:
    def __init__(self, client: AwsClient):
        self.ec2 = client.client("ec2")

    def list_instances(self):
        """Lista todas as instâncias EC2"""
        start = time.time()
        logger.info("Iniciando listagem de instâncias EC2")
        response = self.ec2.describe_instances()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de instâncias EC2 em {duration:.2f}s")
        return response.get("Reservations", [])

    def create_instance(self, image_id: str, instance_type: str):
        """Cria uma instância EC2"""
        start = time.time()
        logger.info(f"Iniciando criação de instância EC2 tipo {instance_type}")
        response = self.ec2.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1
        )
        duration = time.time() - start
        logger.info(f"Instância EC2 criada em {duration:.2f}s")
        return response

    def start_instance(self, instance_id: str):
        """Inicia uma instância EC2"""
        start = time.time()
        logger.info(f"Iniciando instância '{instance_id}'")
        response = self.ec2.start_instances(InstanceIds=[instance_id])
        duration = time.time() - start
        logger.info(f"Instância '{instance_id}' iniciada em {duration:.2f}s")
        return response

    def stop_instance(self, instance_id: str):
        """Para uma instância EC2"""
        start = time.time()
        logger.info(f"Parando instância '{instance_id}'")
        response = self.ec2.stop_instances(InstanceIds=[instance_id])
        duration = time.time() - start
        logger.info(f"Instância '{instance_id}' parada em {duration:.2f}s")
        return response

    def terminate_instance(self, instance_id: str):
        """Termina uma instância EC2"""
        start = time.time()
        logger.info(f"Terminando instância '{instance_id}'")
        response = self.ec2.terminate_instances(InstanceIds=[instance_id])
        duration = time.time() - start
        logger.info(f"Instância '{instance_id}' terminada em {duration:.2f}s")
        return response
