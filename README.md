# FinGestAPI

API REST para gestão financeira pessoal, construída com FastAPI e arquitetura limpa.

## 📋 Descrição

FinGestAPI é uma API RESTful moderna para gerenciamento de finanças pessoais. O projeto segue os princípios da arquitetura limpa (Clean Architecture), separando claramente as responsabilidades em camadas de API, serviços, repositórios e modelos de banco de dados.

### Funcionalidades Principais

- **Gestão de Transações**: Controle de receitas e despesas
- **Categorização**: Organização de transações por categorias
- **Relatórios**: Geração de relatórios financeiros
- **Autenticação**: Sistema seguro com JWT e hash de senhas
- **Tarefas Assíncronas**: Processamento em background com Celery
- **Cache**: Otimização com Redis
- **Monitoramento**: Integração com Sentry para rastreamento de erros

## 🛠️ Tecnologias

| Categoria | Tecnologia |
|-----------|------------|
| **Framework** | FastAPI 0.136+ |
| **Validação** | Pydantic 2.13+ |
| **Banco de Dados** | PostgreSQL + SQLAlchemy 2.0 |
| **Migrações** | Alembic |
| **Autenticação** | JWT (PyJWT) + Passlib |
| **Filas/Tarefas** | Celery |
| **Cache** | Redis |
| **Logging** | Structlog |
| **Monitoramento** | Sentry SDK |
| **Notificações** | FCM (Firebase Cloud Messaging) |
| **Servidor** | Uvicorn |

## 📦 Pré-requisitos

- Python 3.12+
- PostgreSQL 14+
- Redis 6+
- Poetry (gerenciador de dependências)

## 🔧 Instalação

### 1. Clone o repositório

```bash
cd /media/jvvsricci/10625AD5625ABEE2/Repositorio/Python/FinGestAPI
```

### 2. Instale as dependências

```bash
poetry install
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Banco de Dados
DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/fingestapi

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Sentry (Opcional)
SENTRY_DSN=

# Servidor
HOST=127.0.0.1
PORT=8000
```

### 4. Execute as migrações do banco de dados

```bash
poetry run alembic upgrade head
```

## 🚀 Como Executar

### Modo Desenvolvimento

```bash
poetry run dev
```

O servidor estará disponível em: `http://127.0.0.1:8000`

### Documentação da API

A documentação interativa está disponível em:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Verificar Saúde da API

```bash
curl http://127.0.0.1:8000/health-check
```

Resposta esperada:
```json
{"status": "OK"}
```

## 📁 Estrutura do Projeto

```
FinGestAPI/
├── src/
│   ├── api/              # Camada de API (routes, endpoints)
│   │   └── v1/
│   │       └── routes/   # Rotas da API v1
│   ├── core/             # Configurações centrais
│   ├── db/               # Configurações do banco de dados
│   ├── models/           # Modelos SQLAlchemy
│   ├── repositories/     # Padrão Repository
│   ├── schemas/          # Schemas Pydantic (DTOs)
│   ├── services/        # Lógica de negócio
│   └── main.py           # Ponto de entrada
├── tests/
│   ├── e2e/              # Testes end-to-end
│   ├── integration/      # Testes de integração
│   └── unit/             # Testes unitários
├── pyproject.toml        # Configurações Poetry
├── run.py                # Script de execução
└── README.md             # Este arquivo
```

## 🧪 Testes

### Executar todos os testes

```bash
poetry run pytest
```

### Executar com coverage

```bash
poetry run pytest --cov=src
```

### Executar testes específicos

```bash
poetry run pytest tests/unit/
poetry run pytest tests/integration/
poetry run pytest tests/e2e/
```

## 🔨 Comandos Úteis

| Comando | Descrição |
|---------|-----------|
| `poetry run dev` | Iniciar servidor em modo desenvolvimento |
| `poetry run pytest` | Executar testes |
| `poetry run alembic upgrade head` | Aplicar migrações |
| `poetry run alembic revision --autogenerate -m "mensagem"` | Criar nova migração |
| `poetry run ruff check src/` | Verificar código com Ruff |
| `poetry run mypy src/` | Verificar tipos com MyPy |

## 📝 Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `DATABASE_URL` | URL de conexão do PostgreSQL | `postgresql+asyncpg://localhost:5432/fingestapi` |
| `REDIS_URL` | URL de conexão do Redis | `redis://localhost:6379/0` |
| `SECRET_KEY` | Chave secreta para JWT | (obrigatório) |
| `ALGORITHM` | Algoritmo de assinatura JWT | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tempo de expiração do token | `30` |
| `SENTRY_DSN` | DSN do Sentry para monitoramento | (opcional) |

## 📄 Licença

MIT License - sinta-se livre para usar e modificar este projeto.

---

Desenvolvido com FastAPI ⚡