"""
Mini Help Desk
Sistema simples de linha de comando para abertura e acompanhamento de
chamados de suporte, usando um banco de dados SQLite local.

Uso:
    python helpdesk.py
"""
import sqlite3
from datetime import datetime

DB = "chamados.db"


def conectar():
    conn = sqlite3.connect(DB)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            solicitante TEXT NOT NULL,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'Aberto',
            data_abertura TEXT,
            data_fechamento TEXT
        )
        """
    )
    return conn


def abrir_chamado(conn):
    solicitante = input("Nome do solicitante: ")
    titulo = input("Título do chamado: ")
    descricao = input("Descrição do problema: ")
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    conn.execute(
        "INSERT INTO chamados (solicitante, titulo, descricao, status, data_abertura) "
        "VALUES (?, ?, ?, 'Aberto', ?)",
        (solicitante, titulo, descricao, agora),
    )
    conn.commit()
    print("✅ Chamado aberto com sucesso!\n")


def listar_chamados(conn, apenas_abertos=False):
    query = "SELECT id, solicitante, titulo, status, data_abertura FROM chamados"
    if apenas_abertos:
        query += " WHERE status = 'Aberto'"
    query += " ORDER BY id DESC"
    chamados = conn.execute(query).fetchall()

    if not chamados:
        print("Nenhum chamado encontrado.\n")
        return

    print(f"\n{'ID':<4}{'Solicitante':<20}{'Título':<25}{'Status':<12}{'Abertura'}")
    print("-" * 80)
    for c in chamados:
        print(f"{c[0]:<4}{c[1]:<20}{c[2]:<25}{c[3]:<12}{c[4]}")
    print()


def fechar_chamado(conn):
    id_chamado = input("ID do chamado a fechar: ")
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor = conn.execute(
        "UPDATE chamados SET status = 'Fechado', data_fechamento = ? "
        "WHERE id = ? AND status = 'Aberto'",
        (agora, id_chamado),
    )
    conn.commit()
    if cursor.rowcount:
        print("✅ Chamado fechado com sucesso!\n")
    else:
        print("⚠ Chamado não encontrado ou já está fechado.\n")


def menu():
    conn = conectar()
    opcoes = {
        "1": ("Abrir novo chamado", lambda: abrir_chamado(conn)),
        "2": ("Listar todos os chamados", lambda: listar_chamados(conn)),
        "3": ("Listar apenas chamados abertos", lambda: listar_chamados(conn, True)),
        "4": ("Fechar chamado", lambda: fechar_chamado(conn)),
        "5": ("Sair", None),
    }

    while True:
        print("=== Mini Help Desk ===")
        for chave, (texto, _) in opcoes.items():
            print(f"{chave}. {texto}")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "5":
            print("Encerrando. Até logo!")
            break
        elif escolha in opcoes:
            opcoes[escolha][1]()
        else:
            print("Opção inválida.\n")

    conn.close()


if __name__ == "__main__":
    menu()
