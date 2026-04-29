"""
Endpoints de chat:
  POST /chat                        — envia mensagem para a IA, injeta context.xml do agente via ai_service,
                                      avalia condições de escalonamento, executa quality_analyzer pós-resposta
                                      e retorna resposta estruturada com metadados de sessão e tokens.

Ciclo de vida da sessão:
  POST /chat/{session_id}/end       — encerra a sessão, grava ended_at
  POST /chat/{session_id}/resolve   — marca a sessão como resolvida (resolved=true)
  POST /chat/{session_id}/escalate  — marca a sessão como escalonada (escalated=true)
"""
