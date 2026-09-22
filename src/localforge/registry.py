from dataclasses import dataclass
@dataclass(frozen=True)
class Model: name:str; task:str; context:int; local:bool=True
class Registry:
 def __init__(self,models=None): self.models=list(models or [])
 def add(self,m): self.models.append(m)
 def find(self,task): return [m for m in self.models if m.task==task and m.local]
