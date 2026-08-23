# Documentação de Monitoramento — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Garantir visibilidade em tempo real sobre:
- Total de atendimentos por clínica.
- Cumprimento da meta de 10 atendimentos pro-bono/mês.
- Receita mensal consolidada.
- Alertas automáticos para o Sr. Roberto.

---

## 🏗️ Componentes

### [CloudWatch Metrics](ca://s?q=Explicar_CloudWatch_Metrics)
- Coleta métricas de Lambdas e DynamoDB.
- Métricas principais:
  - `TotalAtendimentos`
  - `ProBonoAtendimentos`
  - `ReceitaMensal`

### [CloudWatch Dashboard](ca://s?q=Explicar_CloudWatch_Dashboard)
- Arquivo: `devops-clinicas/monitoring/cloudwatch_dashboard.json`
- Widgets:
  - Série temporal de atendimentos por clínica.
  - Série temporal de atendimentos pro-bono.
  - Receita mensal consolidada.

### [CloudWatch Alarms](ca://s?q=Explicar_CloudWatch_Alarms)
- Arquivo: `devops-clinicas/monitoring/sns_alerts_config.json`
- Regras:
  - Alerta se clínica não atingir 10 atendimentos pro-bono.
  - Alerta se receita cair mais de 30% em relação ao mês anterior.

### [SNS Alerts](ca://s?q=Explicar_SNS_Alerts)
- Notificações enviadas para o Sr. Roberto.
- Canal configurado: email e SMS.
- Tópico: `ClinicasAlerts`.

---

## 📊 Fluxo ASCII do Monitoramento

```plaintext
Lambda → CloudWatch Metrics
       ↓
CloudWatch Dashboard → Sr. Roberto acompanha métricas
       ↓
CloudWatch Alarms → SNS Alerts
       ↓
Sr. Roberto recebe notificação automática
