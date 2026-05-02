"""
Gerencia o ciclo de vida dos agentes.
Depende de PersistenceDriver (via factory) para storage,
CacheClient para invalidação de contexto e ContextService para versionamento.
"""
from src.core.persistence.factory import get_driver
from src.core.persistence.base import PersistenceDriver
from src.core.cache.client import CacheClient
from src.core.security import generate_api_key, hash_api_key
from src.core.schemas import AgentRecord, SessionRecord
from src.routes.base_schemas import AgentContext


class AgentService:

    def __init__(self):
        self.driver: PersistenceDriver = get_driver()
        self.cache = CacheClient()

    def create_agent(self, name: str, owner: str, context: AgentContext) -> dict:
        # gera agent_id único e API Key bruta
        # cria AgentRecord com api_key_hash (nunca a chave em claro)
        # persiste AgentRecord via driver.save_agent
        # delega criação do AgentContextRecord (versão 1) ao ContextService
        # retorna agent_id e api_key bruta — única vez que é exposta
        pass

    def get_agent(self, agent_id: str) -> AgentRecord | None:
        # carrega e retorna AgentRecord via driver.load_agent
        pass

    def get_metrics(self, agent_id: str) -> dict:
        # lista todas as SessionRecord do agente via driver.list_sessions
        # agrega: total_sessions, total_messages, total_tokens,
        #         avg_response_time_ms, resolution_rate, escalation_rate
        # retorna dicionário com as métricas calculadas
        pass

    def delete_agent(self, agent_id: str) -> None:
        # remove AgentRecord e todos os dados associados via driver.delete_agent
        # invalida contexto em cache via cache.invalidate_context
        pass
