# Guia de Execução — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Registrar o passo a passo para colocar toda a arquitetura DevOps em funcionamento, garantindo que qualquer membro da equipe consiga replicar o processo.

---

## 🏗️ Etapas de Execução

### 1. Provisionar Infraestrutura
- Utilizar o arquivo `infra/cloudformation_template.yaml`.
- Executar o comando:

  ```
  aws cloudformation create-stack --stack-name ClinicasStack --template-body file://infra/cloudformation_template.yaml --capabilities CAPABILITY_IAM
  ```

- Isso cria SNS, DynamoDB, RDS, Lambdas e Step Functions.

---

### 2. Inicializar Dados
- Rodar o script `infra/init_script.py` para popular DynamoDB e RDS.
- Comando:

  ```
  python infra/init_script.py
  ```

- Resultado esperado:
  - DynamoDB com atendimentos iniciais.
  - RDS com relatórios mensais básicos.

---

### 3. Validar CI/CD
- Fazer um commit de teste no CodeCommit.
- Pipeline CodePipeline deve:
  - Executar testes unitários.
  - Fazer build com CodeBuild.
  - Deploy Blue/Green com CodeDeploy.

---

### 4. Executar Testes de Performance
- Rodar `tests/performance_test.py` para simular carga.
- Comando:
  
  ```
  python tests/performance_test.py
  ```

- Métricas esperadas:
  - Throughput médio (eventos/segundo).
  - Tempo total de execução.

---

### 5. Ativar Monitoramento
- Conferir dashboards no CloudWatch.
- Validar alertas via SNS.
- Garantir que logs de Lambdas e RDS estão sendo armazenados.

---

### 6. Suporte e Operações
- Seguir documentação em `docs/suporte.md` e `docs/operacoes.md`.
- Escalonar incidentes conforme níveis N1, N2 e N3.
- Manter Sr. Roberto informado via relatórios.

---

## 📊 Fluxo ASCII da Execução

```plaintext
CloudFormation → Infra provisionada
       ↓
Init Script → Dados iniciais
       ↓
CI/CD → Build + Deploy
       ↓
Performance Test → Validar escalabilidade
       ↓
Monitoramento → CloudWatch + SNS
       ↓
Suporte → Operações e incidentes
```

---

## 📌 Conclusão
Com `devops-clinicas/docs/executar_sistema.md`, temos um **guia prático e consolidado** para colocar toda a arquitetura em funcionamento, desde a infraestrutura até monitoramento e suporte.  

---
