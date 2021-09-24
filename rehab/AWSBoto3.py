import boto3
import json


# from boto.dynamodb2.table import Table

# For a Boto3 service resource
ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = ddb.Table('UUIDPathology')


# with table.batch_writer() as batch:
#     batch.put_item(
#         Item={
#             "UUID": "8337d1e3-9654-4268-b52a-2bd009b902fd",
#             "PathologyUUID": "acromioclavicular_joint_reconstruction-8337d1e3-9654-4268-b52a-2bd009b902fd-PHASE-2",
#             "Phase": 2,
#             "description": "AC reconstruction is surgery to repair a ligament injury. A ligament is connective tissue that connects bones or holds a joint together. The AC is where the highest point of your shoulder bone meets your clavicle (collarbone).",
#             "reference_articles": "6",
#             "Length": "4 weeks",
#             "Limitations":
#             [{
#                 "limitation": "No lifting shoulder over head"
#             }, {
#                 "limitation": "avoid lifting first 5 weeks"
#             }, {
#                 "limitation": "avoid reaching behind back excessively"
#             }
#             ],
#             "Goals": ["Full passive range of motion for shoulder fleion and internal rotation", "pain free ADLs", "90% full external rotation"],
#             "Interventions": [
#                 {
#                     "name": "passive range of motion shoulder",
#                     "description": "do the YMCA but in all planes",
#                     "equpiment": False,
#                     "number_of_times_referenced": "5",
#                     "video reference": "https://www.youtube.com/watch?v=CSgL0qB7DEY&ab_channel=GreenredProductions-RelaxingMusic",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#                 },
#                 {
#                     "name": "internal rotation against band",
#                     "description": "pulling band inward against band",
#                     "equpiment": "resistance band",
#                     "number_of_times_referenced": "2",
#                     "video reference": "https://www.youtube.com",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#                 },
#                 {
#                     "name": "external rotation against band",
#                     "description": "rotate hand outward against band",
#                     "equpiment": "resistance band",
#                     "number_of_times_referenced": "2",
#                     "video reference": "https://www.youtube.com/",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#                 },
#                 {
#                     "name": "Rhythmic stabilization",
#                     "description": "Move the arm in different planes of motion with cues for contracting against or with manual resistance",
#                     "equpiment": False,
#                     "number_of_times_referenced": "1",
#                     "video reference": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#                 }
#             ]
#         }
#     )
#     batch.put_item(
#         Item={
#             "UUID": "94bcdba9-02cb-4be1-9cad-e13cc8fd832c",
#             "PathologyUUID": "rotator_cuff_repair_small-94bcdba9-02cb-4be1-9cad-e13cc8fd832c-PHASE-1",
#             "Phase": 1,
#             "description": "Surgery to repair a torn rotator cuff most often involves re-attaching the tendon to the head of humerus (upper arm bone). A partial tear, however, may need only a trimming or smoothing procedure called a debridement. A complete tear is repaired by stitching the tendon back to its original site on the humerus.",
#             "goals": ["Protect surgical repair", "Avoid a stiff shoulder", "start PT after 4 weeks"],
#             "reference_articles": "4",
#             "Length": "4 weeks",
#             "Limitations":
#             ["Sling first 6 weeks ", "ok to shower but keep surgical area dry",
#              "avoid reaching behind back excessively", "avoid active contraction first 4 weeks"],
#             "Interventions": [
#                 {
#                     "name": "Pendulums",
#                     "description": "bending at hips supporting upper half on table slowly rock surgical arm in circles",
#                     "equpiment": False,
#                     "number_of_times_referenced": "4",
#                     "video reference": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#                 },
#                 {
#                     "name": "Active range of motion for : hand, wrist, elbow",
#                     "description": "keep those body parts movin",
#                     "equpiment": False,
#                     "number_of_times_referenced": "5",
#                     "video reference": "https://www.youtube.com",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#                 },
#                 {
#                     "name": "passive range of motion external rotation",
#                     "description": "rotate hand outward against band",
#                     "equpiment": "resistance band",
#                     "number_of_times_referenced": "2",
#                     "video reference": "https://www.youtube.com/",
#                     "limitations": [{
#                         "as tolerated by pain?": True

#                     }, {
#                         "range limits": "45 degrees"
#                     }]
#                 }
#             ]
#         }
#     )
#     batch.put_item(
#         Item={
#             "UUID": "998b2db9-6866-46e2-890b-83b4000a74b6",
#             "PathologyUUID": "rotator_cuff_repair_small-998b2db9-6866-46e2-890b-83b4000a74b6-PHASE-2",
#             "Phase": 2,
#             "description": "Surgery to repair a torn rotator cuff most often involves re-attaching the tendon to the head of humerus (upper arm bone). A partial tear, however, may need only a trimming or smoothing procedure called a debridement. A complete tear is repaired by stitching the tendon back to its original site on the humerus.",
#             "goals": ["may remove sling for showering", "less than 10 lbs", "shoulder flexion 120 degrees passively"],
#             "reference_articles": "4",
#             "Length": "4 weeks",
#             "Limitations":
#             ["Sling first 6 weeks ", "ok to shower but keep surgical area dry",
#              "avoid reaching behind back excessively", "avoid active contraction first 4 weeks"],
#             "Interventions": [
#                 {
#                     "name": "Pendulums",
#                     "description": "bending at hips supporting upper half on table slowly rock surgical arm in circles",
#                     "equpiment": False,
#                     "number_of_times_referenced": "4",
#                     "video reference": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#                 },
#                 {
#                     "name": "wall climb",
#                     "description": "crawl arm up wall",
#                     "equpiment": False,
#                     "number_of_times_referenced": "2",
#                     "video reference": "https://www.youtube.com",
#                     "limitations": [
#                         {
#                             "as tolerated by pain?": True
#                         },
#                         {
#                             "Range of motion": "no more than 120 degrees"
#                         }
#                     ]
#                 },
#                 {
#                     "name": "shoulder Isometrics",
#                     "description": "maintain shoulder in neutral position",
#                     "equpiment": "walls or other solid surfaces",
#                     "number_of_times_referenced": "3",
#                     "video reference": "https://www.youtube.com/",
#                     "limitations": [{
#                         "as tolerated by pain?": True

#                     }]
#                 }
#             ]

#         }
#     )


# UUID = [{
#     "UUID": "73440c14-bfe0-4fb7-9d78-893d15d79eb5",
#     "PathologyUUID": "acromioclavicular_joint_reconstruction-73440c14-bfe0-4fb7-9d78-893d15d79eb5-PHASE-1",
#     "Phase": 1,
#     "description": "AC reconstruction is surgery to repair a ligament injury. A ligament is connective tissue that connects bones or holds a joint together. The AC is where the highest point of your shoulder bone meets your clavicle (collarbone).",
#     "reference_articles": "6",
#     "Length": "5 weeks",
#     "Limitations":
#     [{
#         "limitation": "No lifting shoulder over head"
#     }, {
#         "limitation": "avoid lifting first 5 weeks"
#     }],
#     "Goals": ["control pain", "reduce swelling", "protect shoulder and surgery"],
#     "Interventions": [
#         {
#             "name": "active range of motion of elbow",
#                     "description": "bending your elbow from full extension into full flexion",
#                     "equpiment": False,
#                     "number_of_times_referenced": "5",
#                     "video reference": "https://www.youtube.com/watch?v=3RhAXHRvrKI&ab_channel=VirtualHandCare",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#         },
#         {
#             "name": "active range of motion of wrist",
#                     "description": "bending your wrist from full extension into full flexion",
#                     "equpiment": False,
#                     "number_of_times_referenced": "5",
#                     "video reference": "https://www.youtube.com",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#         },
#         {
#             "name": "Scapular retraction",
#                     "description": "squeeze shoulder blades together",
#                     "equpiment": False,
#                     "number_of_times_referenced": "1",
#                     "video reference": "https://www.youtube.com/",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#         },
#         {
#             "name": "Pendulums",
#                     "description": "bending at hips supporting upper half on table slowly rock surgical arm in circles",
#                     "equpiment": False,
#                     "number_of_times_referenced": "3",
#                     "video reference": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#         }
#     ]
# },
#     {
# "UUID": "8337d1e3-9654-4268-b52a-2bd009b902fd",
# "PathologyUUID": "acromioclavicular_joint_reconstruction-8337d1e3-9654-4268-b52a-2bd009b902fd-PHASE-2",
# "Phase": 2,
# "description": "AC reconstruction is surgery to repair a ligament injury. A ligament is connective tissue that connects bones or holds a joint together. The AC is where the highest point of your shoulder bone meets your clavicle (collarbone).",
# "reference_articles": "6",
# "Length": "4 weeks",
# "Limitations":
# [{
#     "limitation": "No lifting shoulder over head"
# }, {
#     "limitation": "avoid lifting first 5 weeks"
# }, {
#     "limitation": "avoid reaching behind back excessively"
# }
# ],
# "Goals": ["Full passive range of motion for shoulder fleion and internal rotation", "pain free ADLs", "90% full external rotation"],
# "Interventions": [
#     {
#         "name": "passive range of motion shoulder",
#                 "description": "do the YMCA but in all planes",
#                 "equpiment": False,
#                 "number_of_times_referenced": "5",
#                 "video reference": "https://www.youtube.com/watch?v=CSgL0qB7DEY&ab_channel=GreenredProductions-RelaxingMusic",
#                 "limitations": [{
#                     "as tolerated by pain?": True
#                 }]
#     },
#     {
#         "name": "internal rotation against band",
#                 "description": "pulling band inward against band",
#                 "equpiment": "resistance band",
#                 "number_of_times_referenced": "2",
#                 "video reference": "https://www.youtube.com",
#                 "limitations": [{
#                     "as tolerated by pain?": True
#                 }]
#     },
#     {
#         "name": "external rotation against band",
#                 "description": "rotate hand outward against band",
#                 "equpiment": "resistance band",
#                 "number_of_times_referenced": "2",
#                 "video reference": "https://www.youtube.com/",
#                 "limitations": [{
#                     "as tolerated by pain?": True
#                 }]
#     },
#     {
#         "name": "Rhythmic stabilization",
#                 "description": "Move the arm in different planes of motion with cues for contracting against or with manual resistance",
#                 "equpiment": False,
#                 "number_of_times_referenced": "1",
#                 "video reference": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
#                 "limitations": [{
#                     "as tolerated by pain?": True
#                 }]
#     }
# ]
# },
#     {
#     "UUID": "94bcdba9-02cb-4be1-9cad-e13cc8fd832c",
#     "PathologyUUID": "rotator_cuff_repair_small-94bcdba9-02cb-4be1-9cad-e13cc8fd832c-PHASE-1",
#     "Phase": 1,
#     "description": "Surgery to repair a torn rotator cuff most often involves re-attaching the tendon to the head of humerus (upper arm bone). A partial tear, however, may need only a trimming or smoothing procedure called a debridement. A complete tear is repaired by stitching the tendon back to its original site on the humerus.",
#     "goals": ["Protect surgical repair", "Avoid a stiff shoulder", "start PT after 4 weeks"],
#     "reference_articles": "4",
#     "Length": "4 weeks",
#     "Limitations":
#     ["Sling first 6 weeks ", "ok to shower but keep surgical area dry",
#      "avoid reaching behind back excessively", "avoid active contraction first 4 weeks"],
#     "Interventions": [
#         {
#             "name": "Pendulums",
#                     "description": "bending at hips supporting upper half on table slowly rock surgical arm in circles",
#                     "equpiment": False,
#                     "number_of_times_referenced": "4",
#                     "video reference": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#         },
#         {
#             "name": "Active range of motion for : hand, wrist, elbow",
#                     "description": "keep those body parts movin",
#                     "equpiment": False,
#                     "number_of_times_referenced": "5",
#                     "video reference": "https://www.youtube.com",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#         },
#         {
#             "name": "passive range of motion external rotation",
#                     "description": "rotate hand outward against band",
#                     "equpiment": "resistance band",
#                     "number_of_times_referenced": "2",
#                     "video reference": "https://www.youtube.com/",
#                     "limitations": [{
#                         "as tolerated by pain?": True

#                     }, {
#                         "range limits": "45 degrees"
#                     }]
#         }
#     ]
# },
#     {
#     "UUID": "998b2db9-6866-46e2-890b-83b4000a74b6",
#     "PathologyUUID": "rotator_cuff_repair_small-998b2db9-6866-46e2-890b-83b4000a74b6-PHASE-2",
#     "Phase": 2,
#     "description": "Surgery to repair a torn rotator cuff most often involves re-attaching the tendon to the head of humerus (upper arm bone). A partial tear, however, may need only a trimming or smoothing procedure called a debridement. A complete tear is repaired by stitching the tendon back to its original site on the humerus.",
#     "goals": ["may remove sling for showering", "less than 10 lbs", "shoulder flexion 120 degrees passively"],
#     "reference_articles": "4",
#     "Length": "4 weeks",
#     "Limitations":
#     ["Sling first 6 weeks ", "ok to shower but keep surgical area dry",
#      "avoid reaching behind back excessively", "avoid active contraction first 4 weeks"],
#     "Interventions": [
#         {
#             "name": "Pendulums",
#                     "description": "bending at hips supporting upper half on table slowly rock surgical arm in circles",
#                     "equpiment": False,
#                     "number_of_times_referenced": "4",
#                     "video reference": "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
#                     "limitations": [{
#                         "as tolerated by pain?": True
#                     }]
#         },
#         {
#             "name": "wall climb",
#                     "description": "crawl arm up wall",
#                     "equpiment": False,
#                     "number_of_times_referenced": "2",
#                     "video reference": "https://www.youtube.com",
#                     "limitations": [
#                         {
#                             "as tolerated by pain?": True
#                         },
#                         {
#                             "Range of motion": "no more than 120 degrees"
#                         }
#                     ]
#         },
#         {
#             "name": "shoulder Isometrics",
#                     "description": "maintain shoulder in neutral position",
#                     "equpiment": "walls or other solid surfaces",
#                     "number_of_times_referenced": "3",
#                     "video reference": "https://www.youtube.com/",
#                     "limitations": [{
#                         "as tolerated by pain?": True

#                     }]
#         }
#     ]
# }]
x = table.scan()
print(x)
