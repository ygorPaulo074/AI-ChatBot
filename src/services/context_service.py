"""
Gerencia o versionamento de contexto dos agentes.
Salva novas versões do AgentContext, calcula o diff de campos alterados para
popular o histórico (changes), e retorna versões anteriores sob demanda.
Cada PUT /agent/context cria uma nova linha em agent_contexts com version incrementado.
"""
