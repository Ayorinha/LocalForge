from localforge.core import *

class Fake:\n def generate(self,prompt,*,temperature=0.0):return prompt\ndef test_runtime():assert LocalRuntime(Fake(),"demo").generate("hello")=="hello"
