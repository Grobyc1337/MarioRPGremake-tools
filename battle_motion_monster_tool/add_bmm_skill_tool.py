# Made by Maxtoad & Grobyc

import json
import sys
from typing import Dict, List
def create_new_cwi(object_id, monster_id, skill_id, string_id_1, string_id_2, string_id_3, string_id_4, string_id_5, string_id_6, string_id_7):
    return ['ClassWithId', {'ObjectId': object_id, 'MetadataId': 3, 'Values': [['_player_id : Primitive', monster_id], ['_skill_id : Primitive', skill_id], ['_weapon_id : Primitive', 0], ['_exec_condition : Primitive', 0], ['_exec_condition_param : Primitive', 0], ['_proceed_condition : Primitive', 0], ['_proceed_condition_param : Primitive', 0], ['_total_frame : Primitive', 0], ['_internal_processing : Primitive', 0], ['_loop_condition : Primitive', 0], ['_loop_back_index : Primitive', 0], ['_loop_limit : Primitive', 0], ['_interrept_anim_id : Primitive', 0], ['_move_chara : Primitive', 0], ['_move_chara_index : Primitive', 0], ['_move_chara_parent : String', ['BinaryObjectString', {'ObjectId': string_id_1, 'Value': '0'}]], ['_anim_set : Primitive', 0], ['_move_route : Primitive', 0], ['_move_route_index : Primitive', 0], ['_chara_height_decision_method : Primitive', 0], ['_move_pos_x : Primitive', 0.0], ['_move_pos_y : Primitive', 0.0], ['_move_pos_z : Primitive', 0.0], ['_chara_move_condition : Primitive', 0], ['_move_stert_frame : Primitive', 0], ['_move_frame : Primitive', 0], ['_move_speed : Primitive', 0.0], ['_move_pattern : Primitive', 0], ['_chara_jump_height : Primitive', 0.0], ['_chara_wave_num : Primitive', 0.0], ['_chara_rotate_condition : Primitive', 0], ['_chara_rotate_method : Primitive', 0], ['_chara_rotate_direction : Primitive', 0], ['_chara_rotate_angle : Primitive', 0.0], ['_chara_rotate_frame : Primitive', 0], ['_chara_rotate_start_frame : Primitive', 0], ['_motion_play_condition : Primitive', 0], ['_motion_id : Primitive', 0], ['_motion_id2 : Primitive', 0], ['_motion_id3 : Primitive', 0], ['_motion_blend_frame : Primitive', 0], ['_motion_disp_pattern : Primitive', 0], ['_actor_disp : Primitive', 0], ['_actor_afterimage_lifespan : Primitive', 0], ['_actor_afterimage_param_index : Primitive', 0], ['_move_chara_rotate_component_condition : Primitive', 0], ['_move_chara_rotate_component : Primitive', 0], ['_move_chara_rotate_component_start_frame : Primitive', 0], ['_move_chara_rotate_component_frame : Primitive', 0], ['_hit_condition : Primitive', 0], ['_hit_target : Primitive', 0], ['_hit_frame : Primitive', 0], ['_hit_offset_frame : Primitive', 0], ['_hit_motion_id : Primitive', 0], ['_hit_effect_id : Primitive', 0], ['_hit_se_id : Primitive', 0], ['_damage_value_disp_condition : Primitive', 0], ['_bad_status_change_condition : Primitive', 0], ['_dead_anim_condition : Primitive', 0], ['_zako_dead_motion_id : Primitive', 0], ['_zako_dead_effect_id : Primitive', 0], ['_action_command_input : Primitive', 0], ['_action_command_max_num : Primitive', 0], ['_input_start_frame : Primitive', 0], ['_input_period : Primitive', 0], ['_sweetspot_input_start_frame : Primitive', 0], ['_sweetspot_input_period : Primitive', 0], ['_is_message : Primitive', 0], ['_message_id : Primitive', 0], ['_message_num : Primitive', 0], ['_message_disp_method : Primitive', 0], ['_message_disp_position : String', ['BinaryObjectString', {'ObjectId': string_id_2, 'Value': '0'}]], ['_message_disp_position_index : Primitive', 0], ['_chara_color_id : Primitive', 0], ['_screen_color_change : Primitive', 0], ['_screen_color_frame : Primitive', 0], ['_is_screen_color_action_command_link : Primitive', 0], ['_screen_color_r : Primitive', 0.0], ['_screen_color_g : Primitive', 0.0], ['_screen_color_b : Primitive', 0.0], ['_screen_color_a : Primitive', 0.0], ['_screen_color_vertex_color : Primitive', 0], ['_is_exclude_character_from_screen_color : Primitive', 0], ['_special_effect : Primitive', 0], ['_effect_id : Primitive', 0], ['_effect_parent : String', ['BinaryObjectString', {'ObjectId': string_id_3, 'Value': '0'}]], ['_effect_disp_condition : Primitive', 0], ['_effect_disp_start_frame : Primitive', 0], ['_effect_unit_id : Primitive', 0], ['_effect_is_anim_change : Primitive', 0], ['_effect_change_anim_id : Primitive', 0], ['_effect_anim_blend_frame : Primitive', 0], ['_effect_anim_speed_setting : Primitive', 0], ['_effect_anim_end_frame : Primitive', 0], ['_effect_anim_action_command_link : Primitive', 0], ['_effect_move_start_frame : Primitive', 0], ['_effect_move_frame_decide_method : Primitive', 0], ['_effect_move_frame : Primitive', 0], ['_effect_move_speed : Primitive', 0.0], ['_effect_life_span_scale_particle_name : String', ['BinaryObjectString', {'ObjectId': string_id_4, 'Value': '0'}]], ['_effect_move_pattern : Primitive', 0], ['_effect_jump_height : Primitive', 0.0], ['_effect_bound_ratio : Primitive', 0.0], ['_effect_wave_num : Primitive', 0], ['_effect_disp_start : String', ['BinaryObjectString', {'ObjectId': string_id_5, 'Value': '0'}]], ['_effect_rotation_start : String', ['BinaryObjectString', {'ObjectId': string_id_6, 'Value': '0'}]], ['_effect_disp_end : String', ['BinaryObjectString', {'ObjectId': string_id_7, 'Value': '0'}]], ['_effect_disp_start_index : Primitive', 0], ['_effect_disp_end_index : Primitive', 0], ['_is_effect_disp_target_num : Primitive', 0], ['_effect_disp_target_num_frame_interval : Primitive', 0], ['_effect_disp_target_num_order : Primitive', 0], ['_effect_disp_start_offset_x : Primitive', 0.0], ['_effect_disp_start_offset_y : Primitive', 0.0], ['_effect_disp_start_offset_z : Primitive', 0.0], ['_effect_disp_end_offset_x : Primitive', 0.0], ['_effect_disp_end_offset_y : Primitive', 0.0], ['_effect_disp_end_offset_z : Primitive', 0.0], ['_effect_end_pos_ratio : Primitive', 0.0], ['_is_effect_end_pos_height_directly_set : Primitive', 0], ['_effect_end_pos_final_height : Primitive', 0.0], ['_effect_distance_from_camera : Primitive', 0.0], ['_effect_scale : Primitive', 0.0], ['_effect_rotate_method : Primitive', 0], ['_effect_rotate_direction : Primitive', 0], ['_effect_rotate_angle : Primitive', 0], ['_effect_rotate_frame : Primitive', 0], ['_effect_rotate_start_frame : Primitive', 0], ['_effect_afterimage_lifespan : Primitive', 0], ['_effect_afterimage_param_index : Primitive', 0], ['_effect_change_id : Primitive', 0], ['_effect_change_frame : Primitive', 0], ['_effect_end_condition : Primitive', 0], ['_effect_total_frame : Primitive', 0], ['_camera_id : Primitive', 0], ['_camera_start_frame : Primitive', 0], ['_camera_effect : Primitive', 0], ['_camera_effect_frame : Primitive', 0], ['_camera_effect_shake_max_range : Primitive', 0.0], ['_camera_effect_shake_half_period : Primitive', 0], ['_camera_move_condition : Primitive', 0], ['_camera_move_start_frame : Primitive', 0], ['_camera_move_frame : Primitive', 0], ['_camera_look_at_position : Primitive', 0], ['_camera_look_at_position_offset_x : Primitive', 0.0], ['_camera_look_at_position_offset_y : Primitive', 0.0], ['_camera_look_at_position_offset_z : Primitive', 0.0], ['_camera_delta_distance : Primitive', 0.0], ['_camera_rotate_x : Primitive', 0.0], ['_camera_rotate_y : Primitive', 0.0], ['_se_condition : Primitive', 0], ['_se_id : Primitive', 0], ['_se_frame : Primitive', 0], ['_se_volume : Primitive', 0.0], ['_se_pos : Primitive', 0], ['_se_pos_index : Primitive', 0], ['_movie_id : Primitive', 0]]}]

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
last_object_id = last_dict['ObjectId']      # Get ObjectId number
last_string_id_value = last_dict['Values'][106][1]
last_string_id_value_dict = last_string_id_value[1]
last_string_id_value_dict_ID = int(last_string_id_value_dict['ObjectId'])

i = 1
j = 0  # setting new ObjectID's for new Skill

if last_object_id < 40000:   # Test to see if the list is genuine
    skill_object_id = 50000  # Start custom ObjectID for new skill at 50000
    string_id_1 = 60000      # Start new custom String ID at 60000
else:
    skill_object_id = last_object_id + 1  # Set new ObjectID number
    string_id_1 = last_string_id_value_dict_ID + 1

# Start input for Block amount here
block_amount_to_add = input('How many Block do you want to add? : ')   # Length of new Spell
display_block_amount_changed = block_amount_to_add
try:
    val = int(block_amount_to_add)
except ValueError:
    print("Stop it......Get some help")
    sys.exit()

# Start input for Skill ID here
skill_id_to_set = input('Which skill id do you want to add? : ')
display_skill_set = skill_id_to_set
try:
    val = int(skill_id_to_set)
except ValueError:
    print("Stop it......Get some help")
    sys.exit()

# Start input for Monster ID here
monster_to_set = input('Which monster (monster ID) would you like to set your new skill for? : ')
display_monster_set = monster_to_set
try:
    val = int(monster_to_set)
except ValueError:
    print("Stop it......Get some help")
    sys.exit()

block_amount_to_add = int(block_amount_to_add) #Set to int for while loop
while i <= block_amount_to_add:
    skill_id = int(skill_id_to_set)
    new_id = skill_object_id + j
    #string_id_1 = last_string_id_value_dict_ID + 1
    string_id_2 = string_id_1 + 1
    string_id_3 = string_id_2 + 1
    string_id_4 = string_id_3 + 1
    string_id_5 = string_id_4 + 1
    string_id_6 = string_id_5 + 1
    string_id_7 = string_id_6 + 1

    monster_id = int(monster_to_set)


    new_cwi = create_new_cwi(new_id, monster_id, skill_id, string_id_1, string_id_2, string_id_3, string_id_4, string_id_5, string_id_6, string_id_7)
    classes_with_ids.append(new_cwi)
    file_content.insert(-1, new_cwi)
    i += 1
    j += 1
    string_id_1 = string_id_7 + 1
print("""
You added """ + display_block_amount_changed + """ Block length for your new Skill ID#""" + display_skill_set + """ 
allocated to monster ID#""" + display_monster_set + """ "!
Thank you!
Bubye for now!
""")

output_file = input_file.replace('.json','_added.json')
file_writer = open(output_file, 'w')
file_writer.write(json.dumps(file_content, indent=2))