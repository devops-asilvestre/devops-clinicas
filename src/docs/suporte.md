# Documentação de Suporte — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Definir canais de comunicação, processos de abertura de chamados e SLA de atendimento para garantir:
- Resposta rápida a problemas.
- Clareza na comunicação.
- Transparência no acompanhamento de incidentes.

---

## 🏗️ Canais de Suporte

### [Email Suporte](ca://s?q=Suporte_por_email)
- Endereço: suporte@clinicas.devops
- Uso: abertura de chamados formais.
- SLA: resposta inicial em até 4h úteis.

### [Chat Interno](ca://s?q=Suporte_por_chat_interno)
- Plataforma: Slack/Teams.
- Uso: dúvidas rápidas e comunicação imediata.
- SLA: resposta em até 1h.

### [Telefone Emergencial](ca://s?q=Suporte_por_telefone)
- Número: +55 (11) 4000-1234
- Uso: incidentes críticos (Nível 3).
- SLA: atendimento imediato.

---

## 🚨 Processo de Abertura de Chamados

### [Classificação](ca://s?q=Classificacao_de_chamados)
- **Nível 1** → Problemas menores (ex.: falha em Lambda isolada).
- **Nível 2** → Falhas em múltiplos serviços (ex.: DynamoDB + RDS).
- **Nível 3** → Impacto crítico (ex.: indisponibilidade geral).

### [Registro](ca://s?q=Registro_de_chamados)
- Canal: email ou chat interno.
- Informações obrigatórias:
  - Clínica afetada.
  - Descrição do problema.
  - Logs ou prints relevantes.
  - Impacto percebido.

### [Acompanhamento](ca://s?q=Acompanhamento_de_chamados)
- Chamados registrados no Jira/Trello.
- Status: Aberto → Em andamento → Resolvido → Validado.
- Notificações automáticas para o solicitante.

---

## 📊 SLA de Atendimento

| Nível | Tempo de Resposta | Tempo de Resolução |
|-------|------------------|--------------------|
| **[Nível