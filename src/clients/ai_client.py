"""
Conexão e configuração com o modelo de IA via LiteLLM.
Abstrai o provedor (Anthropic, OpenAI, Gemini, DeepSeek, Groq), gerencia
API key, modelo e timeout. Expõe interface única de completion para o ai_service.
"""
from dataclasses import dataclass
from litellm import completion
from src.infrastructure.config import settings


@dataclass
class AIResponse:
    content: str
    usage: dict


class AIClient:

    def complete(self, system: str, messages: list[dict], max_tokens: int = 1024) -> AIResponse:
        response = completion(
            model=settings.AI_MODEL,
            api_key=settings.AI_API_KEY,
            messages=[{"role": "system", "content": system}, *messages],
            max_tokens=max_tokens,
        )
        return AIResponse(
            content=response.choices[0].message.content,
            usage={
                "input": response.usage.prompt_tokens,
                "output": response.usage.completion_tokens,
                "total": response.usage.total_tokens,
            },
        )
