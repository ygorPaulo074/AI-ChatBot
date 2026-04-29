"""
Endpoints de dados e analytics:
  GET    /data/chat                                   — lista conversas do agente autenticado
  GET    /data/chat/{session_id}                      — histórico completo de uma sessão
  DELETE /data/chat/{session_id}                      — remove sessão e dados associados
  GET    /data/chat/{session_id}/insights             — insight completo (consome tokens)
  GET    /data/chat/{session_id}/insights/sentiment   — sentimento da sessão (local, sem tokens)
  GET    /data/chat/{session_id}/insights/topics      — tópicos detectados (local, sem tokens)
  GET    /data/chat/{session_id}/insights/metrics     — métricas da sessão (local, sem tokens)
  GET    /data/chat/{session_id}/insights/suggestions — análise e sugestões da IA (consome tokens)
  GET    /data/context                                — contextos de usuários do agente
  GET    /data/context/{user_id}                      — contexto de um usuário específico
  DELETE /data/context/{user_id}                      — remove contexto do usuário
  GET    /data/analytics                              — visão analítica completa agregada
"""
