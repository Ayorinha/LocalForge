"""Local runtime safety controls."""
from dataclasses import dataclass

@dataclass(frozen=True)
class RuntimePolicy:
    allow_network: bool = False
    allow_shell: bool = False
    max_context_tokens: int = 8192

def validate_policy(policy: RuntimePolicy) -> None:
    if policy.max_context_tokens <= 0:
        raise ValueError("max_context_tokens must be positive")
