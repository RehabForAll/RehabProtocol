import jsonpickle
import uuid


class Pathology:
    """
    Represents a pathology, which is initialized with a name and description.
    """

    def __init__(self, name: str, description: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.phases = []

    def add_phase(self, phase):
        self.phases.append(phase)

    def remove_phase(self, phase_number):
        self.phases.pop(phase_number - 1)

    def get_phases(self):
        return self.phases

    def to_json(self):
        return jsonpickle.encode(self, make_refs=False, unpicklable=False)
