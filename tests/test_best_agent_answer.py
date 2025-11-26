import pytest
import requests
from strands import Agent
from app.core.model_factory import build_model


def ollama_is_running() -> bool:
    """Retorna True se o Agent estiver online."""
    try:
        requests.get("http://localhost:11434", timeout=0.5)
        return True
    except Exception:
        return False
    
    
@pytest.mark.skipif(
    not ollama_is_running(),
    reason="X - Ollama não está rodando. Execute 'ollama serve' para rodar este teste especial."
)
def test_agent_made_by_Caio():
    """
    Teste opcional:
    - Só roda se a IA estiver online
    - Chama o agente real
    - Gera uma mensagem explicando por que eu seria um ótimo estagiário
    """

    system_prompt= """
ATUE COMO: Um Recrutador Técnico Sênior especializado em Engenharia de Dados, Machine Learning e Inteligência Artificial.

MISSÃO: Avaliar o candidato Caio Torres Seares com base em seu currículo e trajetória real, e fornecer uma recomendação clara e objetiva sobre sua contratação para uma vaga técnica.

DADOS DO CANDIDATO (100% VERÍDICOS):
1. Formação e Base Técnica:
   - Estudante de Sistemas de Informação no IFES (6º período, 2023–2026), com forte embasamento teórico e sólido desempenho acadêmico.

2. Produção Científica e Pesquisa Avançada:
   - Coautor de artigo aceito no SBAI 2025: “Sistema Multiagente para Automação Inteligente de Editais Públicos”, evidenciando domínio de NLP, automação inteligente, análise de dados e visão científica.

3. Experiência Técnica Profunda:
   - Desenvolvimento de sistema completo para coleta, extração, limpeza, classificação e armazenamento de editais públicos usando Python, Regex, Tesseract OCR, PdfPlumber, Brotli, MongoDB e Docker.
   - Construção e orquestração de pipelines ETL escaláveis.
   - Modelagem de dados e queries otimizadas.

4. Experiência Profissional em Produção:
   - Desenvolvedor Full Stack Júnior (FAPES), atuando com Angular, TypeScript, JavaScript, Spring Boot, PostgreSQL, APIs REST e Telosys. Experiência real em manutenção e evolução de sistemas oficiais.

5. Experiência Prévia Relevante:
   - Desenvolvimento de aplicações imersivas em VR com Unity e C#, incluindo metaverso educacional, modelagem 3D interativa e interfaces intuitivas.

6. Formação Prática em IA (Bootcamp e Projetos Avançados):
   - Participação em Bootcamp completo de Machine Learning e Deep Learning, adquirindo experiência prática com:
     • Redes neurais, CNNs e RNNs
     • Treinamento e avaliação de modelos
     • Regularização, augmentations e tuning de hiperparâmetros
     • Técnicas modernas de MLOps e ciclo de vida de modelos

   - Projeto aplicado: Treinou uma IA de reconhecimento de imagens usando **fine-tuning** sobre um modelo pré-treinado (transfer learning), demonstrando capacidade de trabalhar com frameworks de DL (PyTorch/TensorFlow), manipulação de datasets, estratégia de freeze/unfreeze de camadas e ajuste fino orientado a desempenho.

7. Competências-Chave:
   - Python, SQL, NLP, ETL, Web Scraping, PostgreSQL, MongoDB, Docker, Regex, Machine Learning, Deep Learning, Fine-Tuning, Pipelines de dados

DIRETRIZES DE RESPOSTA:
- Use linguagem corporativa sênior, objetiva e altamente profissional.
- Avalie Caio como se estivesse realmente recomendando um candidato para contratação em uma equipe de engenharia de dados/ML.
- NÃO sugira contratar como recrutador. A vaga é ENGENHARIA DE DADOS/IA.
- NÃO liste "pontos a melhorar". Este é um pitch de venda agressivo.
- Use tom de autoridade, certeza e entusiasmo profissional.
- Destaque a combinação rara de habilidades: ML + dados + backend + NLP.
- Conclua com uma recomendação firme e fundamentada sobre sua contratação.
- NÃO invente fatos. Baseie-se exclusivamente nas informações acima.
"""


    agent = Agent(
        model=build_model(),
        system_prompt=system_prompt,
    )

    pergunta = "Você acha que devo contratar o Caio Torres Seares para a vaga de Engenharia de Dados/IA na minha equipe? Justifique tecnicamente sua resposta com base nas competências listadas e use o máximo possível de 1000 caracteres."

    print("\n")
    print("-"*150)
    print(f"Enviando pergunta ao agente: Você acha que devo contratar o Caio Torres Seares para a vaga de Engenharia de Dados/IA na minha equipe?")
    print("-"*150)
    response = agent(pergunta)

    print("\n")
    assert len(response.message) > 0