import json
import sys
from typing import Dict, List


def create_new_cwi(object_id, skill_id):
    return ['ClassWithId', {'ObjectId': object_id, 'MetadataId': 3,
                            'Values': [['_skill_id : Primitive', skill_id], ['_kind_id : Primitive', 0],
                                       ['_calc_type_id : Primitive', 0], ['_koudou_kouka_id : Primitive', 0],
                                       ['_target_condition : Primitive', 0], ['_use_point : Primitive', 0],
                                       ['_hit_percent : Primitive', 100], ['_element : Primitive', 0],
                                       ['_effect_value : Primitive', 0], ['_target_ptn_id : Primitive', 0],
                                       ['_action_command_type_id : Primitive', 0], ['_item_id : Primitive', 0],
                                       ['_is_reget_item : Primitive', False],
                                       ['_can_action_defense : Primitive', False], ['_is_disp_item : Primitive', False],
                                       ['_message_id : Primitive', 0]]}]

input_file = sys.argv[1]

file_reader = open(input_file, 'r')
file_content = json.load(file_reader)
classes_with_ids = []

for item in file_content:
    item_class = item[0]
    if item_class == 'ClassWithId':
        classes_with_ids.append(item)

last = classes_with_ids[-1]
last_dict = last[1]
last_object_id = last_dict['ObjectId']
last_skill_id = last_dict['Values'][0][1]

i = 1
amount_to_add = input('How many Skill do you want to add? : ')
display_amount_changed = amount_to_add

try:
    val = int(amount_to_add)
except ValueError:
    print("That's not an int!")
    sys.exit()

amount_to_add = int(amount_to_add)
while i <= amount_to_add:
    skill_id = last_skill_id + i
    new_id = last_object_id + i
    new_cwi = create_new_cwi(new_id, skill_id)
    classes_with_ids.append(new_cwi)
    file_content.insert(-1, new_cwi)
    i += 1

print("""
You added """ + display_amount_changed + """ Skill!
Bubye for now!
""")

output_file = input_file.replace('.json','_added.json')
file_writer = open(output_file, 'w')
file_writer.write(json.dumps(file_content, indent=2))