# aws_utils/aws_services/S3Service.py
# S3 - Armazenamento de objetos.
import time
from aws_utils.client import AwsClient
from aws_utils.logger import setup_logger

logger = setup_logger(__name__)

class S3Service:
    def __init__(self, client: AwsClient):
        self.s3 = client.client("s3")

    def list_buckets(self):
        """Lista todos os buckets S3"""
        start = time.time()
        logger.info("Iniciando listagem de buckets S3")
        response = self.s3.list_buckets().get("Buckets", [])
        duration = time.time() - start
        logger.info(f"Finalizada listagem de buckets S3 em {duration:.2f}s")
        return response

    def create_bucket(self, bucket_name: str, region: str = "us-east-1"):
        """Cria um bucket S3"""
        start = time.time()
        logger.info(f"Iniciando criação do bucket '{bucket_name}' na região {region}")
        if region == "us-east-1":
            response = self.s3.create_bucket(Bucket=bucket_name)
        else:
            response = self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region}
            )
        duration = time.time() - start
        logger.info(f"Bucket '{bucket_name}' criado em {duration:.2f}s")
        return response

    def upload_file(self, file_path: str, bucket_name: str, object_name: str = None):
        """Faz upload de um arquivo para o bucket"""
        start = time.time()
        if object_name is None:
            object_name = file_path.split("/")[-1]
        logger.info(f"Iniciando upload do arquivo '{file_path}' para bucket '{bucket_name}' como '{object_name}'")
        self.s3.upload_file(file_path, bucket_name, object_name)
        duration = time.time() - start
        logger.info(f"Upload concluído em {duration:.2f}s")
        return object_name

    def download_file(self, bucket_name: str, object_name: str, dest_path: str):
        """Faz download de um arquivo do bucket"""
        start = time.time()
        logger.info(f"Iniciando download do objeto '{object_name}' do bucket '{bucket_name}' para '{dest_path}'")
        self.s3.download_file(bucket_name, object_name, dest_path)
        duration = time.time() - start
        logger.info(f"Download concluído em {duration:.2f}s")
        return dest_path

    def delete_file(self, bucket_name: str, object_name: str):
        """Exclui um arquivo (objeto) do bucket"""
        start = time.time()
        logger.info(f"Iniciando exclusão do objeto '{object_name}' do bucket '{bucket_name}'")
        response = self.s3.delete_object(Bucket=bucket_name, Key=object_name)
        duration = time.time() - start
        logger.info(f"Objeto '{object_name}' excluído em {duration:.2f}s")
        return response

    def delete_bucket(self, bucket_name: str):
        """Exclui um bucket S3 (precisa estar vazio)"""
        start = time.time()
        logger.info(f"Iniciando exclusão do bucket '{bucket_name}'")
        response = self.s3.delete_bucket(Bucket=bucket_name)
        duration = time.time() - start
        logger.info(f"Bucket '{bucket_name}' excluído em {duration:.2f}s")
        return response

    def isEmpty_Bucket(self, bucket_name: str):
        """Verifica se o bucket está vazio"""
        start = time.time()
        logger.info(f"Verificando se o bucket '{bucket_name}' está vazio")
        response = self.s3.list_objects_v2(Bucket=bucket_name)
        is_empty = response.get("KeyCount", 0) == 0
        duration = time.time() - start
        logger.info(f"Verificação concluída em {duration:.2f}s. Bucket vazio: {is_empty}")
        return is_empty
