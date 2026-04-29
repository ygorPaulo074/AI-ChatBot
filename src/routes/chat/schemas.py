from pydantic import BaseModel
from typing import List, Optional, Literal


class ChatRequest(BaseModel):
    session_id: str
    message: str


class TokenUsage(BaseModel):
    input: int
    output: int
    total: int


class SessionInfo(BaseModel):
    session_id: str
    agent_id: str
    model: str
    created_at: str
    response_time_ms: int
    tokens: TokenUsage


class Message(BaseModel):
    id: str
    role: Literal["user", "assistant"]
    content: str
    timestamp: str
    status: Literal["delivered", "pending", "failed", "escalated"]
    tokens: int
    response_time_ms: Optional[int] = None  


class ConversationEntry(BaseModel):
    message: Message


class ChatResponse(BaseModel):
    session: SessionInfo
    conversation: List[ConversationEntry]