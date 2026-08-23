# Documentação de Escalabilidade — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Garantir que a arquitetura suporte o crescimento da rede de clínicas e o aumento no volume de atendimentos, mantendo:
- Performance
- Confiabilidade
- Custos otimizados

---

## 🏗️ Estratégias de Escalabilidade

### [Escalabilidade Horizontal](ca://s?q=Escalabilidade_horizontal)
- DynamoDB com **Auto Scaling** para throughput.
- Lambdas com **Concurrency Scaling** automático.
- SNS e SQS para desacoplamento de eventos.

### [Escalabilidade Vertical](ca://s?q=Escalabilidade_vertical)
- RDS com aumento de instância (db.m5.large → db.m5.xlarge).
- Ajuste de memória e CPU conforme demanda.
- Storage elástico para relatórios históricos.

### [Desacoplamento](ca://s?q=Desacoplamento_de_servicos)
- Uso de SNS + SQS para filas assíncronas.
- Step Functions para orquestração modular.
- Redução de dependências diretas entre serviços.

### [Caching](ca://s?q=Caching_em_arquitetura)
- CloudFront para distribuição de relatórios.
- DynamoDB DAX para consultas rápidas.
- Cache em memória para métricas acessadas com frequência.

### [Custos Otimizados](ca://s?q=Otimizacao_de_custos_AWS)
- Monitoramento de uso com CloudWatch.
- Reserved Instances para RDS.
- DynamoDB On-Demand para clínicas menores.

---

## 📊 Fluxo ASCII da Escalabilidade

```plaintext
Mais clínicas → Mais atendimentos
       ↓
Auto Scaling (DynamoDB + Lambda)
       ↓
Desacoplamento (SNS + SQS + Step Functions)
       ↓
RDS vertical scaling + caching
       ↓
Custos otimizados com monitoramento
