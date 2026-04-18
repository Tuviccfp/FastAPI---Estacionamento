# 🚗 Sistema de Cadastro de Clientes — Estacionamento

> Mini sistema de gerenciamento de clientes de estacionamento com menu interativo via terminal, construído em Python com SQLite3.

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Arquitetura](#arquitetura)
- [Decisões Técnicas](#decisões-técnicas)
- [Funcionalidades](#funcionalidades)
- [Como Executar](#como-executar)
- [Banco de Dados](#banco-de-dados)

---

## Sobre o Projeto

Sistema CRUD para cadastro e gerenciamento de clientes de um estacionamento. A interação acontece inteiramente via terminal, com um menu interativo onde o usuário navega digitando opções numéricas e fornecendo os dados pelo `input`.

O foco do projeto é aplicar boas práticas de arquitetura de software em Python, seguindo os mesmos princípios utilizados em projetos TypeScript/Node.js modernos.

---

## Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.x | Linguagem principal |
| SQLite3 | built-in | Banco de dados local |

Sem dependências externas — o projeto roda com a biblioteca padrão do Python.

---

## Estrutura do Projeto

```
📦 estacionamento/
├── 📂 controller/
│   └── controller.py        # Ponto de entrada das ações do usuário
├── 📂 database/
│   ├── 📂 models/
│   │   └── cliente.py       # Definição/criação da tabela
│   ├── connection.py        # Gerenciamento da conexão com o SQLite
│   └── database.sqlite      # Arquivo do banco de dados
├── 📂 repository/
│   └── cliente_repository.py  # Acesso direto ao banco de dados
├── 📂 service/
│   └── cliente_service.py   # Regras de negócio
└── main.py                  # Menu interativo e inicialização
```

---

## Arquitetura

O projeto aplica o padrão **Layered Architecture** (Arquitetura em Camadas) combinado com o **Repository Pattern**, o mesmo modelo utilizado em projetos NestJS/TypeScript — porém implementado em Python puro.

```
[ Terminal / main.py ]
        │
        ▼
[ Controller ]      ← recebe o input do usuário e orquestra a resposta
        │
        ▼
[ Service Layer ]   ← contém as regras de negócio
        │
        ▼
[ Repository ]      ← único responsável por falar com o banco de dados
        │
        ▼
[ SQLite3 / database.sqlite ]
```

### Injeção de Dependência

A conexão com o banco é criada no `controller` e **injetada** nas camadas inferiores, em vez de cada camada instanciar sua própria conexão. Isso mantém o controle do ciclo de vida da conexão em um único lugar e facilita substituições futuras (ex: trocar SQLite por PostgreSQL).

```python
conn = connect_db()

clienteRepo = ClienteRepository(conn)   # conn injetada no repositório
clienteService = ClienteService(clienteRepo)  # repositório injetado no serviço
```

Essa abordagem garante **baixo acoplamento** entre as camadas e facilita testes unitários, pois qualquer camada pode receber um mock no lugar da dependência real.

---

## Decisões Técnicas

### 🔑 Conversão de Tupla para Dicionário no Repository

O método `fetchone()` do SQLite3 retorna uma **tupla** por padrão — ou seja, os dados são acessados por índice: `cliente[0]`, `cliente[1]`, etc.

Isso cria um problema de **acoplamento implícito**: qualquer reordenação das colunas na tabela, ou adição de uma nova coluna no meio, quebra silenciosamente todo código que depende da posição dos valores.

A solução adotada foi converter o resultado para um **dicionário** diretamente dentro do `ClienteRepository`, antes de retornar os dados para as camadas superiores:

```python
# Antes (frágil — depende da ordem das colunas)
cliente = cursor.fetchone()
print(cliente[1])  # Qual campo é esse? Depende da ordem da query.

# Depois (robusto — acesso por nome semântico)
cliente = dict(zip([col[0] for col in cursor.description], cursor.fetchone()))
print(cliente["nome"])  # Explícito, legível e resistente a mudanças de schema.
```

**Por que isso importa?**

| Situação | Acesso por índice | Acesso por chave |
|---|---|---|
| Coluna nova adicionada no meio | 💥 Quebra | ✅ Transparente |
| Ordem de colunas alterada | 💥 Quebra | ✅ Transparente |
| Código legível | ❌ `cliente[2]` | ✅ `cliente["email"]` |
| Mudança de schema isolada | ❌ Propaga para todas camadas | ✅ Muda só no Repository |

Dessa forma, o **contrato entre Repository e Service** é sempre um dicionário com chaves nomeadas, e qualquer mudança no schema da tabela exige alteração **somente dentro do Repository** — as camadas superiores permanecem intocadas.

---

## Funcionalidades

| Opção | Descrição |
|---|---|
| `1` | Cadastrar novo cliente (nome, email, placa) |
| `2` | Listar todos os clientes |
| `3` | Buscar cliente por ID |
| `4` | Atualizar dados de um cliente |
| `5` | Deletar cliente por ID |

---

## Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
# Clone o repositório
git clone <url-do-repositório>
cd estacionamento

# Execute o sistema
python main.py
```

O banco de dados `database.sqlite` é criado automaticamente na primeira execução — nenhuma configuração adicional é necessária.

---

## Banco de Dados

O sistema utiliza uma única tabela, sem relacionamentos:

```sql
CREATE TABLE IF NOT EXISTS cliente (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        VARCHAR(100),
    email       VARCHAR(100),
    placa_carro VARCHAR(20)
);
```

O arquivo `.sqlite` é gerado localmente e pode ser inspecionado com ferramentas como [DB Browser for SQLite](https://sqlitebrowser.org/).

Feito com Python 🐍 e boas práticas de arquitetura.
---
