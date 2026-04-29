"""
Endpoints de chat:
  POST /chat — envia mensagem para a IA, injeta context.xml do agente via ai_service,
               avalia condições de escalonamento, executa quality_analyzer pós-resposta
               e retorna resposta estruturada com metadados de sessão e tokens.
"""
