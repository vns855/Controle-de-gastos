import json
from pathlib import Path

import pytest

from src.app import (
    adicionar_gasto,
    calcular_total,
    listar_gastos,
    remover_gasto,
    salvar_gastos,
)


@pytest.fixture(autouse=True)
def limpar_arquivo():
    Path("data").mkdir(exist_ok=True)
    with open("data/gastos.json", "w", encoding="utf-8") as file:
        json.dump([], file)
    yield
    with open("data/gastos.json", "w", encoding="utf-8") as file:
        json.dump([], file)

def test_adicionar_gasto_com_sucesso():
    mensagem = adicionar_gasto("Almoço", 25.0)
    gastos = listar_gastos()
    assert mensagem == "Gasto adicionado com sucesso."
    assert len(gastos) == 1
    assert gastos[0]["descricao"] == "Almoço"
    assert gastos[0]["valor"] == 25.0

def test_adicionar_gasto_com_valor_invalido():
    with pytest.raises(ValueError, match="O valor deve ser maior que zero."):
        adicionar_gasto("Ônibus", -5.0)

def test_calcular_total():
    salvar_gastos([
        {"id": 1, "descricao": "Lanche", "valor": 10.0},
        {"id": 2, "descricao": "Transporte", "valor": 15.5},
    ])
    total = calcular_total()
    assert total == 25.5

def test_remover_gasto_existente():
    salvar_gastos([
        {"id": 1, "descricao": "Lanche", "valor": 10.0},
        {"id": 2, "descricao": "Transporte", "valor": 15.0},
    ])
    mensagem = remover_gasto(1)
    gastos = listar_gastos()
    assert mensagem == "Gasto removido com sucesso."
    assert len(gastos) == 1
    assert gastos[0]["descricao"] == "Transporte"

def test_remover_gasto_inexistente():
    with pytest.raises(ValueError, match="Gasto não encontrado."):
        remover_gasto(999)
