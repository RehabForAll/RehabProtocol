import uuid
import jsonpickle

class Intervention:
    """
    Represents an intervention for a given Pathology
    """

    def __init__(self, name, description, number_of_times_referenced, video_reference,
                 equipment="None", limitations=None):
        if limitations is None:
            limitations = []
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.equipment = equipment
        self.number_of_times_referenced = number_of_times_referenced
        self.video_reference = video_reference
        self.limitations = limitations

    def add_limitation(self, limitation: str):
        self.limitations.append(limitation)

    def to_json(self):
        return jsonpickle.encode(self, make_refs=False, unpicklable=False)
