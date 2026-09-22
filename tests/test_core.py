from localforge.core import LocalRuntime
class Fake:
    def generate(self, prompt, *, temperature=0.0): return f"{temperature}:{prompt}"
def test_runtime(): assert LocalRuntime(Fake(), "demo").generate("hello") == "0.0:hello"
