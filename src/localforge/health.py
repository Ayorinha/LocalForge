from dataclasses import dataclass

@dataclass(frozen=True)
class ModelHealth:
    name: str
    available: bool
    reason: str

def check_model(registry, name: str) -> ModelHealth:
    if not name:
        raise ValueError("model name is required")
    available = any(model.name == name and model.local for model in registry.models)
    return ModelHealth(name, available, "registered" if available else "not-registered")
