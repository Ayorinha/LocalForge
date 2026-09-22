from dataclasses import dataclass

@dataclass(frozen=True)
class ModelHealth:
    name: str
    available: bool
    reason: str

def check_model(registry, name: str) -> ModelHealth:
    if not name: raise ValueError("model name is required")
    models=registry.search(name)
    if models: return ModelHealth(name, True, "registered")
    return ModelHealth(name, False, "not-registered")
