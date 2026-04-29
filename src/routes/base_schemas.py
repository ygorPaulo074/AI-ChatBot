from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Literal


class FileReference(BaseModel):
    name: str
    url: HttpUrl


class RestrictionsConfig(BaseModel):
    topics: Optional[List[str]] = []
    files: Optional[List[FileReference]] = []


class KnowledgeBaseConfig(BaseModel):
    urls: Optional[List[HttpUrl]] = []
    files: Optional[List[FileReference]] = []


class EscalationCondition(BaseModel):
    type: Literal["keyword", "sentiment", "message_count", "topic", "time_elapsed", "intent"]
    value: Optional[str | int | float] = None
    values: Optional[List[str]] = None
    threshold: Optional[float] = None  # usado por sentiment


class EscalationTrigger(BaseModel):
    operator: Literal["OR", "AND"]
    conditions: List[EscalationCondition]


class AgentContext(BaseModel):
    tone: Optional[Literal["formal", "informal", "neutro"]] = None
    language: Optional[str] = None           # ex: "pt-BR", "en-US"
    segment: Optional[str] = None            # ex: "ecommerce", "saas"
    persona: Optional[str] = None
    behavior: Optional[str] = None
    fallback_message: Optional[str] = None
    tags: Optional[List[str]] = []
    restrictions: Optional[RestrictionsConfig] = None
    knowledge_base: Optional[KnowledgeBaseConfig] = None
    escalation_trigger: Optional[EscalationTrigger] = None