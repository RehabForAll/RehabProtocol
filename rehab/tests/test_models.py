import os
import unittest

from rehab.models.intervention import Intervention
from rehab.models.pathology import Pathology
from rehab.models.phase import Phase


class TestModelsToJSON(unittest.TestCase):
    # Create AC pathology
    pathology = Pathology("Acromioclavicular Joint Reconstruction",
                          "AC reconstruction is surgery to repair a ligament injury. A ligament is connective tissue "
                          "that connects bones or holds a joint together. The AC is where the highest point of your "
                          "shoulder bone meets your clavicle (collarbone)")

    # First phase
    phase_one = Phase("Phase 1", "5 weeks", 6, ["No lifting shoulder over head", "avoid lifting first 5 weeks"],
                      ["control pain", "reduce swelling", "protect shoulder and surgery"])

    # Phase 1 intervention 1
    phase_one_intervention_one = Intervention("active range of motion of elbow",
                                              "bending your elbow from full extension into full flexion",
                                              5,
                                              "https://www.youtube.com/watch?v=3RhAXHRvrKI&ab_channel=VirtualHandCare")

    phase_one_intervention_one.add_limitation("as tolerated by pain")

    # Phase 1 intervention 2
    phase_one_intervention_two = Intervention("active range of motion of wrist",
                                              "bending your wrist from full extension into full flexion",
                                              5,
                                              "https://www.youtube.com")
    phase_one_intervention_two.add_limitation("as tolerated by pain")

    # Add all interventions to phase 1
    phase_one.add_intervention(phase_one_intervention_one)
    phase_one.add_intervention(phase_one_intervention_two)

    # Second phase
    phase_two = Phase("Phase 2", "4 weeks", 6)
    phase_two.add_limitation("No lifting shoulder over head")
    phase_two.add_limitation("Avoid lifting first 5 weeks")
    phase_two.add_limitation("Avoid reaching behind back excessively")
    phase_two.add_goal("Full passive range of motion for shoulder flexion and internal rotation")
    phase_two.add_goal("Pain free ADLs")
    phase_two.add_goal("90% full external rotation")

    # Phase 2 intervention 1
    phase_two_intervention_one = Intervention("passive range of motion shoulder", "do the YMCA but in all planes",
                                              5,
                                              "https://www.youtube.com/watch?v=CSgL0qB7DEY&ab_channel"
                                              "=GreenredProductions-RelaxingMusic")
    phase_two_intervention_one.add_limitation("as tolerated by pain")

    # Phase 2 intervention 2
    phase_two_intervention_two = Intervention("internal rotation against band", "pulling band inward against band", 2,
                                              "https://www.youtube.com/")
    phase_two_intervention_two.add_limitation("as tolerated by pain")

    # Add all interventions to phase 2
    phase_two.add_intervention(phase_two_intervention_one)
    phase_two.add_intervention(phase_two_intervention_two)

    # Add all phases
    pathology.add_phase(phase_one)
    pathology.add_phase(phase_two)

    print(pathology.to_json())
    assert pathology is not None


class TestModelsFromJSON(unittest.TestCase):
    # read and parse file
    pathology_from_file = Pathology.from_json_file('data/test_case_1.json')
    assert pathology_from_file is not None
    assert pathology_from_file.id == "8e7975c2-fc5c-4e0c-8a95-f44b6364428e"
    assert len(pathology_from_file.phases) == 2


class TestRoundtripSerialization(unittest.TestCase):
    pathology = Pathology('my-name', 'my test description.')

    # Save JSON to file
    with open('test_file.json', 'w') as out_file:
        out_file.write(pathology.to_json())

    # De-serialize object from file
    pathology_from_file = Pathology.from_json_file('test_file')

    # assert both objects are same
    assert pathology == pathology_from_file

    assert pathology.id == pathology_from_file.id, 'expected IDs to be the same'

    out_file.close()
    os.remove('test_file.json')


if __name__ == '__main__':
    unittest.main()
