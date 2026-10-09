from dataclasses import dataclass,field
from time import time
@dataclass
class Trace:
    trace_id:str
    started_at:float=field(default_factory=time)
    attributes:dict=field(default_factory=dict)
