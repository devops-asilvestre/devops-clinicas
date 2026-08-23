# O Projeto

Vamos desenhar um **cenário de negócio** para essa rede de clínicas odontológicas, que servirá como base para a aplicação DevOps que vamos construir. Nós somos responsáveis pelo desenvolvimento DevOps em Python, ou seja, pela camada de automação, infraestrutura e monitoramento. Não precisamos construir o front-end ou a API de negócio, mas sim a espinha dorsal DevOps que garante que os eventos publicados no SNS/SQS sejam processados corretamente e que toda a infraestrutura esteja sob controle.

---

## 🏢 Cenário da Empresa
- **Empresa**: Rede de Clínicas Odontológicas (25 unidades).  
- **Proprietário**: Sr. Roberto (nome fictício).  
- **Público-alvo**: pacientes de classe social alta.  
- **Regra de negócio atual**: cada clínica deve atender **10 pacientes pro-bono por mês** (atendimento gratuito obrigatório).  
- **Objetivo estratégico**: acompanhar o crescimento da rede com suporte tecnológico, garantindo **padronização, monitoramento e escalabilidade**.  

---

## 🎯 Desafios identificados
- **Gestão centralizada**: Sr. Roberto precisa acompanhar todas as clínicas em tempo real.  
- **Controle de regras de negócio**: garantir que cada clínica cumpra os 10 atendimentos gratuitos mensais.  
- **Integração de dados**: consolidar informações de pacientes, atendimentos e métricas em um único sistema.  
- **Escalabilidade**: permitir que novas clínicas sejam adicionadas sem complicações técnicas.  
- **Monitoramento**: acompanhar métricas de desempenho (quantidade de atendimentos, tempo médio, cumprimento das metas).  

---

## 🛠️ Aplicação DevOps proposta
A aplicação será construída sobre o **framework AWS Utils** que você já tem, e terá como foco:

1. **Eventos AWS (SNS/SQS/EventBridge)**  
   - Cada atendimento gera um **JSON** com dados do paciente e da clínica.  
   - Esse evento dispara **Lambda** ou **Step Functions**.  

2. **Processamento (Lambda/Step Functions)**  
   - Valida se o atendimento é pro-bono ou pago.  
   - Atualiza o banco de dados (DynamoDB ou RDS).  
   - Aplica regras de negócio (ex.: contar os 10 atendimentos gratuitos).  

3. **Persistência (DataServers)**  
   - **DynamoDB**: armazena atendimentos em tempo real.  
   - **RDS (MySQL/PostgreSQL)**: consolida relatórios mensais.  

4. **Monitoramento (CloudWatch)**  
   - Métricas por clínica: número de atendimentos, cumprimento da meta pro-bono.  
   - Alertas via **SNS** se alguma clínica não atingir os 10 atendimentos gratuitos.  

5. **Infraestrutura como código (CloudFormation)**  
   - Toda a arquitetura provisionada automaticamente.  
   - Fácil replicação para novas clínicas.  

---

## 📊 Fluxo ASCII da aplicação

```plaintext
Paciente → Clínica → Front-end
   ↓
API C# (AtendimentoRegistrado)
   ↓
AWS SDK → SNS (evento JSON)
   ↓
SNS Topic
   ↓
Lambda / Step Functions
   ↓
Validação + Regras de negócio
   ↓
Persistência (DynamoDB + RDS)
   ↓
CloudWatch (métricas e alertas)
   ↓
Dashboard (Sr. Roberto acompanha rede)
```

---
## Estrutura de pastas
```
src/
│
├── aws_utils/                         # Framework central para integração AWS
│   ├── client.py                      # Cliente AWS central
│   ├── aws_services/                  # Serviços encapsulados
│   │   ├── CloudFormationService.py   # Gerencia stacks CloudFormation
│   │   ├── CloudWatchService.py       # Monitora métricas e alarmes
│   │   ├── DynamoDBService.py         # Operações com tabelas DynamoDB
│   │   ├── EC2Service.py              # Gerencia instâncias EC2
│   │   ├── IAMService.py              # Gerencia usuários e permissões IAM
│   │   ├── LambdaService.py           # Criação e execução de funções Lambda
│   │   ├── RDSService.py              # Conexão e operações com RDS
│   │   ├── S3Service.py               # Operações com buckets S3
│   │   ├── SNSService.py              # Publicação em tópicos SNS
│   │   ├── SQSService.py              # Gerenciamento de filas SQS
│   │   ├── StepFunctionsService.py    # Orquestração de workflows
│   │   └── STSService.py              # Tokens temporários de segurança
│   └── utils/
│       └── logger.py                  # Logs e métricas
│
├── pipelines/                         # Definições de CI/CD
│   ├── codepipeline_atendimento.py    # Pipeline para processar eventos de atendimento
│   └── codedeploy_config.py           # Configuração de deploy automatizado
│
├── lambdas/                           # Funções Lambda (Python)
│   ├── process_event.py               # Consome evento SNS/SQS e grava no DynamoDB
│   ├── validar_probono.py             # Valida regra dos atendimentos gratuitos
│   └── atualizar_relatorio.py         # Atualiza métricas no RDS
│
├── step_functions/                    # Fluxos orquestrados
│   └── atendimento_workflow.json      # Workflow: validar → persistir → notificar
│
├── infra/                             # Infraestrutura como código
│   ├── cloudformation_template.yaml   # Provisiona recursos AWS (SNS, Lambda, DynamoDB, RDS, Step Functions)
│   └── init_script.py                 # Popula dados iniciais em DynamoDB e RDS
│
├── monitoring/                        # Monitoramento e alertas
│   ├── cloudwatch_dashboard.json      # Dashboard de métricas
│   └── sns_alerts_config.json         # Configuração de alertas via SNS
│
├── tests/                             # Testes automatizados
│   ├── unit/
│   │   └── test_sns_publish.py        # Teste unitário de publicação SNS
│   ├── integration/
│   │   └── test_lambda_flow.py        # Teste de integração do fluxo Lambda
│   ├── performance/
│   │   └── performance_test.py        # Teste de carga e escalabilidade
│   └── e2e/
│       └── test_full_pipeline.py      # Teste ponta a ponta do pipeline
│
└── docs/                              # Documentação DevOps
    ├── arquitetura.md                  # Arquitetura geral do sistema
    ├── checklist_entrega.md            # Checklist final de entrega
    ├── cicd.md                         # Pipeline CI/CD
    ├── escalabilidade.md               # Estratégias de escalabilidade
    ├── executar_sistema.md             # Guia prático de execução
    ├── governanca.md                   # Governança e auditoria
    ├── monitoramento.md                # Monitoramento e alertas
    ├── onboarding.md                   # Integração de novos membros
    ├── operacoes.md                    # Rotinas operacionais
    ├── roadmap.md                      # Evolução planejada
    ├── seguranca.md                    # Segurança e LGPD
    ├── suporte.md                      # Canais de suporte e SLA
    ├── testes.md                       # Estratégia de testes
    └── treinamento.md                  # Capacitação da equipe
```
---

## 📌 Conclusão
Esse cenário mostra como a rede de clínicas pode usar tecnologia como **estratégia de negócio**:  
- Cada atendimento vira um **evento DevOps**.  
- O sistema garante que as regras (10 pro-bono/mês) sejam cumpridas.  
- O proprietário tem **visibilidade centralizada** e pode expandir a rede sem perder controle.  


---

## 📊 Modelo de Dados — DynamoDB (tempo real)
O **modelo de dados DevOps** que sustentará o cenário da rede de clínicas odontológicas. Como nosso foco é Python + AWS, vamos pensar em como estruturar **DynamoDB** (para dados em tempo real) e **RDS** (para relatórios consolidados).  

DynamoDB é ideal para armazenar os **eventos de atendimento** publicados via SNS/SQS.  
Cada item representa um atendimento realizado em uma clínica.

**Tabela: `Atendimentos`**
- **Partition Key**: `clinicaId` (identificador da clínica)  
- **Sort Key**: `atendimentoId` (UUID do atendimento)  
- **Atributos adicionais**:  
  - `pacienteId`  
  - `tipoAtendimento` (pro-bono ou pago)  
  - `dataHora`  
  - `valor`  
  - `status` (concluído, cancelado)  

Exemplo de item:
```json
{
  "clinicaId": "CLINICA-001",
  "atendimentoId": "ATT-12345",
  "pacienteId": "PAC-67890",
  "tipoAtendimento": "pro-bono",
  "dataHora": "2026-08-22T22:00:00Z",
  "valor": 0.00,
  "status": "concluido"
}
```

---

## 📊 Modelo de Dados — RDS (relatórios mensais)
RDS (MySQL/PostgreSQL) será usado para consolidar relatórios e análises.  
Aqui teremos tabelas relacionais para cruzar informações.

**Tabela: `Clinicas`**
- `clinicaId` (PK)  
- `nome`  
- `endereco`  
- `responsavel`  

**Tabela: `Pacientes`**
- `pacienteId` (PK)  
- `nome`  
- `cpf`  
- `classeSocial`  

**Tabela: `Atendimentos`**
- `atendimentoId` (PK)  
- `clinicaId` (FK → Clinicas)  
- `pacienteId` (FK → Pacientes)  
- `tipoAtendimento`  
- `dataHora`  
- `valor`  
- `status`  

**Tabela: `RelatoriosMensais`**
- `relatorioId` (PK)  
- `clinicaId` (FK → Clinicas)  
- `mesReferencia`  
- `totalAtendimentos`  
- `totalProBono`  
- `totalPagos`  
- `receitaTotal`  

---

## 🔍 Como funciona na prática
1. **Evento SNS/SQS** → JSON publicado pela API.  
2. **Lambda** → consome o evento e grava no **DynamoDB**.  
3. **Step Functions** → ao final do mês, consolida dados do DynamoDB em **RDS**.  
4. **CloudWatch** → monitora se cada clínica atingiu os 10 atendimentos pro-bono.  
5. **Dashboard** → Sr. Roberto visualiza relatórios mensais consolidados.  

---

## 📌 Conclusão
- **DynamoDB** → armazena eventos em tempo real (cada atendimento).  
- **RDS** → consolida relatórios mensais e análises financeiras.  
- Essa combinação garante **velocidade + consistência**: DynamoDB para ingestão rápida, RDS para relatórios estruturados.  

---

## 📊 Pipeline DevOps — Fluxo de Atendimento

```plaintext
Usuário confirma atendimento
        ↓
Front-end → API C#
        ↓
API publica evento JSON no SNS
        ↓
SNS Topic
        ↓
Lambda (process_event.py)
   - Lê JSON
   - Valida dados
   - Identifica se é pro-bono ou pago
        ↓
DynamoDB (tempo real)
   - Armazena atendimento
   - Atualiza contador de pro-bono
        ↓
Step Functions (atendimento_workflow.json)
   - Orquestra fluxo mensal
   - Consolida dados
   - Atualiza RDS (relatórios mensais)
        ↓
RDS (MySQL/PostgreSQL)
   - Relatórios consolidados
   - Receita total
   - Cumprimento da meta pro-bono
        ↓
CloudWatch
   - Métricas por clínica
   - Alertas se meta não atingida
        ↓
Dashboard (Sr. Roberto)
   - Visualiza status da rede
   - Acompanha desempenho em tempo real
```

---

## 🔍 Interpretação
- **SNS** → recebe o evento da API.  
- **Lambda** → processa o evento e grava no DynamoDB.  
- **DynamoDB** → armazena atendimentos em tempo real.  
- **Step Functions** → consolida dados e atualiza RDS.  
- **RDS** → gera relatórios mensais e financeiros.  
- **CloudWatch** → monitora métricas e envia alertas.  
- **Dashboard** → Sr. Roberto acompanha tudo centralizado.  

---

## 📌 Conclusão
Esse pipeline mostra como o **evento de negócio (atendimento)** vira um **gatilho DevOps**:  
- É processado em tempo real (Lambda + DynamoDB).  
- Consolidado em relatórios (Step Functions + RDS).  
- Monitorado com métricas e alertas (CloudWatch).  
- Exposto em dashboards para gestão estratégica.  

---

## 📞 Informações de Contato
- **Perfil Desenvolvedor**: [LinkedIn](https://www.linkedin.com/in/alessandro-silvestre-devops/)
- **Email**: [devops.asilvestre@gmail.com](mailto:devops.asilvestre@gmail.com)
