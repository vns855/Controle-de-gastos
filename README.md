# Gerenciador de Gastos

🌐 **Deploy:** https://vns855.github.io/Controle-de-gastos/

## Descricao do Problema Real

Muitas pessoas tem dificuldade em manter um registro fiel de suas financas diarias. Este projeto tem como objetivo oferecer uma solucao pratica para controle de despesas e receitas, facilitando a organizacao financeira pessoal.

---

## Publico-alvo

Pessoas que buscam uma solucao tecnologica para gerenciar suas financas pessoais de forma simples e eficiente.

---

## Funcionalidades

- Adicionar, listar, remover e calcular gastos pessoais
- Exibicao da cotacao do dolar em tempo real via API
- Testes automatizados com pytest
- Linting com ruff
- CI com GitHub Actions

---

## Tecnologias Utilizadas

- **Python 3.11+**: Linguagem base para processamento de dados
- **Requests**: Consumo da API publica de cotacao do dolar (AwesomeAPI)
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
cd Controle-de-gastos
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

## Evidencia de Funcionamento

```
=== Controle de Gastos Pessoais ===
Cotacao do dolar: R$ 5.25
1. Adicionar gasto
2. Listar gastos
3. Remover gasto
4. Mostrar total
5. Mostrar versao
0. Sair
Escolha uma opcao: 1
Descricao do gasto: Supermercado
Valor do gasto: 100
Gasto adicionado com sucesso.
```