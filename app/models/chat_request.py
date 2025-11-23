from pydantic import BaseModel, Field, field_validator

class ChatRequest(BaseModel):
    message: str = Field(
        ..., 
        min_length=1,
        max_length=3000,
        description="Mensagem do usuário para o agente"
    )

    @field_validator('message')
    def validate_message(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("A mensagem não pode estar vazia!")
        
        return value