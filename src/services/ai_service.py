"""
Orquestra as chamadas ao modelo de IA.
Recebe a mensagem do usuário, carrega o context.xml do agente, injeta via ai_client,
avalia as condições de escalonamento definidas no AgentContext e retorna
a resposta estruturada com metadados de sessão, tokens e tempo de resposta.
"""
