# Documentação de Onboarding — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Facilitar a integração de novos membros da equipe ao projeto DevOps, garantindo:
- Rapidez na adaptação.
- Clareza sobre responsabilidades.
- Acesso às ferramentas e processos corretos.

---

## 🏗️ Etapas de Onboarding

### [Acesso Inicial](ca://s?q=Onboarding_Acesso_Inicial)
- Criação de conta AWS com permissões específicas via IAM.
- Inclusão no repositório CodeCommit.
- Configuração de credenciais locais (AWS CLI, Git).

### [Treinamento Básico](ca://s?q=Onboarding_Treinamento_Basico)
- Revisão dos módulos em `devops-clinicas/docs/treinamento.md`.
- Introdução ao pipeline CI/CD.
- Uso de CloudWatch para monitoramento.

### [Ferramentas de Trabalho](ca://s?q=Onboarding_Ferramentas_de_Trabalho)
- IDE padrão: VSCode com extensões Python e AWS.
- Acesso ao Slack/Teams para comunicação.
- Integração com Jira/Trello para gestão de tarefas.

### [Responsabilidades](ca://s?q=Onboarding_Responsabilidades)
- DevOps: manter infraestrutura e pipeline.
- Backend: desenvolver e manter Lambdas.
- Data: cuidar de relatórios no RDS.
- Segurança: revisar IAM e conformidade LGPD.

### [Primeira Tarefa](ca://s?q=Onboarding_Primeira_Tarefa)
- Configurar ambiente local.
- Executar testes unitários (`devops-clinicas/tests/unit/`).
- Submeter primeiro Pull Request para revisão.

---

## 📊 Fluxo ASCII do Onboarding

```plaintext
Acesso inicial → Treinamento básico
       ↓
Ferramentas configuradas → Responsabilidades definidas
       ↓
Primeira tarefa → Pull Request revisado
       ↓
Integração completa na equipe
