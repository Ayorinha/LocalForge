from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
class ModelBackend(Protocol):
    def generate(self, prompt: str, *, temperature: float = 0.0) -> str: ...
@dataclass
class LocalRuntime:
    backend: ModelBackend; model: str
    def __post_init__(self):
        if not self.model.strip(): raise ValueError("model must be non-empty")
    def generate(self, prompt: str, *, temperature: float = 0.0) -> str:
        if not prompt.strip() or not 0.0 <= temperature <= 2.0: raise ValueError("invalid prompt or temperature")
        return self.backend.generate(prompt, temperature=temperature)
