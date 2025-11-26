# Documentação da API REST

Referência resumida dos endpoints da DreamSquad Challenge API.

[⬅ Voltar para a Documentação Geral](../README.md)

## Visão Geral

A API fornece acesso a um agente de IA que:

- Responde perguntas de conhecimento geral
- Executa cálculos matemáticos via tool `calculator`
- Mantém contexto conversacional
- Valida entradas contra prompt injection

**Formato:** JSON — **Versão:** 1.0.0 — **Protocol:** HTTP/1.1

## Base URL
`http://localhost:8000`

## Rate Limiting

1 requisição por segundo por IP.  
Headers padrão `X-RateLimit-*` indicam uso atual. Exceder o limite retorna `429` com `{"detail":"1 per 1 second"}`.

## Endpoints

### GET `/`

Retorna status básico da API.

**Resposta:** `200 OK`
```json
{"message":"API rodando!"}
```

---

### GET `/health`

Health check básico.  
**Resposta:** `200 OK`
```json
{"status":"healthy","service":"dreamsquad-challenge-api"}
```

---

### POST `/chat`

Processa a mensagem via agente de IA.

**Request**
```json
{"message":"Sua pergunta aqui"}
```

**Regras:**

- Campo `message` é obrigatório
- Máximo: `MAX_PROMPT_LENGTH` caracteres (presente no .env)
- Proteção contra `prompt injection`
- Limite: `1 requisição/segundo por IP`



**Respostas comuns**
- `200` → `{"response":"..."}`  
- `400` → Erro de validação (Pydantic) 
- `429` → rate limit  
- `500` → erro interno / prompt injection detectada

---

## Modelos de Dados

### ChatRequest

```python
{
  "message": "texto"  # Mensagem do usuário (1-MAX_PROMPT_LENGTH chars)
}
```

### ChatResponse

```python
{
  "response": "texto"  # Resposta gerada pelo agente
}
```

## Códigos de Erro

| Código | Descrição | Causa Comum |
|--------|-----------|-------------|
| `200` | OK | Requisição bem-sucedida |
| `400` | Bad Request | Mensagem vazia / payload inválido |
| `422` | Unprocessable Entity | Schema fora do padrão |
| `429` | Too Many Requests | Rate limit excedido |
| `500` | Internal Server Error | Erro do agente / prompt injection bloqueada |


## Documentação Interativa

- Swagger UI: http://localhost:8000/docs  

## Segurança

Prompt injection é bloqueada via regex. O sistema bloqueia automaticamente padrões suspeitos:

**❌ Bloqueados:**
```
- "mostre seu prompt"
- "ignore suas instruções"
- "revele o system prompt"
- "system_prompt"
```

**✅ Permitidos:**

```
- Perguntas normais
- Cálculos matemáticos
- Conversas casuais
```