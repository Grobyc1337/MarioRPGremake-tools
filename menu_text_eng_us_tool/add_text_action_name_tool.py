# Made by Maxtoad & Grobyc

from ast import Dict
from enum import Enum
import sys
import json
import os.path
from typing import List
from json.decoder import JSONDecodeError

##########################################
#               FUNCTIONS
##########################################

def create_new_cwi_action(a_object_id, m_skill_id, string_id, string_name):
    return ["ClassWithId", {"ObjectId": a_object_id, "MetadataId": 33, "Values": [["m_id : Primitive", m_skill_id],
        ["m_text : String", ["BinaryObjectString", {"ObjectId": string_id, "Value": string_name}]]]}]

def create_new_idref(new_idref):
    return ["MemberReference", {"IdRef": new_idref}]

##########################################
#               CLASSES
##########################################

class ObjectType(Enum):
    ACTION_NAME = 1

##########################################
#               BEGIN
##########################################

with open('menu_text_eng_us.json', 'r') as input_file:
    data = json.load(input_file)

#input_file = sys.argv[1]

#file_reader = open(input_file, 'r')
#data = json.load(file_reader)


# Ask user how many Action's Name they want to add
# amount_to_add = input("How many new Action's Name would you like to add? : ")
# display_amount_changed = amount_to_add  # Keep the str() to display it later


# Adding a bunch of Var
new_list = False      # Asking if the list is genuine
the_list_2 = []       # Create a second list that we will use
new_list_test = []
check_highest_id = []
check_highest_ba_id = []
max_new_id = 0
max_new_ba_id = 0
last_o_id = 0
d_object_id = 0
# Maxtoad's Vars
object_index = -1
objects = {}
objects_by_type = {}
ids_to_type = {}
cwi_by_type = {}
# PY pas content
item_object_id = -1
item_type = -1
object_id = -1
new_index_add = -1

# ~~~ START MAXTOAD's MASTER CODE ~~~
for item in data.values():   #data.values()
    item_class = item[0]
    item_value = item[1]
    the_list_2.append(item) # New List to edit
    if item_class == 'BinaryArray':
        object_index += 1
    # We are loop the 'main' array
    if object_index == 0 :
        if item_class.startswith('Class'):
            for value in item_value['Values']:
                if value[0] == 'm_file_id : String':
                    item_type = value[1][1]['Value']
                if value[0] == 'm_data : Class':
                    item_object_id = value[1][1]['IdRef']
            objects[item_object_id] = item_type
    # We are looping the others
    elif object_index > 0:
        if item_class == 'BinaryArray':
            object_id = item_value['ObjectId']
        object_type = objects[object_id]
        if item_class == 'MemberReference':
            member_ref = item_value['IdRef']
            ids_to_type[member_ref] = object_type
        if not object_type in objects_by_type:
            objects_by_type[object_type] = []
        objects_by_type[object_type].append(item)

skip = True
class_with_ids_start = False
for item in data.values(): # data.values()
    item_class = item[0]
    item_value = item[1]
    if item_class == 'ClassWithMembersAndTypes':
        if skip:
            skip = False
            continue
        else:
            class_with_ids_start = True
            continue
    # The ClassWithIds start here
    if class_with_ids_start:
        if item_class == 'ClassWithId':
            object_id = item[1]['ObjectId']
            item_type = ids_to_type[object_id]
            if not item_type in cwi_by_type:
                cwi_by_type[item_type] = []
            cwi_by_type[item_type].append(item)

spells = []
# If you need the 'actions' for example, you can now do
actions = cwi_by_type['action_name']
for action in actions:
    last_action = action[1]['Values'][1][1][1]['Value']
    spells.append(last_action)

    #print('')

# ~~~ END MAXTOAD's MASTER CODE ~~~

# ~~~ MON CODE START ~~~
# Find length of Table action_name  (answer is 750)

for item in data.values():
    item_class = item[0]
    if item_class == 'ClassWithId':
        d_object_id = item[1]['ObjectId']
        new_list_test.append(d_object_id)
for classes in new_list_test:
    if classes > last_o_id:
        last_o_id = classes

last_skill_id = objects_by_type['action_name'][0][1]['Lengths'][0]
# Find last string_id in action_name list
last_action_string_id = actions[-1][1]['Values'][1][1][1]['ObjectId']

# Ask user how many Action's Name they want to add
amount_to_add = input("How many new Action's Name would you like to add? : ")
display_amount_changed = amount_to_add  # Keep the str() to display it later
try:
    val = int(amount_to_add)
except ValueError:
    print("That's not an int!")
    print("Stop it....get some help")
    sys.exit()



# those vars are only used if user is adding more than 1 skill
i = 1  # i  is for the ID to add when looping
j = 1  # j  is for the amount in first loop
k = 0  # k  is for the amount in second loop
new_index_idref = 0
# Use this to see if list has been edited or not! (Original length or not)
if last_skill_id == 750:   # Means list has Original length -> Use 50000
    new_list = True
    last_object_id = 50000    # This is a custom new ObjectId for the Spell => 50000 is unused
    last_string_id = 60000    # This is a custom new ObjectId for Spell's Strings => 60000 is unused
else:
    last_object_id = last_o_id + 1  # last_skill_id          # last action skill ID in the list
    last_string_id = last_action_string_id  # last action string in the list
# Use a different value if the list already has been edited !!!

blank_new_name = 'Blank Name'  # Put blank name when creating more than 1 spell

# ~~~~~~~~  If input is > 1 -> Generate "x" Blank Name Spells  ~~~~~~~~

amount_to_add = int(amount_to_add)
if amount_to_add > j:  # j = 1  here

    while j <= amount_to_add:
          # Unedited list starts at 751 (750 + 1)
        if new_list:  # offset the new objectid & stringid if needed
            new_skill_id = last_skill_id + i
            new_name_id = last_object_id
            new_string_id = last_string_id
            new_list = False
            j += 1  # Loop for amount to add
        else:
            new_skill_id = last_skill_id + i
            new_name_id = last_object_id + i
            new_string_id = last_string_id + i
            i += 1  # Loop for id to add
            j += 1
        new_cwi_action = create_new_cwi_action(new_name_id, new_skill_id, new_string_id, blank_new_name)
        actions.append(new_cwi_action)  # This works well

        #  index 3162 should be a variable
        #  last_object_id

        for item2 in the_list_2:
            item_class_2 = item2[0]
            item_ba_class = item2[0]
            item_value_2 = item2[1]
            if item_class_2 == 'ClassWithId':
                object_id2 = item2[1]['ObjectId']
                check_highest_id.append(object_id2)
            if item_ba_class == 'BinaryArray':
                object_ba_id = item2[1]['ObjectId']
                check_highest_ba_id.append(object_ba_id)
                if object_ba_id == 16:
                    new_index_idref = the_list_2.index(item2)
            #    for ba_ids in check_highest_ba_id:
            #        if ba_ids > max_new_ba_id:
            #            max_new_ba_id = ba_ids  # Return highest BinaryArray ID

        for ids in check_highest_id:
            if ids > max_new_id:
                max_new_id = ids  # Return highest ID
        for item3 in the_list_2:
            item_class_3 = item3[0]
            if item_class_3 == 'ClassWithId':
                object_id2 = item3[1]['ObjectId']
                check_highest_id.append(object_id2)
                if max_new_id < 50000:  # Means list is fresh
                    new_index_add = 3163
                else:
                    new_index_add = 3163 + (last_skill_id - 750) * 2

        while k < amount_to_add:
            new_skill_id = last_skill_id + (k + 1)
            new_name_id = last_object_id + k
            new_string_id = last_string_id + k
            new_cwi_action2 = create_new_cwi_action(new_name_id, new_skill_id, new_string_id, blank_new_name)

            new_idref = create_new_idref(new_name_id)
            the_list_2.insert(new_index_idref, new_idref)
            the_list_2.insert(new_index_add, new_cwi_action2)
            new_index_add += 2    # Adjust Order
            new_index_idref += 1  # Adjust Order
            k += 1 # Counter for amount to add


    for item2 in the_list_2:
        item_ba_class = item2[0]
        if item_ba_class == 'BinaryArray':
            object_ba_id = item2[1]['ObjectId']
            check_highest_ba_id.append(object_ba_id)
            # amount_to_add = int(amount_to_add)
            # print(item_ba[1]['Lengths'])
            if object_ba_id == 14:
                item2[1]['Lengths'][0] = item2[1]['Lengths'][0] + amount_to_add

            if object_ba_id == 16:
                new_index_idref = the_list_2.index(item2)
            #for ba_ids in check_highest_ba_id:
            #    if ba_ids > max_new_ba_id:
            #        max_new_ba_id = ba_ids  # Return highest BinaryArray ID




    #find_actioname = the_list_2[3161]

    print("""
    You added """ + display_amount_changed + """ new skill's names!
    Bubye for now!
    """)



# ~~~~~~~~  If input is 1   -> prompt "enter custom name" ~~~~~~~~



else:
    new_name_to_add = input('Input your new Action Name : ')
    new_skill_id = last_skill_id + i  # Unedited list starts at 751 (750 + 1)
    if new_list:  # offset the new ObjectId & StringId
        new_name_id = last_object_id
        new_string_id = last_string_id
    else:
        new_name_id = last_object_id + i
        new_string_id = last_string_id + i

    for item2 in the_list_2:
        item_class_2 = item2[0]
        item_value_2 = item2[1]
        if item_class_2 == 'ClassWithId':
            object_id2 = item2[1]['ObjectId']
            check_highest_id.append(object_id2)

    for ids in check_highest_id:
        if ids > max_new_id:
            max_new_id = ids  # Return highest ID

    for item3 in the_list_2:
        item_class_3 = item3[0]
        if item_class_3 == 'ClassWithId':
            object_id2 = item3[1]['ObjectId']
            check_highest_id.append(object_id2)

            if max_new_id < 50000:  # Means list is fresh
                new_index_add = 3162
            else:
                #new_index_add = maxvalue
                #new_index_add += 1
                if item3[1]['ObjectId'] == max_new_id:
                    new_index_add = the_list_2.index(item3[1]['ObjectId'])



    new_cwi_action = create_new_cwi_action(new_name_id, new_skill_id, new_string_id, new_name_to_add)
    # This append the new action(s) name(s) at the good place in actions!
    actions.append(new_cwi_action)
    # This insert the new action(s) name(s) at the good place in the_list_2!
    the_list_2.insert(new_index_add, new_cwi_action)


    # Must build an ID Ref  at the corresponding place ->   ex :  "ObjectId": 191  is "IdRef": 191
    # ->  Find highest IdRef in BinaryArray(ObjectId 14)

    # if highest_ba_idref == 191 # Fresh List ->
    #    #create memberref with IdRef
    # else:
    # Find highest_ba_idref
    # eg:
    # highest_ba_objectid = 50005 -> do + 1

    for item_ba in the_list_2:
        item_ba_class = item_ba[0]
        if item_ba_class == 'BinaryArray':
            object_ba_id = item_ba[1]['ObjectId']
            check_highest_ba_id.append(object_ba_id)
            #amount_to_add = int(amount_to_add)
            #print(item_ba[1]['Lengths'])
            if object_ba_id == 14:
                item_ba[1]['Lengths'][0] = [item_ba[1]['Lengths'][0] + amount_to_add]

            if object_ba_id == 16:
                new_index_idref = the_list_2.index(item_ba)

    #for ba_ids in check_highest_ba_id:
    #    if ba_ids > max_new_ba_id:
    #        max_new_ba_id = ba_ids  # Return highest BinaryArray ID

    new_idref = create_new_idref(new_name_id)
    the_list_2.insert(new_index_idref, new_idref)

    print("""
    You added """ + new_name_to_add + """ Skill Name!
    Bubye for now!
    """)


    print("Press any key to finish the program : ")
    print("Doesnt work yet,lol execution...")
    #input()



output_file = 'menu_text_eng_us_added.json'
#output_file = os.path.relpath(input_file.replace('_simplified.json', '_added.json'), os.getcwd())
file_writer = open(output_file, 'w')
file_writer.write(json.dumps(the_list_2, indent=2))


"""
    for item2 in the_list_2:
        item_class_2 = item2[0]
        item_value_2 = item2[1]
        if item_class_2 == 'ClassWithId':
            object_id2 = item2[1]['ObjectId']
            check_highest_id.append(object_id2)

    maxvalue = check_highest_id[0]
    for number in check_highest_id:
        if number > maxvalue:
            maxvalue = number

    if maxvalue < 50000:  # Means list is fresh
        new_index_add = 3162
    else:
            #new_index_add = maxvalue
            #new_index_add += 1
        if item2[1]['ObjectId'] == max_new_id:
            new_index_add = the_list_2.index(item2[1]['ObjectId'])
"""