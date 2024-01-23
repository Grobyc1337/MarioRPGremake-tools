# Made by Maxtoad & Grobyc

import os
import json
import sys
from typing import Dict, List

import subprocess


def create_new_cwi(monster_var, speed_var):
    return [ "ClassWithId", { "ObjectId": 5, "MetadataId": 3, "Values": [[ "_monster_id : Primitive", 2 ], [ "_character_id : Primitive", monster_var ], [ "_hp : Primitive", 16 ], [ "_fp : Primitive", 150 ], [ "_attack : Primitive", 1], ["_defense : Primitive", 3], ["_magic_attack : Primitive", 1], ["_magic_defense : Primitive", 1], ["_speed : Primitive", speed_var], ["_avoid : Primitive", 0], ["_resist_jump : Primitive", 0], ["_resist_fire : Primitive", 2], ["_resist_thunder : Primitive", 0], ["_resist_ice : Primitive", 0], ["_invalid_fear : Primitive", false], ["_invalid_poison : Primitive", false], ["_invalid_sleep : Primitive", false], ["_invalid_silent : Primitive", false], ["_resist_sheep : Primitive", 1], ["_invalid_geno_cutter : Primitive", false], ["_invalid_holy_water : Primitive", true], ["_invalid_yoshi_cookie : Primitive", false], ["_start_state : Primitive", 0], ["_exp : Primitive", 2000], ["_coin : Primitive", 0], ["_is_drop_100per : Primitive", false], ["_drop_item_id_1 : Primitive", 0], ["_drop_item_id_2 : Primitive", 0], ["_drop_item_by_yoshi_cookie : Primitive", 87], ["_bonus_flower_id : Primitive", 1], ["_bonus_flower_persent : Primitive", 30], ["_appear_ptn_id : Primitive", 1], ["_escape_ptn_id : Primitive", 1], ["_collision_size_x : Primitive", 0.0], ["_collision_size_y : Primitive", 0.0], ["_collision_size_z : Primitive", 0.0], ["_collision_offset_x : Primitive", 0.0], ["_collision_offset_y : Primitive", 0.0], ["_collision_offset_z : Primitive", 0.0], ["_scale : Primitive", 0.0], ["_nanikangaeteruno_id : Primitive", 502004], ["_nanikangaeteruno_mess_num : Primitive", 1], ["_ryuuyou_chara_id : Primitive", 0], ["_cookie_hit_percent : Primitive", 100], ["_monster_book_sort_order : Primitive", 4], ["_monster_book_msg_id : Primitive", 533005], ["_monster_book_area_id : Primitive", 51], ["_monster_book_fixed_position : Primitive", 1], ["_monster_book_encounter_id : Primitive", 0], ["_monster_book_encount_pattern_id : Primitive", 0], ["_monster_book_multiple_display : Primitive", 0], ["_monster_book_camera_pattern : Primitive", 1], ["_monster_book_pos_move_x : Primitive", 0.0], ["_monster_book_pos_move_z : Primitive", 0.0], ["_dying_disp : Primitive", true]]}],


with open('monster.json', 'r') as input_file:
    data = json.load(input_file)


classes_with_ids = []
the_list_2 = []
item2 = 0

speed_factor = input('Multiply Boss Enemies Speed by : ')
display_speed_factor = speed_factor

try:
    val = float(speed_factor)
except ValueError:
    print("That's not an int!")
    sys.exit()

speed_factor = float(speed_factor)

for item in data.values():
    item_class = item[0]
    if item_class == 'ClassWithId':
        monster_id = item[1]['Values'][1][1]
        speed_monster_boss = item[1]['Values'][8][1]
        if monster_id >= 1500:  # Check if Monster is Regular/Not Boss
            speed_monster_boss = float(speed_monster_boss)
            speed_monster_boss = speed_monster_boss * speed_factor
            speed_monster_boss = int(speed_monster_boss)
            item2 = item
            item2[1]['Values'][8][1] = speed_monster_boss
            the_list_2.append(item2)
        else:
            the_list_2.append(item)
    else:
        the_list_2.append(item)


print("""
You Change all Boss Enemies Speed by x""" + display_speed_factor + """ !!
Enjoy!
""")

output_file = 'monster_added.json'
file_writer = open(output_file, 'w')
file_writer.write(json.dumps(the_list_2, indent=2))


file_writer.close()

print("""
Rebuilding the new .json""")

# Run the other script
subprocess.call(["python", "rebuild.py", output_file])

print("""
File has been rebuild! Press Enter to finish""")
input()

os.remove('monster_added.json')

print("""
Deleting monster_added.json""")

sys.exit("Process Completed!")
