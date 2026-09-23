"""Production smoke tests for LocalForge."""
import importlib

def test_package_imports() -> None:
    module = importlib.import_module("localforge")
    assert module.__name__ == "localforge"
