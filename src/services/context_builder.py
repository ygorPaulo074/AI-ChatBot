"""
Transforma o AgentContext (Pydantic) em um prompt XML estruturado.
Executado no POST /agent (criação) e no PUT /agent/context (atualização).
O XML gerado é persistido em context.xml e injetado como system prompt
em cada chamada do POST /chat via ai_service.
"""
