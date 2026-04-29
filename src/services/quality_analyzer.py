"""
Análise local de qualidade pós-resposta, sem consumo de tokens.
Usa textblob para calcular sentiment_score e sentiment_label por mensagem.
Usa spaCy para detectar tópicos, main_topic e intent da conversa.
Executado automaticamente após cada resposta do POST /chat e persiste
os resultados em scores.json (storage Local) ou na tabela scores (Database).
"""
