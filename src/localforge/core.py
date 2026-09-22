from dataclasses import dataclass
from typing import Protocol
class ModelBackend(Protocol):
 def generate(self,prompt:str,*,temperature:float=0.0)->str:...
@dataclass
class LocalRuntime:
 backend:ModelBackend;model:str
 def generate(self,prompt):
  if not prompt.strip():raise ValueError("prompt cannot be empty")
  return self.backend.generate(prompt,temperature=0.0)
