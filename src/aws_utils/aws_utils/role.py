# aws_utils/role.py
"""
Módulo de utilidades para assumir roles na AWS usando STS.
"""

from typing import List, Optional
import boto3
from botocore.exceptions import ClientError


def assume_role(
    session: boto3.Session,
    role_arn: str,
    role_session_name: str = "aws_utils_session",
    duration_seconds: int = 3600,
) -> boto3.Session:
    """
    Assume uma única role e devolve uma nova sessão boto3 com as credenciais temporárias.

    :param session: Sessão boto3 com credenciais iniciais (pode ser a sessão padrão).
    :param role_arn: ARN completo da role a ser assumida.
    :param role_session_name: Nome descritivo da sessão (usado no CloudTrail).
    :param duration_seconds: Duração em segundos da sessão temporária (máx. 12h).
    :return: Nova sessão boto3 autenticada com a role assumida.
    """
    sts = session.client("sts")
    try:
        response = sts.assume_role(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            DurationSeconds=duration_seconds,
        )
        creds = response["Credentials"]
        return boto3.Session(
            aws_access_key_id=creds["AccessKeyId"],
            aws_secret_access_key=creds["SecretAccessKey"],
            aws_session_token=creds["SessionToken"],
            region_name=session.region_name,
        )
    except ClientError as e:
        raise RuntimeError(f"Falha ao assumir role {role_arn}: {e}") from e


def assume_multiple_roles(
    session: boto3.Session,
    role_arns: List[str],
    role_session_name: str = "aws_utils_session",
    duration_seconds: int = 3600,
) -> boto3.Session:
    """
    Assume uma sequência de roles. Cada chamada de `assume_role` sobrepõe a sessão
    anterior, de modo que a última role da lista será a que permanece.

    :param session: Sessão boto3 inicial.
    :param role_arns: Lista de ARNs de roles, em ordem de assunção.
    :return: Sessão boto3 final com a última role assumida.
    """
    current_session = session
    for idx, arn in enumerate(role_arns, start=1):
        print(f"Assumindo role {idx}/{len(role_arns)}: {arn}")
        current_session = assume_role(
            session=current_session,
            role_arn=arn,
            role_session_name=f"{role_session_name}_{idx}",
            duration_seconds=duration_seconds,
        )
    return current_session