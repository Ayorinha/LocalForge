from localforge.core import LocalRuntime

class Fake:
    def generate(self, prompt, *, temperature=0.0):
        return prompt

def test_runtime():
    assert LocalRuntime(Fake(), "demo").generate("hello") == "hello"
