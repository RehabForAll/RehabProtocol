import json
import uuid
from dataclasses import dataclass, asdict, field
from functools import cached_property
from typing import List


@dataclass
class Pathology:
    """
    Represents a pathology, which is initialized with a name and description.
    """
    name: str
    description: str
    phases: List[str] = field(default_factory=list)

    @cached_property
    def id(self):
        return str(uuid.uuid4())

    def to_json(self):
        return json.dumps(asdict(self))

    @classmethod
    def from_json_file(cls, file_name: str):
        if not file_name.endswith('.json'):
            file_name += '.json'

        with open(file_name, 'r') as in_file:
            json_file = json.load(in_file)

        # parse file
        return cls(**json_file)

    def add_phase(self, phase):
        self.phases.append(phase)

    def remove_phase(self, phase_number):
        self.phases.pop(phase_number - 1)

    def get_phases(self):
        return self.phases
