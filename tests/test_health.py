from localforge.registry import Registry, Model
from localforge.health import check_model

def test_model_health():
    registry=Registry([Model("llama", "chat", 4096)])
    assert check_model(registry, "llama").available
    assert not check_model(registry, "missing").available
