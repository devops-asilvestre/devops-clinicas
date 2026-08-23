import boto3
import psycopg2

# Configurações
DYNAMODB_TABLE = "ClinicasAtendimentos"
RDS_ENDPOINT = "clinicas-relatorios.xxxxxxx.us-east-1.rds.amazonaws.com"
RDS_DB = "postgres"
RDS_USER = "admin"
RDS_PASSWORD = "SuperSecret123"

# Inicializa clientes AWS
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DYNAMODB_TABLE)

# Função para popular DynamoDB
def popular_dynamodb():
    atendimentos_iniciais = [
        {"ClinicaId": "SP001", "AtendimentoId": "A001", "Paciente": "João", "Tipo": "Convênio", "Valor": 200},
        {"ClinicaId": "SP001", "AtendimentoId": "A002", "Paciente": "Maria", "Tipo": "ProBono", "Valor": 0},
        {"ClinicaId": "RJ001", "AtendimentoId": "A003", "Paciente": "Carlos", "Tipo": "Particular", "Valor": 300},
    ]
    for item in atendimentos_iniciais:
        table.put_item(Item=item)
    print("✅ DynamoDB populado com atendimentos iniciais.")

# Função para popular RDS
def popular_rds():
    conn = psycopg2.connect(
        host=RDS_ENDPOINT,
        database=RDS_DB,
        user=RDS_USER,
        password=RDS_PASSWORD
    )
    cur = conn.cursor()

    # Criação da tabela de relatórios
    cur.execute("""
        CREATE TABLE IF NOT EXISTS RelatoriosMensais (
            ClinicaId VARCHAR(10),
            Mes VARCHAR(7),
            TotalAtendimentos INT,
            ProBonoAtendimentos INT,
            ReceitaTotal DECIMAL
        );
    """)

    # Inserção de dados iniciais
    relatorios_iniciais = [
        ("SP001", "2026-08", 2, 1, 200),
        ("RJ001", "2026-08", 1, 0, 300),
    ]
    cur.executemany("""
        INSERT INTO RelatoriosMensais (ClinicaId, Mes, TotalAtendimentos, ProBonoAtendimentos, ReceitaTotal)
        VALUES (%s, %s, %s, %s, %s);
    """, relatorios_iniciais)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ RDS populado com relatórios iniciais.")

if __name__ == "__main__":
    popular_dynamodb()
    popular_rds()
