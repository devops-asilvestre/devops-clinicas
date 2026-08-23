# Arquitetura DevOps — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Garantir que cada clínica da rede:
- Registre atendimentos em tempo real.
- Cumpra a meta de 10 atendimentos pro-bono/mês.
- Consolide relatórios financeiros e sociais.
- Disponibilize métricas e alertas para o Sr. Roberto.

---

## 🏗️ Componentes Principais

### [SNS](ca://s?q=Explicar_SNS)
- Recebe eventos JSON da API.
- Publica mensagens para acionar Lambdas.

### [Lambda](ca://s?q=Explicar_AWS_Lambda)
- `devops-clinicas/lambdas/process_event.py` → grava atendimentos no DynamoDB.
- `devops-clinicas/lambdas/validar_probono.py` → valida regra dos 10 atendimentos gratuitos.
- `devops-clinicas/lambdas/atualizar_relatorio.py` → consolida dados no RDS.

### [DynamoDB](ca://s?q=Explicar_AWS_DynamoDB)
- Armazena atendimentos em tempo real.
- Permite consultas rápidas por clínica e mês.

### [RDS](ca://s?q=Explicar_AWS_RDS)
- Consolida relatórios mensais.
- Estrutura relacional para análises financeiras.

### [Step Functions](ca://s?q=Explicar_AWS_Step_Functions)
- Orquestra o fluxo completo:
  - Processar evento → Validar pro-bono → Atualizar relatório.

### [CloudWatch](ca://s?q=Explicar_AWS_CloudWatch)
- Monitora métricas de atendimentos, pro-bono e receita.
- Dispara alertas via SNS.

### [CodePipeline](ca://s?q=Explicar_AWS_CodePipeline)
- Automatiza CI/CD:
  - Source → Build → Test → Deploy.

### [CodeDeploy](ca://s?q=Explicar_AWS_CodeDeploy)
- Realiza deploy Blue/Green das Lambdas.
- Rollback automático em caso de falha.

---

## 📊 Fluxo ASCII da Arquitetura

```plaintext
API → SNS → Lambda process_event → DynamoDB
       ↓
Step Functions → Lambda validar_probono → SNS Alerts
       ↓
Step Functions → Lambda atualizar_relatorio → RDS
       ↓
CloudWatch Dashboard → Sr. Roberto acompanha métricas
       ↓
CodePipeline + CodeDeploy → CI/CD automatizado
