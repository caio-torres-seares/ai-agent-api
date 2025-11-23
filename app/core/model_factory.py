from app.core.config import settings
from strands.models.ollama import OllamaModel

def build_model():
    
    if settings.MODEL_BACKEND == "ollama":
        return OllamaModel(
            host=settings.OLLAMA_HOST,
            model_id=settings.LLM_MODEL,
        )
    
    if settings.MODEL_BACKEND == "another_backend":
        # Caso queira utilizar outro modelo, implemente aqui
        # OBS: Não esqueça de adicionar a importação necessária no topo do arquivo
        pass

    raise ValueError(f"Modelo {settings.MODEL_BACKEND} desconhecido ou não implementado!")