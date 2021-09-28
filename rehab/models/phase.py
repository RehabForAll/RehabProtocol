import uuid
import jsonpickle


class Phase:
    """
    Represents a phase, which is initialized for a given pathology.
    """

    def __init__(self, description, length, reference_articles, limitations=None, goals=None):
        if limitations is None:
            limitations = []
        if goals is None:
            goals = []

        self.id = str(uuid.uuid4())
        self.description = description
        self.length = length
        self.reference_articles = reference_articles
        self.limitations = limitations
        self.goals = goals
        self.interventions = {}

    def add_limitation(self, limitation):
        self.limitations.append(limitation)

    def add_goal(self, goal):
        self.goals.append(goal)

    def add_intervention(self, intervention):
        self.interventions[intervention.id] = intervention

    def remove_intervention(self, intervention_id):
        self.interventions.pop(intervention_id)

    def to_json(self):
        return jsonpickle.encode(self, make_refs=False, unpicklable=False)
