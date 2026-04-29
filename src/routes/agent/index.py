"""
Endpoints do agente:
  POST   /agent                    — cria agente, gera context.xml e retorna API Key
  GET    /agent                    — retorna dados do agente autenticado
  GET    /agent/context            — retorna contexto atual com versão
  GET    /agent/context/history    — histórico de versões e campos alterados
  GET    /agent/metrics            — métricas agregadas de sessões e mensagens
  PUT    /agent/context            — atualiza contexto, incrementa versão, regenera XML
  DELETE /agent                    — remove agente, context.xml e todos os dados associados
"""
