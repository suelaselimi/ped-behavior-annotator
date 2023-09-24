from dataclasses import dataclass, field
from typing import *

@dataclass
class SingleFrameAnnotataion:
    time: float
    frame: int
    tags: List[str] = field(default_factory=list)

