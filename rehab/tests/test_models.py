import os
import unittest

from rehab.models.intervention import Intervention
from rehab.models.pathology import Pathology
from rehab.models.phase import Phase


class TestPath(unittest.TestCase):
    p1 = Pathology('my-name', 'my test description.')
    print('P1:', p1)
    p_id = p1.id
    print('P1 -> id:', p_id)
    assert p1.id == p_id, 'expected id value to be cached'

    print('Serialized JSON:', p1.to_json())

    # Save JSON to file
    with open('test_file.json', 'w') as out_file:
        out_file.write(p1.to_json())

    # De-serialize object from file
    p2 = Pathology.from_json_file('test_file')

    print('P2:', p2)

    # assert both objects are same
    assert p2 == p1

    # IDs should be unique, since it's automatically generated each time (we
    # don't pass in an ID to the constructor or store it in JSON file)
    assert p1.id != p2.id, 'expected IDs to be unique'

    out_file.close()
    os.remove('test_file.json')


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
    import json

    # read file
    with open('data/test_case_1.json', 'r') as test_case_1_file:
        test_case_1 = test_case_1_file.read()

    # parse file
    obj = json.loads(test_case_1)
    print(obj)
    assert obj is not None


# class TestRoundTripModel(unittest.TestCase):
#     # Create AC pathology
#     pathology = Pathology("Acromioclavicular Joint Reconstruction",
#                           "AC reconstruction is surgery to repair a ligament injury. A ligament is connective tissue "
#                           "that connects bones or holds a joint together. The AC is where the highest point of your "
#                           "shoulder bone meets your clavicle (collarbone)")
#
#     # First phase
#     phase_one = Phase("Phase 1", "5 weeks", 6, ["No lifting shoulder over head", "avoid lifting first 5 weeks"],
#                       ["control pain", "reduce swelling", "protect shoulder and surgery"])
#
#     # Phase 1 intervention 1
#     phase_one_intervention_one = Intervention("active range of motion of elbow",
#                                               "bending your elbow from full extension into full flexion", False, 5,
#                                               "https://www.youtube.com/watch?v=3RhAXHRvrKI&ab_channel=VirtualHandCare")
#
#     phase_one_intervention_one.add_limitation("as tolerated by pain")
#
#     # Phase 1 intervention 2
#     phase_one_intervention_two = Intervention("active range of motion of wrist",
#                                               "bending your wrist from full extension into full flexion", False, 5,
#                                               "https://www.youtube.com")
#     phase_one_intervention_two.add_limitation("as tolerated by pain")
#
#     # Add all interventions to phase 1
#     phase_one.add_intervention(phase_one_intervention_one)
#     phase_one.add_intervention(phase_one_intervention_two)
#
#     # Second phase
#     phase_two = Phase("Phase 2", "4 weeks", 6)
#     phase_two.add_limitation("No lifting shoulder over head")
#     phase_two.add_limitation("Avoid lifting first 5 weeks")
#     phase_two.add_limitation("Avoid reaching behind back excessively")
#     phase_two.add_goal("Full passive range of motion for shoulder flexion and internal rotation")
#     phase_two.add_goal("Pain free ADLs")
#     phase_two.add_goal("90% full external rotation")
#
#     # Phase 2 intervention 1
#     phase_two_intervention_one = Intervention("passive range of motion shoulder", "do the YMCA but in all planes",
#                                               5,
#                                               "https://www.youtube.com/watch?v=CSgL0qB7DEY&ab_channel"
#                                               "=GreenredProductions-RelaxingMusic")
#     phase_two_intervention_one.add_limitation("as tolerated by pain")
#
#     # Phase 2 intervention 2
#     phase_two_intervention_two = Intervention("internal rotation against band", "pulling band inward against band", 2,
#                                               "https://www.youtube.com/")
#     phase_two_intervention_two.add_limitation("as tolerated by pain")
#
#     # Add all interventions to phase 2
#     phase_two.add_intervention(phase_two_intervention_one)
#     phase_two.add_intervention(phase_two_intervention_two)
#
#     # Add all phases
#     pathology.add_phase(phase_one)
#     pathology.add_phase(phase_two)
#
#     # read file
#     with open('data/test_case_1.json', 'r') as test_case_1_file:
#         test_case_1 = test_case_1_file.read()
#
#     # parse file
#     assert pathology == Pathology(**obj)


if __name__ == '__main__':
    unittest.main()
