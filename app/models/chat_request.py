from pydantic import BaseModel, Field, field_validator
from app.core.config import settings

class ChatRequest(BaseModel):
    message: str = Field(
        ..., 
        min_length=1,
        max_length=settings.MAX_PROMPT_LENGTH,
        description="Mensagem do usuário para o agente"
    )

    @field_validator('message')
    def validate_message(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("A mensagem não pode estar vazia!")
        
        return value