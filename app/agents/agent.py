from strands import Agent
from app.core.model_factory import build_model
from strands_tools import calculator

model = build_model()

system_prompt = """
Você é um assistente útil.
Você só deve usar a ferramenta 'calculator' SE o usuário fornecer explicitamente
uma expressão matemática válida, como:
- 2+2
- 1234 * 5678
- sqrt(144)
- O resultado de 20/4

NÃO use a ferramenta se a pergunta for sobre conhecimento geral,
geografia, história, linguagem ou qualquer outra área que NÃO envolva
uma expressão matemática.

Quando não souber, responda normalmente.
"""
_agent_instance: Agent | None = None

def get_agent() -> Agent:
    global _agent_instance
    if _agent_instance is None:   
        _agent_instance = Agent(
            model=model,
            tools=[calculator],
            system_prompt=system_prompt,
        )
    return _agent_instance

def run_agent(message: str) -> str:
    agent = get_agent()
    raw = str(agent(message))
    return raw.rstrip("\n")