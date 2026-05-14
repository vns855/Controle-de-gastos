# Gerenciador de Gastos

🌐 **Deploy:** https://vns855.github.io/Controle-de-gastos/

## Descricao do Problema Real

Muitas pessoas tem dificuldade em manter um registro fiel de suas financas diarias. Este projeto tem como objetivo oferecer uma solucao pratica para controle de despesas e receitas, facilitando a organizacao financeira pessoal.

---

## Publico-alvo

Pessoas que buscam uma solucao tecnologica para gerenciar suas financas pessoais de forma simples e eficiente.

---

## Funcionalidades

- Registro e categorizacao de despesas e receitas
- Validacao automatica de integridade de dados via scripts
- Automacao de testes e padronizacao de codigo com GitHub Actions
- Dashboard visual para acesso rapido e gerenciamento de informacoes

---

## Tecnologias Utilizadas

- **Python 3.11+**: Linguagem base para processamento de dados
- **Pytest**: Framework para execucao de testes automatizados
- **Ruff**: Ferramenta de linting para garantir qualidade do codigo
- **GitHub Actions**: Automacao de workflow e integracao continua (CI)

---

## Instrucoes de Instalacao e Execucao

### 1. Clone este repositorio

```bash
git clone https://github.com/vns855/Controle-de-gastos.git
```

### 2. Acesse a pasta do projeto

```bash
cd controle-gastos-cli
```

### 3. Instale as dependencias

```bash
uv sync --dev
```

### 4. Execute a aplicacao

```bash
uv run python src/app.py
```

---

## Como rodar os testes

```bash
uv run pytest
```

---

## Como rodar o lint

```bash
uv run ruff check .
```

---

## Versao e Autor

- **Versao:** 1.0.0
- **Autor:** Vinicius Jorge
- **Repositorio:** https://github.com/vns855/Controle-de-gastos