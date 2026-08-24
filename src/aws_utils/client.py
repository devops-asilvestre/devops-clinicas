# main.py
"""
Exemplo de uso da biblioteca aws_utils.
Agora:
  • Carrega credenciais do arquivo .env.
  • Usa logger em vez de print.
  • Demonstra uso de DynamoDB, EC2 e Step Functions.
"""

import os
from dotenv import load_dotenv
from aws_utils import AwsClient
from aws_utils.logger import setup_logger
from aws_utils.aws_services import DynamoDBService, EC2Service, StepFunctionsService

# ------------------------------------------------------------------
#  Carregar variáveis do .env
# ------------------------------------------------------------------
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")  # pode ser None
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

ROLES = []  # Lista de ARNs de roles, se necessário

# ------------------------------------------------------------------
#  Configuração do logger
# ------------------------------------------------------------------
logger = setup_logger(__name__)

# ------------------------------------------------------------------
#  Criação do cliente AWS
# ------------------------------------------------------------------
client = AwsClient(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION,
    roles=ROLES if ROLES else None,
)

# ------------------------------------------------------------------
#  Exemplo 1: Listar buckets S3
# ------------------------------------------------------------------
try:
    s3 = client.client("s3")
    buckets = s3.list_buckets()
    logger.info("=== Buckets S3 ===")
    for bucket in buckets.get("Buckets", []):
        logger.info(f" - {bucket['Name']}")
except Exception as e:
    logger.error(f"Erro ao listar buckets S3: {e}")

# ------------------------------------------------------------------
#  Exemplo 2: Listar roles IAM
# ------------------------------------------------------------------
try:
    iam = client.client("iam")
    roles = iam.list_roles()
    logger.info("=== Roles IAM ===")
    for role in roles.get("Roles", []):
        logger.info(f" - {role['RoleName']} (ARN: {role['Arn']})")
except Exception as e:
    logger.error(f"Erro ao listar roles IAM: {e}")

# ------------------------------------------------------------------
#  Exemplo 3: Listar tabelas DynamoDB
# ------------------------------------------------------------------
try:
    tables = DynamoDBService.list_tables(client)
    logger.info("=== Tabelas DynamoDB ===")
    for table in tables:
        logger.info(f" - {table}")
except Exception as e:
    logger.error(f"Erro ao listar tabelas DynamoDB: {e}")

# ------------------------------------------------------------------
#  Exemplo 4: Listar instâncias EC2
# ------------------------------------------------------------------
try:
    instances = EC2Service.list_instances(client)
    logger.info("=== Instâncias EC2 ===")
    for reservation in instances:
        for instance in reservation.get("Instances", []):
            logger.info(f" - {instance['InstanceId']} ({instance['State']['Name']})")
except Exception as e:
    logger.error(f"Erro ao listar instâncias EC2: {e}")

# ------------------------------------------------------------------
#  Exemplo 5: Listar state machines do Step Functions
# ------------------------------------------------------------------
try:
    state_machines = StepFunctionsService.list_state_machines(client)
    logger.info("=== Step Functions ===")
    for sm in state_machines:
        logger.info(f" - {sm['name']} (ARN: {sm['stateMachineArn']})")
except Exception as e:
    logger.error(f"Erro ao listar Step Functions: {e}")

# ------------------------------------------------------------------
# Exemplo 6: Criar tabela DynamoDB
# ------------------------------------------------------------------
try:
    response = DynamoDBService.create_table(client, "TestTable")
    logger.info(f"Tabela criada: {response['TableDescription']['TableName']}")
except Exception as e:
    logger.error(f"Erro ao criar tabela DynamoDB: {e}")

# ------------------------------------------------------------------
# Exemplo 7: Criar instância EC2
# ------------------------------------------------------------------
try:
    response = EC2Service.create_instance(client, ami_id="ami-0c55b159cbfafe1f0")  # exemplo de AMI Amazon Linux
    logger.info(f"Instância criada: {response['InstanceId']} (estado: {response['State']['Name']})")
except Exception as e:
    logger.error(f"Erro ao criar instância EC2: {e}")

# ------------------------------------------------------------------
# Exemplo 8: Criar e executar State Machine no Step Functions
# ------------------------------------------------------------------
try:
    definition = """
    {
      "Comment": "Exemplo Hello World",
      "StartAt": "HelloWorld",
      "States": {
        "HelloWorld": {
          "Type": "Pass",
          "Result": "Hello World!",
          "End": true
        }
      }
    }
    """
    role_arn = "arn:aws:iam::383158157790:role/service-role/StepFunctions-HelloWorldStateMachine-role-ip9lz78ij"
    response = StepFunctionsService.create_state_machine(client, "HelloWorldStateMachine", definition, role_arn)
    logger.info(f"State Machine criada: {response['stateMachineArn']}")

    # Iniciar execução
    exec_response = StepFunctionsService.start_execution(client, response["stateMachineArn"])
    logger.info(f"Execução iniciada: {exec_response['executionArn']}")

    # Consultar status
    status = StepFunctionsService.describe_execution(client, exec_response["executionArn"])
    logger.info(f"Status da execução: {status['status']}")
    logger.info(f"Saída: {status.get('output')}")
except Exception as e:
    logger.error(f"Erro ao criar/rodar State Machine: {e}")
