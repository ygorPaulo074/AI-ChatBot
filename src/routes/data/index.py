"""
Endpoints de dados e analytics:
  GET    /data/chat                                   — lista conversas do agente autenticado
  GET    /data/chat/{session_id}                      — histórico completo de uma sessão
  DELETE /data/chat/{session_id}                      — remove sessão e dados associados

Insights (por sessão):
  GET    /data/chat/{session_id}/insights             — insight completo (consome tokens)
  GET    /data/chat/{session_id}/insights/sentiment   — sentimento da sessão (local, sem tokens)
  GET    /data/chat/{session_id}/insights/topics      — tópicos detectados (local, sem tokens)
  GET    /data/chat/{session_id}/insights/metrics     — métricas da sessão (local, sem tokens)
  GET    /data/chat/{session_id}/insights/suggestions — análise e sugestões da IA (consome tokens)

Contexto:
  GET    /data/context                                — contextos de usuários do agente
  GET    /data/context/{user_id}                      — contexto de um usuário específico
  DELETE /data/context/{user_id}                      — remove contexto do usuário

Analytics (agregado por agente):
  GET    /data/analytics                              — visão analítica completa
  GET    /data/analytics/summary                      — resumo numérico agregado
  GET    /data/analytics/patterns                     — padrões de tópico, horário e resolução
  GET    /data/analytics/sentiment                    — distribuição e score médio de sentimento
  GET    /data/analytics/users                        — segmentação e comportamento de usuários
  GET    /data/analytics/timeline                     — evolução diária das métricas
"""
