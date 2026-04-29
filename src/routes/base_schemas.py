from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Literal


class FileReference(BaseModel):
    name: str
    url: HttpUrl


class RestrictionsConfig(BaseModel):
    topics: List[str] = []
    files: List[FileReference] = []


class KnowledgeBaseConfig(BaseModel):
    urls: List[HttpUrl] = []
    files: List[FileReference] = []


class EscalationCondition(BaseModel):
    type: Literal["keyword", "sentiment", "message_count", "topic", "time_elapsed", "intent"]
    value: Optional[str | int | float] = None
    values: Optional[List[str]] = None
    threshold: Optional[float] = None  # usado por sentiment


class EscalationTrigger(BaseModel):
    operator: Literal["OR", "AND"]
    conditions: List[EscalationCondition]


class AgentContextBase(BaseModel):
    tone: Optional[Literal["formal", "informal", "neutro"]] = None
    language: Optional[str] = None
    segment: Optional[str] = None
    persona: Optional[str] = None
    behavior: Optional[str] = None
    fallback_message: Optional[str] = None
    restrictions: Optional[RestrictionsConfig] = None
    knowledge_base: Optional[KnowledgeBaseConfig] = None
    escalation_trigger: Optional[EscalationTrigger] = None


class AgentContext(AgentContextBase):
    tags: List[str] = []
