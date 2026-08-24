# aws_utils/aws_services/RDSService.py
# RDS - Banco de dados relacional gerenciado.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class RDSService:
    def __init__(self, client: AwsClient):
        self.rds = client.client("rds")

    def list_instances(self):
        """Lista instâncias RDS"""
        start = time.time()
        logger.info("Iniciando listagem de instâncias RDS")
        response = self.rds.describe_db_instances()
        duration = time.time() - start
        logger.info(f"Finalizada listagem de instâncias RDS em {duration:.2f}s")
        return response.get("DBInstances", [])

    def create_instance(self, db_instance_id: str, db_instance_class: str, engine: str):
        """Cria uma instância RDS"""
        start = time.time()
        logger.info(f"Iniciando criação da instância RDS '{db_instance_id}'")
        response = self.rds.create_db_instance(
            DBInstanceIdentifier=db_instance_id,
            DBInstanceClass=db_instance_class,
            Engine=engine
        )
        duration = time.time() - start
        logger.info(f"Instância RDS '{db_instance_id}' criada em {duration:.2f}s")
        return response

    def delete_instance(self, db_instance_id: str, skip_final_snapshot: bool = True):
        """Exclui uma instância RDS"""
        start = time.time()
        logger.info(f"Iniciando exclusão da instância RDS '{db_instance_id}'")
        response = self.rds.delete_db_instance(
            DBInstanceIdentifier=db_instance_id,
            SkipFinalSnapshot=skip_final_snapshot
        )
        duration = time.time() - start
        logger.info(f"Instância RDS '{db_instance_id}' excluída em {duration:.2f}s")
        return response

    def start_instance(self, db_instance_id: str):
        """Inicia uma instância RDS"""
        start = time.time()
        logger.info(f"Iniciando instância RDS '{db_instance_id}'")
        response = self.rds.start_db_instance(DBInstanceIdentifier=db_instance_id)
        duration = time.time() - start
        logger.info(f"Instância RDS '{db_instance_id}' iniciada em {duration:.2f}s")
        return response

    def stop_instance(self, db_instance_id: str):
        """Para uma instância RDS"""
        start = time.time()
        logger.info(f"Parando instância RDS '{db_instance_id}'")
        response = self.rds.stop_db_instance(DBInstanceIdentifier=db_instance_id)
        duration = time.time() - start
        logger.info(f"Instância RDS '{db_instance_id}' parada em {duration:.2f}s")
        return response

    def describe_instance(self, db_instance_id: str):
        """Descreve detalhes de uma instância RDS"""
        start = time.time()
        logger.info(f"Iniciando descrição da instância RDS '{db_instance_id}'")
        response = self.rds.describe_db_instances(DBInstanceIdentifier=db_instance_id)
        duration = time.time() - start
        logger.info(f"Descrição da instância RDS '{db_instance_id}' concluída em {duration:.2f}s")
        return response.get("DBInstances", [])

    def backup_instance(self, db_instance_id: str, snapshot_id: str):
        """Cria um snapshot de backup da instância RDS"""
        start = time.time()
        logger.info(f"Iniciando backup da instância RDS '{db_instance_id}'")
        response = self.rds.create_db_snapshot(
            DBInstanceIdentifier=db_instance_id,
            DBSnapshotIdentifier=snapshot_id
        )
        duration = time.time() - start
        logger.info(f"Backup da instância RDS '{db_instance_id}' concluído em {duration:.2f}s")
        return response
