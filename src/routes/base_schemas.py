from pydantic import BaseModel, HttpUrl, ValidationError
from typing import List, Optional, Literal

class FileReference(BaseModel):
    name: str
    url: HttpUrl

class RestrictionsConfig(BaseModel):
    topics: Optional[List[str]] = []
    files: Optional[List[FileReference]] = []

class KnowledgeBaseConfig(BaseModel):
    topics: Optional[List[str]] = []
    files: Optional[List[FileReference]] = []

class EscalationCondition(BaseModel):
    type: Literal["sentiment", "message_count", "keyword", "topic"]
    value: Optional[str] = None
    values: Optional[List[str]] = None

class EscalationTrigger(BaseModel):
    operator: Literal["OR", "AND"]
    conditions: List[EscalationCondition]

class AgentContext(BaseModel):
    restrictions: Optional[RestrictionsConfig] = None
    knowledge_base: Optional[KnowledgeBaseConfig] = None
    escalation_conditions: Optional[List[EscalationCondition]] = None
    escalation_trigger: Optional[EscalationTrigger] = None
    
