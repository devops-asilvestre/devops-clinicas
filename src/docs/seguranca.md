# Documentação de Segurança — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Proteger dados sensíveis de pacientes e clínicas, garantindo:
- Confidencialidade
- Integridade
- Disponibilidade
- Conformidade com LGPD

---

## 🏗️ Práticas de Segurança

### [IAM Roles](ca://s?q=Explicar_AWS_IAM_Roles)
- Cada Lambda possui role dedicada com permissões mínimas (principle of least privilege).
- Step Functions acessa apenas Lambdas autorizadas.
- CodePipeline e CodeDeploy usam roles específicas para CI/CD.

### [Criptografia](ca://s?q=Explicar_AWS_Criptografia)
- DynamoDB e RDS com **KMS** habilitado.
- Dados em trânsito protegidos com TLS 1.2+.
- Senhas e secrets armazenados no **AWS Secrets Manager**.

### [Auditoria](ca://s?q=Explicar_AWS_CloudTrail)
- CloudTrail habilitado para rastrear todas as chamadas de API.
- Logs enviados para bucket S3 com retenção de 1 ano.
- Integração com CloudWatch Logs para alertas de acessos suspeitos.

### [Segurança de Rede](ca://s?q=Explicar_AWS_VPC)
- RDS isolado em sub-rede privada.
- Lambdas acessam RDS via VPC.
- Security Groups restritos por IP e porta.

### [Conformidade LGPD](ca://s?q=Explicar_LGPD)
- Dados de pacientes anonimizados em relatórios.
- Consentimento registrado para atendimentos.
- Logs de acesso a dados pessoais mantidos para auditoria.

---

## 📊 Fluxo ASCII da Segurança

```plaintext
IAM Roles → Controle de acesso mínimo
       ↓
KMS → Criptografia em repouso
       ↓
TLS → Criptografia em trânsito
       ↓
CloudTrail → Auditoria e rastreabilidade
       ↓
VPC → Isolamento de rede
       ↓
LGPD → Conformidade legal
