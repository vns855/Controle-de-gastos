import json
from pathlib import Path

import requests

DATA_FILE = Path("data/gastos.json")
VERSION = "1.0.0"

def inicializar_arquivo() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        salvar_gastos([])

def carregar_gastos() -> list:
    inicializar_arquivo()
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def salvar_gastos(gastos: list) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(gastos, file, indent=4, ensure_ascii=False)

def adicionar_gasto(descricao: str, valor: float) -> str:
    if not descricao.strip():
        raise ValueError("A descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    gastos = carregar_gastos()
    novo_gasto = {"id": len(gastos) + 1, "descricao": descricao, "valor": valor}
    gastos.append(novo_gasto)
    salvar_gastos(gastos)
    return "Gasto adicionado com sucesso."

def listar_gastos() -> list:
    return carregar_gastos()

def remover_gasto(gasto_id: int) -> str:
    gastos = carregar_gastos()
    novos_gastos = [g for g in gastos if g["id"] != gasto_id]
    if len(novos_gastos) == len(gastos):
        raise ValueError("Gasto não encontrado.")
    for i, gasto in enumerate(novos_gastos, start=1):
        gasto["id"] = i
    salvar_gastos(novos_gastos)
    return "Gasto removido com sucesso."

def calcular_total() -> float:
    gastos = carregar_gastos()
    return sum(g["valor"] for g in gastos)

def buscar_cotacao_dolar() -> str:
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()
        valor = float(dados["USDBRL"]["bid"])
        return f"Cotacao do dolar: R$ {valor:.2f}"
    except Exception:
        return "Cotacao do dolar: indisponivel no momento."

def exibir_menu() -> None:
    print("\n=== Controle de Gastos Pessoais ===")
    print(buscar_cotacao_dolar())
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Remover gasto")
    print("4. Mostrar total")
    print("5. Mostrar versão")
    print("0. Sair")

def main() -> None:
    inicializar_arquivo()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        try:
            if opcao == "1":
                descricao = input("Descrição do gasto: ").strip()
                valor = float(input("Valor do gasto: "))
                print(adicionar_gasto(descricao, valor))
            elif opcao == "2":
                gastos = listar_gastos()
                if not gastos:
                    print("Nenhum gasto cadastrado.")
                else:
                    print("\n--- Lista de Gastos ---")
                    for gasto in gastos:
                        desc = gasto["descricao"]
                        val = gasto["valor"]
                        print(f'ID: {gasto["id"]} | {desc} | R$ {val:.2f}')
            elif opcao == "3":
                gasto_id = int(input("Digite o ID do gasto a remover: "))
                print(remover_gasto(gasto_id))
            elif opcao == "4":
                total = calcular_total()
                print(f"Total de gastos: R$ {total:.2f}")
            elif opcao == "5":
                print(f"Versão atual: {VERSION}")
            elif opcao == "0":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError as error:
            print(f"Erro: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")

if __name__ == "__main__":
    main()
