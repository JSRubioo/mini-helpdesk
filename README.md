# 🎫 Mini Help Desk

Sistema simples de linha de comando (CLI) para abrir, listar e fechar
chamados de suporte técnico, usando um banco de dados SQLite local.

## Por que esse projeto?

Simula, de forma simplificada, o fluxo de um sistema de tickets de
suporte: registro de solicitante, descrição do problema, status
(Aberto/Fechado) e datas de abertura/fechamento. É o mesmo tipo de
lógica que sistemas como Zendesk, Movidesk ou GLPI usam por trás —
aqui construído do zero para praticar banco de dados e lógica de CRUD.

## Tecnologias

- Python 3
- SQLite3 (biblioteca padrão do Python, sem necessidade de instalação)

## Como rodar

```bash
python helpdesk.py
```

O banco de dados `chamados.db` é criado automaticamente na primeira
execução, na mesma pasta do script.

## Funcionalidades

- Abrir novo chamado (solicitante, título, descrição)
- Listar todos os chamados
- Listar apenas chamados em aberto
- Fechar um chamado pelo ID

## Próximos passos (ideias de evolução)

- Adicionar campo de prioridade (baixa/média/alta) e SLA
- Migrar para uma interface web simples (Flask)
- Gerar relatório de tempo médio de atendimento
