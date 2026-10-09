from dataclasses import dataclass
@dataclass
class EvalCase:
    question:str
    expected_answer:str|None=None
    expected_sources:list[str]|None=None
    intent:str|None=None
