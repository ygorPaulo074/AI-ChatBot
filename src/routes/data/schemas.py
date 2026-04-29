from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional, Literal, Dict, Any
from ..base_schemas import AgentContextBase
from ..chat.schemas import ConversationEntry


# ── /data/chat ──────────────────────────────────────────────

class ChatSummary(BaseModel):
    session_id: str
    agent_id: str
    started_at: str
    ended_at: Optional[str] = None
    total_messages: int
    total_tokens: int
    resolved: bool
    escalated: bool


class ChatListResponse(BaseModel):
    total: int
    chats: List[ChatSummary]


# ── /data/chat/{session_id} ──────────────────────────────────

class SessionDetail(ChatSummary):
    pass


class ChatDetailResponse(BaseModel):
    session: SessionDetail
    conversation: List[ConversationEntry]


# ── Insights ─────────────────────────────────────────────────

class SentimentPoint(BaseModel):
    message_id: str
    score: float


class SentimentData(BaseModel):
    score: float
    label: Literal["positive", "neutral", "negative"]
    progression: List[SentimentPoint]


class SentimentInsightResponse(BaseModel):
    session_id: str
    sentiment: SentimentData


class TopicsData(BaseModel):
    detected: List[str]
    main_topic: str
    intent: Optional[str] = None


class TopicsInsightResponse(BaseModel):
    session_id: str
    topics: TopicsData


class MetricsData(BaseModel):
    total_messages: int
    total_tokens: int
    avg_user_message_length: float
    avg_response_time_ms: float
    time_to_escalation_seconds: Optional[int] = None
    resolution: Literal["resolved", "escalated", "open"]


class MetricsInsightResponse(BaseModel):
    session_id: str
    metrics: MetricsData


class AIAnalysis(BaseModel):
    key_points: List[str]
    suggested_actions: List[str]
    summary: str


class SuggestionsInsightResponse(BaseModel):
    session_id: str
    generated_at: str
    ai_analysis: AIAnalysis


class AgentContextSnapshot(BaseModel):
    version: int
    tone: Optional[str] = None
    segment: Optional[str] = None


class FullInsightResponse(BaseModel):
    session_id: str
    agent_id: str
    generated_at: str
    sentiment: SentimentData
    topics: TopicsData
    resolution: Literal["resolved", "escalated", "open"]
    metrics: MetricsData
    agent_context: AgentContextSnapshot
    ai_analysis: AIAnalysis


# ── /data/context ─────────────────────────────────────────────

class UserProfile(BaseModel):
    segment: Optional[str] = None
    language: Optional[str] = None
    form_answers: Optional[Dict[str, Any]] = None


class UserContextSummary(BaseModel):
    user_id: str
    created_at: str
    updated_at: str
    profile: UserProfile


class UserContextListResponse(BaseModel):
    total: int
    contexts: List[UserContextSummary]


class UserContextResponse(UserContextSummary):
    pass


# ── /data/analytics ───────────────────────────────────────────

class TopicPattern(BaseModel):
    topic: str
    count: int
    resolution_rate: Optional[float] = None


class PeakHour(BaseModel):
    hour: str
    avg_chats: int


class AnalyticsSummary(BaseModel):
    total_chats: int
    total_messages: int
    total_users: int
    avg_messages_per_chat: float
    avg_chat_duration_seconds: float
    avg_response_time_ms: float
    resolution_rate: float
    escalation_rate: float
    total_tokens_used: int
    avg_tokens_per_chat: float


class AnalyticsPatterns(BaseModel):
    most_common_topics: List[TopicPattern]
    most_common_unresolved_topics: List[TopicPattern]
    peak_hours: List[PeakHour]
    peak_days: List[str]
    avg_messages_to_resolution: float
    avg_messages_to_escalation: float


class SentimentDistribution(BaseModel):
    positive: float
    neutral: float
    negative: float


class AnalyticsSentiment(BaseModel):
    avg_score: float
    distribution: SentimentDistribution


class UserSegment(BaseModel):
    segment: str
    total_users: int
    resolution_rate: float


class AnalyticsUsers(BaseModel):
    new_users: int
    returning_users: int
    avg_chats_per_user: float
    segments: List[UserSegment]


class TimelineEntry(BaseModel):
    date: str
    total_chats: int
    resolved: int
    escalated: int
    new_users: int
    total_tokens: int
    avg_response_time_ms: float
    avg_sentiment_score: float


class AnalyticsPeriod(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    from_: Optional[str] = Field(None, alias="from")
    to: Optional[str] = None


class AnalyticsResponse(BaseModel):
    generated_at: str
    period: AnalyticsPeriod
    summary: AnalyticsSummary
    patterns: AnalyticsPatterns
    sentiment: AnalyticsSentiment
    users: AnalyticsUsers
    timeline: List[TimelineEntry]
