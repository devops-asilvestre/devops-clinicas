# Documentação CI/CD — Rede de Clínicas Odontológicas

## 🎯 Objetivo
Automatizar todo o ciclo de desenvolvimento e entrega:
- Build e empacotamento das Lambdas.
- Execução dos testes (unit, integration, e2e).
- Deploy seguro em produção com rollback automático.

---

## 🏗️ Componentes

### [CodeCommit](ca://s?q=Explicar_AWS_CodeCommit)
- Repositório Git centralizado.
- Branch principal: `main`.

### [CodePipeline](ca://s?q=Explicar_AWS_CodePipeline)
- Orquestra o fluxo CI/CD.
- Estágios:
  - **Source** → captura código do CodeCommit.
  - **Build** → compila e empacota Lambdas.
  - **Test** → executa testes automatizados.
  - **Deploy** → publica em produção.

### [CodeBuild](ca://s?q=Explicar_AWS_CodeBuild)
- Responsável por compilar e rodar testes.
- Projetos:
  - `ClinicasLambdaBuild` → build das funções.
  - `ClinicasTests` → execução dos testes unitários, integração e e2e.

### [CodeDeploy](ca://s?q=Explicar_AWS_CodeDeploy)
- Gerencia deploy das Lambdas.
- Estratégia: **Blue/Green** com rollback automático.
- Deployment Group: `ClinicasLambdaDG`.

---

## 📊 Fluxo ASCII do CI/CD

```plaintext
CodeCommit (push na branch main)
       ↓
CodePipeline
   ├── Source → captura código
   ├── Build → CodeBuild compila Lambdas
   ├── Test → CodeBuild executa testes
   └── Deploy → CodeDeploy publica Lambdas
       ↓
Produção atualizada com segurança
