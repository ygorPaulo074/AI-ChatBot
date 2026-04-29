"""
Testes dos endpoints do agente:
  POST   /agent                 — criação, validação de arquivos, retorno de API Key
  GET    /agent                 — autenticação, dados retornados
  GET    /agent/context         — contexto atual e versão
  GET    /agent/context/history — histórico de versões e changes
  GET    /agent/metrics         — métricas agregadas
  PUT    /agent/context         — atualização parcial (PATCH semântico), incremento de versão
  DELETE /agent                 — remoção completa
"""
