import importlib.metadata
from typing import Dict

from omegaconf import DictConfig

from rlpyt._base import BaseRLAgent
from rlpyt.ddpg import DDPGAgent
from rlpyt.ddqn import DDQNAgent
from rlpyt.dqn import DQNAgent
from rlpyt.dueldqn import DuelDQNAgent
from rlpyt.ppo import PPOAgent
from rlpyt.sac import SACAgent
from rlpyt.td3 import TD3Agent
from rlpyt.trpo import TRPOAgent

AGENTS: Dict[str, BaseRLAgent] = {
    "ddpg": DDPGAgent,
    "ddqn": DDQNAgent,
    "dqn": DQNAgent,
    "dueldqn": DuelDQNAgent,
    "ppo": PPOAgent,
    "sac": SACAgent,
    "td3": TD3Agent,
    "trpo": TRPOAgent,
}


def make(cfg: DictConfig) -> BaseRLAgent:
    """To instantiate an agent"""

    def _get_agent(cfg: DictConfig) -> BaseRLAgent:
        """For python annotations"""
        return AGENTS[cfg.agent.algo](cfg)

    agent = _get_agent(cfg)
    agent.setup_model()
    return agent


__version__ = importlib.metadata.version("rlpyt")

__all__ = [
    DDPGAgent,
    DDQNAgent,
    DQNAgent,
    DuelDQNAgent,
    PPOAgent,
    SACAgent,
    TD3Agent,
    TRPOAgent,
    BaseRLAgent,
    AGENTS,
]
