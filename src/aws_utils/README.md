# Projeto AWS Utils

## 🎯 Objetivo
Este projeto tem como objetivo fornecer uma **camada utilitária em Python** para interagir com diversos serviços da AWS de forma organizada, modular e extensível.  

A proposta central é simplificar o uso da AWS em aplicações e automações, oferecendo:
- **Abstração de complexidade**: encapsula chamadas da AWS em classes Python fáceis de usar.
- **Organização modular**: cada serviço (S3, IAM, DynamoDB, EC2, etc.) possui sua própria classe dedicada.
- **Segurança integrada**: utiliza IAM e STS para garantir que permissões e credenciais sejam aplicadas corretamente.
- **Automação de tarefas comuns**: operações como listar, criar, excluir e atualizar recursos são padronizadas.
- **Monitoramento e métricas**: gera relatórios de desempenho a partir dos logs, permitindo análise de tempo médio de execução por operação.
- **Extensibilidade**: novos serviços podem ser adicionados facilmente seguindo o mesmo padrão.

Em resumo, o projeto funciona como uma **biblioteca de apoio para desenvolvedores e engenheiros DevOps**, permitindo:
- Criar e gerenciar recursos AWS com poucas linhas de código.
- Integrar serviços diferentes em fluxos lógicos (ex.: IAM → S3 → EC2 → Lambda → Step Functions).
- Obter visibilidade sobre desempenho e tempo de resposta das operações.
- Facilitar testes e automações em ambientes de desenvolvimento, homologação e produção.
---

## 📂 Estrutura do Projeto
```
aws/
├── main.py                  # Script principal
├── main_s3.py               # Exemplo específico para S3
├── logs/app.log             # Arquivo de log das operações
├── files/                   # Arquivos auxiliares e exportações
├── aws_utils/
│   ├── client.py            # Cliente AWS centralizado
│   ├── logger.py            # Configuração de logs
│   ├── role.py              # Gerenciamento de roles
│   └── aws_services/
│       ├── S3Service.py
│       ├── IAMService.py
│       ├── DynamoDBService.py
│       ├── EC2Service.py
│       ├── StepFunctionsService.py
│       ├── LambdaService.py
│       ├── CloudWatchService.py
│       ├── SNSService.py
│       ├── SQSService.py
│       ├── RDSService.py
│       ├── CloudFormationService.py
│       ├── STSService.py
│       └── report/          # Relatórios de métricas
│           ├── s3_report_metrics.py
│           ├── iam_report_metrics.py
│           ├── dynamodb_report_metrics.py
│           ├── ec2_report_metrics.py
│           ├── stepfunctions_report_metrics.py
│           ├── lambda_report_metrics.py
│           ├── cloudwatch_report_metrics.py
│           ├── sns_report_metrics.py
│           ├── sqs_report_metrics.py
│           ├── rds_report_metrics.py
│           ├── cloudformation_report_metrics.py
│           └── sts_report_metrics.py
└── tests/
    └── test_client.py       # Testes unitários
```
---

## ⚙️ Recursos Implementados

### Serviços AWS
    - S3Service → buckets e objetos (listar, criar, upload, download, excluir, verificar vazio).
    - IAMService → roles e usuários (listar, criar, excluir, anexar políticas).
    - DynamoDBService → tabelas e itens (listar, criar, inserir, consultar, atualizar, excluir).
    - EC2Service → instâncias (listar, criar, iniciar, parar, terminar, descrever).
    - StepFunctionsService → state machines (listar, criar, excluir, iniciar execução, descrever, listar execuções).
    - LambdaService → funções (listar, criar, atualizar código, invocar, excluir).
    - CloudWatchService → métricas e logs (listar métricas, obter dados, criar/excluir alarmes, listar log groups, obter eventos).
    - SNSService → tópicos e mensagens (listar, criar, excluir, publicar, assinar, cancelar assinatura).
    - SQSService → filas e mensagens (listar, criar, excluir, enviar, receber, excluir mensagens).
    - RDSService → instâncias de banco (listar, criar, excluir, iniciar, parar, descrever, backup).
    - CloudFormationService → stacks (listar, criar, atualizar, excluir, descrever).
    - STSService → segurança (assume role, identidade do chamador, token de sessão).

---

### Relatórios de Métricas
- Scripts em `aws_utils/aws_services/report/` analisam o `logs/app.log` e calculam a **duração média das operações** por serviço.
- Cada relatório é independente e pode ser executado diretamente.

---

### 🧭 Sequência lógica recomendada

| Etapa | Serviço | Função principal | Observação |
|----|---|---|---|
| 1️⃣ | **[IAMService](ca://s?q=Como_usar_IAMService)** | Criação de roles, usuários e políticas | Define quem pode acessar e operar recursos AWS. Deve ser o primeiro passo. |
| 2️⃣ | **[STSService](ca://s?q=Como_usar_STSService)** | Assume roles e gera tokens temporários | Usado para autenticação segura antes de acessar outros serviços. |
| 3️⃣ | **[S3Service](ca://s?q=Como_usar_S3Service)** | Armazenamento de arquivos e logs | Base para guardar dados, backups e artefatos de deploy. |
| 4️⃣ | **[DynamoDBService](ca://s?q=Como_usar_DynamoDBService)** | Banco NoSQL para metadados e estados | Ideal para persistir informações de execução ou configurações. |
| 5️⃣ | **[EC2Service](ca://s?q=Como_usar_EC2Service)** | Criação e gerenciamento de instâncias | Requer roles e permissões definidas no IAM. |
| 6️⃣ | **[RDSService](ca://s?q=Como_usar_RDSService)** | Banco relacional | Pode depender de VPCs e roles criadas anteriormente. |
| 7️⃣ | **[LambdaService](ca://s?q=Como_usar_LambdaService)** | Funções serverless | Usa roles IAM e pode interagir com S3, DynamoDB, SNS, etc. |
| 8️⃣ | **[StepFunctionsService](ca://s?q=Como_usar_StepFunctionsService)** | Orquestração de workflows | Integra Lambda, DynamoDB, SQS e outros serviços. |
| 9️⃣ | **[SQSService](ca://s?q=Como_usar_SQSService)** | Fila de mensagens | Usado para desacoplar processos entre EC2, Lambda e Step Functions. |
| 🔟 | **[SNSService](ca://s?q=Como_usar_SNSService)** | Notificações e alertas | Envia mensagens para usuários ou sistemas externos. |
| 1️⃣1️⃣ | **[CloudWatchService](ca://s?q=Como_usar_CloudWatchService)** | Monitoramento e métricas | Coleta logs e métricas de todos os serviços anteriores. |
| 1️⃣2️⃣ | **[CloudFormationService](ca://s?q=Como_usar_CloudFormationService)** | Infraestrutura como código | Pode automatizar toda a criação acima via templates. |

---

## ⚙️ Exemplo de fluxo prático

### Exemplo: Usando o S3Service
```python
from aws_utils.client import AwsClient
from aws_utils.aws_services.IAMService import IAMService
from aws_utils.aws_services.S3Service import S3Service
from aws_utils.aws_services.EC2Service import EC2Service

client = AwsClient()

# 1️⃣ Criar role IAM
iam = IAMService(client)
iam.create_role("AppExecutionRole", assume_policy="...")

# 2️⃣ Criar bucket S3 para armazenar logs
s3 = S3Service(client)
s3.create_bucket("app-logs-bucket")

# 3️⃣ Criar instância EC2 com role e bucket configurados
ec2 = EC2Service(client)
ec2.create_instance(image_id="ami-123456", instance_type="t2.micro")

```
---

### 🧩 Dica de integração
IAM e STS sempre vêm primeiro — são a base de segurança.

S3, DynamoDB, RDS e EC2 formam o núcleo de dados e computação.

Lambda, Step Functions, SQS e SNS cuidam da automação e comunicação.

CloudWatch e CloudFormation fecham o ciclo com monitoramento e infraestrutura automatizada.

---

## 🧪 Testes
- Os testes unitários estão em `tests/`.  
- Exemplo de execução:
```bash
pytest tests/
```

---
## 🧭 Sequência lógica de uso das classes AWS

```

IAMService
 └── STSService
      ├── S3Service
      │    └── LambdaService
      │         └── StepFunctionsService
      │              ├── SQSService
      │              └── SNSService
      ├── DynamoDBService
      │    └── LambdaService
      ├── EC2Service
      │    └── SQSService
      ├── RDSService
      └── CloudFormationService
           └── (automatiza todos os serviços acima)

Monitoramento:
 └── CloudWatchService
      ├── EC2Service
      ├── LambdaService
      ├── StepFunctionsService
      ├── SQSService
      ├── SNSService
      ├── RDSService
      └── S3Service
```

## 📋 Pré-requisitos

Antes de utilizar o projeto, certifique-se de ter instalado e configurado:

- **Python 3.12** ou superior  
- **pip** (gerenciador de pacotes do Python)  
- **AWS CLI** configurado (opcional, mas recomendado)  
- Bibliotecas necessárias:
  - [boto3](ca://s?q=Instalar_boto3)
  - [pytest](ca://s?q=Instalar_pytest)

Além disso, é necessário possuir **credenciais AWS válidas** (Access Key e Secret Key) com permissões adequadas para os serviços que deseja utilizar.

---

## ⚙️ Instalação e Configuração

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/seuusuario/aws-utils.git
   cd aws-utils

2. **Instalar dependências**
    ```bash
    pip install -r requirements.txt

3. **Configurar credenciais AWS**

    Crie um arquivo .env na raiz do projeto:

    ```bash
    AWS_ACCESS_KEY_ID=seu_access_key
    AWS_SECRET_ACCESS_KEY=sua_secret_key
    AWS_DEFAULT_REGION=us-east-1

4. **Alternativamente, configure via AWS CLI:**

    ```bash
    aws configure
---
## Visão Arquitetural
  Mostrando como a biblioteca AWS se encaixa dentro de uma aplicação maior, cobrindo infraestrutura, dados, automação e monitoramento.
```
Arquitetura da Biblioteca AWS Utils
==================================

                 +-------------------+
                 |   Aplicação       |
                 |   Infraestrutura  |
                 +---------+---------+
                           |
                           v
                 +-------------------+
                 | Biblioteca AWS    |
                 | (aws_utils)       |
                 +---------+---------+
                           |
   -------------------------------------------------
   |                   |                   |       |
   v                   v                   v       v
+---------+       +-----------+       +-----------+ +-----------+
| Segurança|       | Dados     |       | Computação| | Automação |
| IAM/STS  |       | S3, RDS,  |       | EC2,      | | Lambda,   |
|          |       | DynamoDB, |       | Aurora    | | Step Func |
+---------+       +-----------+       +-----------+ +-----------+
                           |
                           v
                 +-------------------+
                 | Comunicação       |
                 | SQS, SNS          |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | Monitoramento     |
                 | CloudWatch        |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | Infraestrutura    |
                 | CloudFormation    |
                 +-------------------+

```
---

## 🔍 Interpretação da Arquitetura

- Segurança (IAM/STS) → base inicial, define permissões e credenciais.
- Dados (S3, RDS, DynamoDB, Aurora, DocumentDB) → armazenamento estruturado e não estruturado.
- Computação (EC2, Lambda, Step Functions) → execução de workloads e orquestração de processos.
- Comunicação (SQS, SNS) → integração assíncrona e notificações.
- Monitoramento (CloudWatch) → coleta métricas e logs de todos os serviços.
- Infraestrutura (CloudFormation) → automatiza a criação e manutenção de toda a arquitetura.

---

## 📌 Conclusão
Este projeto fornece uma **base sólida para automação com AWS**, incluindo:

- Serviços encapsulados em classes Python, que abstraem a complexidade das chamadas da AWS.  
- Logs detalhados com métricas de tempo, permitindo análise de desempenho.  
- Relatórios independentes para cada serviço, facilitando a identificação de gargalos.  
- Estrutura modular e extensível, possibilitando a adição de novos serviços com facilidade.  

Além disso, a biblioteca **AWS Utils** já cobre todos os pilares de uma aplicação de infraestrutura moderna:

- **Segurança** → [IAMService](ca://s?q=Como_usar_IAMService) e [STSService](ca://s?q=Como_usar_STSService).  
- **Dados** → [DynamoDBService](ca://s?q=Como_usar_DynamoDBService), [RDSService](ca://s?q=Como_usar_RDSService) (MySQL, PostgreSQL, SQL Server), [S3Service](ca://s?q=Como_usar_S3Service).  
- **Computação** → [EC2Service](ca://s?q=Como_usar_EC2Service), [LambdaService](ca://s?q=Como_usar_LambdaService), [StepFunctionsService](ca://s?q=Como_usar_StepFunctionsService).  
- **Comunicação** → [SQSService](ca://s?q=Como_usar_SQSService), [SNSService](ca://s?q=Como_usar_SNSService).  
- **Monitoramento** → [CloudWatchService](ca://s?q=Como_usar_CloudWatchService).  
- **Infraestrutura como código** → [CloudFormationService](ca://s?q=Como_usar_CloudFormationService).  

Ela pode ser considerada uma **camada central de abstração para aplicações DevOps e arquiteturas em nuvem**, robusta o suficiente para ser usada em produção.  
Combinando segurança, dados, computação, comunicação, monitoramento e infraestrutura como código, o projeto se posiciona como uma solução completa para automação e gestão de recursos AWS.
  

---
## 📞 Informações de Contato

 - Desenvolvedor: [LinkedIn](https://www.linkedin.com/in/alessandro-silvestre-devops/)
 - Email: devops.asilvestre@gmail.com
 