from localforge.security import RuntimePolicy,validate_policy

def test_runtime_policy_defaults_to_restricted():
    p=RuntimePolicy(); validate_policy(p); assert not p.allow_network and not p.allow_shell
