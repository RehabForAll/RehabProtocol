import uuid
import json
from dataclasses import dataclass, asdict, field
from functools import cached_property
from typing import List, Dict


@dataclass
class Phase:
    """
    Represents a phase, which is initialized for a given pathology.
    """
    description: str
    length: str
    reference_articles: int
    limitations: List[str] = field(default_factory=list)
    goals: List[str] = field(default_factory=list)
    interventions: Dict = field(default_factory=dict)
    id: str = field(default=str(uuid.uuid4()))

    def add_limitation(self, limitation):
        self.limitations.append(limitation)

    def add_goal(self, goal):
        self.goals.append(goal)

    def add_intervention(self, intervention):
        self.interventions[intervention.id] = intervention

    def remove_intervention(self, intervention_id):
        self.interventions.pop(intervention_id)

    def to_json(self):
        return json.dumps(asdict(self))
