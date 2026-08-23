# Documentação de Testes — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Garantir que o pipeline DevOps seja confiável e que cada componente funcione corretamente:
- Testes unitários → validam funções isoladas.
- Testes de integração → validam comunicação entre serviços.
- Testes de ponta a ponta (E2E) → simulam o fluxo completo.

---

## 🧪 Tipos de Testes

### [Unitários](ca://s?q=Explicar_testes_unitarios)
- Local: `devops-clinicas/tests/unit/`
- Exemplo: `test_sns_publish.py`
- Valida chamadas isoladas (ex.: publicação no SNS).
- Usa mocks para simular serviços AWS.

### [Integração](ca://s?q=Explicar_testes_de_integracao)
- Local: `devops-clinicas/tests/integration/`
- Exemplo: `test_lambda_flow.py`
- Simula fluxo parcial (SNS → Lambda → DynamoDB).
- Garante que os componentes conversam corretamente.

### [Ponta a Ponta (E2E)](ca://s?q=Explicar_testes_e2e)
- Local: `devops-clinicas/tests/e2e/`
- Exemplo: `test_full_pipeline.py`
- Simula ciclo completo:
  - SNS → Lambdas → DynamoDB → RDS → SNS Alerts.
- Valida integração total do pipeline.

---

## 📊 Fluxo ASCII dos Testes

```plaintext
Unit → Funções isoladas (SNSService, DynamoDBService)
       ↓
Integration → Fluxos parciais (SNS → Lambda → DynamoDB)
       ↓
E2E → Pipeline completo (SNS → Lambdas → DynamoDB → RDS → CloudWatch)
