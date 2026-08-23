# Documentação de Governança — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Estabelecer processos claros de gestão, versionamento e auditoria para garantir:
- Transparência nas mudanças.
- Responsabilidade da equipe.
- Conformidade regulatória.
- Sustentabilidade do ciclo DevOps.

---

## 🏗️ Princípios de Governança

### [Versionamento](ca://s?q=Explicar_versionamento_de_codigo)
- Repositório central: CodeCommit.
- Branch principal: `main`.
- Branches secundárias para features e hotfixes.
- Pull Requests obrigatórios com revisão dupla.

### [Auditoria de Mudanças](ca://s?q=Explicar_auditoria_de_mudancas)
- CloudTrail registra todas as chamadas de API.
- Logs armazenados em S3 com retenção de 1 ano.
- Integração com CloudWatch para alertas de acessos suspeitos.

### [Responsabilidades da Equipe](ca://s?q=Explicar_responsabilidades_de_equipe)
- DevOps: mantém pipeline e infraestrutura.
- Backend: mantém Lambdas e APIs.
- Data: mantém relatórios e consultas no RDS.
- Segurança: garante conformidade LGPD e IAM.
- Gestão: acompanha métricas e relatórios via dashboards.

### [Processos de Deploy](ca://s?q=Explicar_processos_de_deploy)
- CI/CD automatizado com CodePipeline.
- Testes obrigatórios antes de cada deploy.
- Deploy Blue/Green com rollback automático.
- Aprovação manual para mudanças críticas.

### [Conformidade](ca://s?q=Explicar_conformidade_LGPD)
- Dados pessoais anonimizados em relatórios.
- Consentimento registrado para atendimentos.
- Logs de acesso auditados regularmente.

---

## 📊 Fluxo ASCII da Governança

```plaintext
CodeCommit → Pull Request → Revisão dupla
       ↓
CodePipeline → Build + Test
       ↓
CodeDeploy → Blue/Green Deploy
       ↓
CloudTrail + CloudWatch → Auditoria e alertas
       ↓
Gestão → Dashboards + Relatórios
