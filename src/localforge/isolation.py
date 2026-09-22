"""Isolation policy for private model runtimes."""
from dataclasses import dataclass
@dataclass(frozen=True)
class IsolationProfile:
    network: bool=False
    filesystem_write: bool=False
    subprocess: bool=False

def is_restricted(profile: IsolationProfile) -> bool:
    return not (profile.network or profile.filesystem_write or profile.subprocess)