import uuid
import json
from dataclasses import dataclass, asdict, field
from functools import cached_property
from typing import List


@dataclass
class Intervention:
    """
    Represents an intervention for a given Pathology
    """
    name: str
    description: str
    times_referenced: int
    video_reference: str
    equipment: str = field(default_factory=str)
    limitations: List[str] = field(default_factory=list)
    id: str = field(default=str(uuid.uuid4()))

    def add_limitation(self, limitation: str):
        self.limitations.append(limitation)

    def to_json(self):
        return json.dumps(asdict(self))
