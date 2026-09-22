from localforge.registry import Registry
from localforge.health import check_model

def test_model_health():
    registry=Registry()
    registry.register("llama", "local")
    assert check_model(registry,"llama").available
    assert not check_model(registry,"missing").available
