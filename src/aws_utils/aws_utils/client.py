# aws_utils/client.py
"""
Módulo principal da biblioteca aws_utils.
Responsável por criar sessões e clientes boto3 com suporte a múltiplas roles.
"""

import boto3
from botocore.exceptions import ClientError
from typing import List, Optional, Any

# Importa as funções auxiliares de role.py
from .role import assume_multiple_roles


class AwsClient:
    """
    Wrapper que:
        1. Cria uma sessão boto3 com credenciais (explícitas ou padrão).
        2. Assume uma lista de roles (se fornecida) usando STS.
        3. Exponha métodos `client()` e `resource()` já autenticados.
    """

    def __init__(
        self,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        region_name: Optional[str] = None,
        roles: Optional[List[str]] = None,
    ):
        """
        :param aws_access_key_id:    Chave de acesso (opcional)
        :param aws_secret_access_key: Segredo de acesso (opcional)
        :param aws_session_token:    Token de sessão (opcional, usado com STS)
        :param region_name:          Região AWS (ex.: 'us-east-1')
        :param roles:                Lista de ARNs de roles a serem assumidas
        """
        # 1️⃣ Cria a sessão base (pode usar credenciais padrão)
        self.base_session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            region_name=region_name,
        )

        # 2️⃣ Se houver roles, delega a role.py para assumir todas
        self.session = (
            assume_multiple_roles(
                session=self.base_session,
                role_arns=roles,
                role_session_name="aws_utils_session",
                duration_seconds=3600,
            )
            if roles
            else self.base_session
        )

    # ------------------------------------------------------------------
    #  Métodos públicos
    # ------------------------------------------------------------------
    def client(self, service_name: str, **kwargs) -> Any:
        """
        Retorna um cliente boto3 já autenticado para o serviço desejado.
        Ex.: client("s3").list_buckets()
        """
        return self.session.client(service_name, **kwargs)

    def resource(self, service_name: str, **kwargs) -> Any:
        """
        Retorna um recurso boto3 já autenticado.
        Ex.: resource("s3").Bucket("meu-bucket")
        """
        return self.session.resource(service_name, **kwargs)

    # ------------------------------------------------------------------
    #  Helper interno (opcional)
    # ------------------------------------------------------------------
    def _assume_roles(self, roles: List[str]) -> boto3.Session:
        """
        Função interna para manter compatibilidade se alguém usar o método
        diretamente. Ela chama a função do role.py.
        """
        return assume_multiple_roles(
            session=self.base_session,
            role_arns=roles,
            role_session_name="aws_utils_session",
            duration_seconds=3600,
        )