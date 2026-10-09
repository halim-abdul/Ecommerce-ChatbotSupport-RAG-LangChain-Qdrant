from dataclasses import dataclass, field
from typing import Any

@dataclass
class RetrievedChunk:
    text: str
    score: float
    source: str
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class RagAnswer:
    answer: str
    sources: list[str]
    context: list[RetrievedChunk]
