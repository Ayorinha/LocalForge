from localforge.isolation import IsolationProfile,is_restricted
def test_default_is_restricted(): assert is_restricted(IsolationProfile())