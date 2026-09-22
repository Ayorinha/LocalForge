from localforge.registry import *
def test_registry():
 r=Registry([Model('embed','embedding',8192),Model('remote','chat',4096,False)])
 assert [m.name for m in r.find('embedding')]==['embed']
