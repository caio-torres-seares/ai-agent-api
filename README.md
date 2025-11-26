# DreamSquad Challenge API 🚀

<div align="start">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.121.0+-009688?logo=fastapi&logoColor=white)
![Strands Agents](https://img.shields.io/badge/Strands_Agents-1.18.0+-6f42c1)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-green?logo=ollama)
![Docker](https://img.shields.io/badge/Dockerfile-Ready-blue?logo=docker)


Este projeto integra **FastAPI** com o **Strands Agents SDK** e **Ollama** para criar um assistente capaz de executar ferramentas matemáticas e conversação natural, seguindo rigorosos padrões de engenharia de software.

**Destaques Técnicos:**
* 🏗️ **Arquitetura Modular:** Separação clara entre Rotas, Services, Schemas e Agentes.
* 🛡️ **Segurança:** Validação contra *Prompt Injection*.
* 🚦 **Rate Limiting:** Rate Limiting com SlowAPI (1 req/seg).
* 🐳 **Dockerizado:** Pronto para deploy.
* 🧪 **Testes Completos** - Validação dos módulos
* 🎭 **Easter Egg** - Descubra nos testes!

---

• [Quick Start](#-quick-start) • [API Docs](docs/API.md)

</div>

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Documentação](#-documentação)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias](#tecnologias)
- [Quick Start](#-quick-start)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Execução Local](#execução-local)
  - [Execução com Docker](#execução-com-docker)
- [Testes](#-testes)
- [Troubleshooting](#troubleshooting-rápido)

---

## 🎯 Visão Geral

API REST que integra um agente de IA configurável com capacidades de tomada de decisão autônoma:

- ✅ **Processa requisições** via endpoints REST
- ✅ **LLM local** com Ollama 
- ✅ **Executa ferramentas** (calculadora matemática)
- ✅ **Validação de segurança** contra prompt injection
- ✅ **Rate limiting** para proteção
- ✅ **Contexto conversacional** mantido

---

## 📚 Documentação

| Documento | Descrição |
|-----------|-----------|
| **[API.md](docs/API.md)** | Referência completa da API |

### Documentação Interativa (Recomendado)

Com a aplicação rodando, acesse:

- **Swagger UI:** http://localhost:8000/docs

---

## 📂 Estrutura do Projeto
```
dreamsquad_challenge/
├── app/
│   ├── main.py              # 🚀 Arquivo principal
│   ├── agents/              # 🤖 Agentes IA
│   ├── api/routers/         # 🌐 Endpoints REST
│   ├── core/                # ⚙️ Configurações
│   ├── models/              # 📋 Schemas Pydantic
│   ├── security/            # 🔒 Validações segurança
│   └── services/            # 💼 Lógica de negócio
├── docs/                    # 📚 Documentação detalhada
├── tests/                   # 🧪 Testes automatizados
├── .env.example            # Template de variáveis
├── Dockerfile              # Configuração Docker
└── README.md               # Este arquivo
```

**Arquitetura em Camadas:**
```
HTTP Request →   API Router →   Service →      Agent →     Ollama
                [validação]   [segurança]   [tools/LLM]
```

---


## 🛠️ Tecnologias

| Tecnologia | Versão | Propósito |
|---|---|---|
| **Python** | 3.11+ | Linguagem principal |
| **FastAPI** | ≥0.121.0 | Framework web |
| **Uvicorn** | ≥0.38.0 | Servidor |
| **Pydantic** | ≥2.12.0 | Validação de dados |
| **Strands Agents** | ≥1.18.0 | Orquestração de agentes IA |
| **Strands Tools** | ≥0.2.16 | Ferramentas para agentes |
| **Ollama** | Latest | LLM local |
| **SlowAPI** | ≥0.1.9 | Rate limiting |
| **python-dotenv** | ≥1.2.0 | Gerenciamento de variáveis de ambiente |
| **pytest** | ≥9.0.0 | Framework de testes |


---

## 🚀 Quick Start

### Pré-requisitos

- ✅ Python 3.11 ou superior
- ✅ pip (gerenciador de pacotes Python)
- ✅ Ollama instalado (veja [instalação do Ollama](#-instalação-do-ollama))

### Instalação
```bash
# 1. Clonar repositório
git clone https://github.com/caio-torres-seares/dreamsquad_challenge.git
cd dreamsquad_challenge

# 2. Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar variáveis de ambiente
cp .env.example .env
# Edite .env com suas configurações
```

### 🔧 Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
# Provider LLM 
LLM_PROVIDER=ollama

# Endereço do Ollama
OLLAMA_HOST=http://localhost:11434

# Modelo baixado via 'ollama pull'
LLM_MODEL_ID=llama3.1:8b

# Limite máximo de caracteres permitidos no prompt
MAX_PROMPT_LENGTH=2000
```




## 🦙 Configuração do Ollama
### 1. Verificar se Ollama está rodando
```bash
curl http://localhost:11434/api/tags
```

### 2. Baixar o modelo LLM

Recomendação: o modelo `llama3.1:8b` apresentou o melhor equilíbrio entre qualidade e desempenho durante os testes deste projeto.  

- Tamanho aproximado: **4.9 GB**
- Boa qualidade de respostas
- Capaz de lidar com ferramentas (calculator) com precisão

Para máquinas com menos RAM ou disco, uma alternativa mais leve é o `llama3.2`, com aproximadamente **2.0 GB**, mantendo um desempenho "ok" para consultas gerais.

```bash
ollama pull llama3.1:8b
```
### 3. Atualizar .env
```bash
echo "LLM_MODEL_ID=llama3.1:8b" >> .env
```

---

## 🖥️ Execução

### Opção 1: Execução Local (Desenvolvimento)

**⚠️ Atenção! Antes de tudo, garanta que o Ollama está rodando**
```bash
# 1. Roda o serviço ollama
ollama serve
```

```bash
# 2. Ativar ambiente virtual
.venv\Scripts\activate     # Windows

# ou

source .venv/bin/activate  # Linux/macOS


# 3. Executar aplicação
uvicorn app.main:app --reload --host 0.0.0.0
```

A API estará disponível em: **http://localhost:8000**

E a documentação estará disponível em: **http://localhost:8000/docs**

**Opções úteis:**
- `--reload`: Hot reload (apenas desenvolvimento)
- `--host 0.0.0.0`: Aceita conexões externas
- `--port 8000`: Permite mudar a porta padrão de execução (8000)


**Verificar status:**
```bash
curl http://localhost:8000/health
```

---

### Opção 2: Execução com Docker (Produção)

**⚠️ Atenção! Antes de tudo, garanta que o Ollama está rodando**
```bash
# 1. Roda o serviço ollama
ollama serve
```

```bash
# 2. Build da imagem
docker build -t dreamsquad-api:latest .

# 3. Executar container
docker run --name dreamsquad-chat -p 8000:8000 dreamsquad-api:latest

# 4. Verificar logs
docker logs -f dreamsquad-chat

# 5. Testar
curl http://localhost:8000/health
```


**Parar container:**
```bash
docker stop dreamsquad-api
```

**Remover container:**
```bash
docker rm dreamsquad-api
```

---

## 🧪 Testes

### Executar Testes
```bash
# Com output detalhado
pytest -vs
```

### Estrutura
```
tests/
├── conftest.py               # Fixtures compartilhadas
├── test_api.py               # Testes de endpoints
└── test_best_agent_answer.py # Testes do agente (+ easter egg!)
```

## 🎭 Easter Egg

Descubra o teste especial:
```bash
# Certifique-se que Ollama está rodando
ollama serve

# Execute com output
pytest -vs tests/test_best_agent_answer.py
```

> **Spoiler:** É um teste técnico válido que também deixa uma mensagem criativa! 😉

---


## 🔧 Troubleshooting Rápido

**Erro 500 ao chamar /chat?**

Certifique-se de ter o ollama rodando
```bash
ollama serve
curl http://localhost:11434/api/tags
```

**Ollama não conecta?**
```bash
ollama serve
curl http://localhost:11434/api/tags
```

**Modelo não encontrado?**
```bash
ollama list
ollama pull llama3.1:8b # ou outra versão de sua escolha
```

**Docker não acessa Ollama?**
- Use `http://host.docker.internal:11434` (Windows/macOS)
- Use `http://172.17.0.1:11434` (Linux)


---

## 📄 Licença

Desenvolvido como case técnico para **DreamSquad**.

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/caio-seares)



</div>