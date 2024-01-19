




from enum import Enum
import os.path
import sys
import json
from typing import List
from json.decoder import JSONDecodeError

the_list_2 = []


with open('battle_motion_player.json', 'r') as input_file:
    data = json.load(input_file)

skill_to_extract = input("Which Skill would you like to extract? : ")
display_skill_extracted = skill_to_extract  # Keep the str() to display it later
try:
    val = int(skill_to_extract)
except ValueError:
    print("That's not an int!")
    print("Stop it....get some help")
    sys.exit()

skill_to_extract = int(skill_to_extract)


for item in data.values():
    item_class = item[0]

    if item_class == 'ClassWithId':
        skill_id = item[1]['Values'][1][1]
        if skill_id == skill_to_extract:
            the_list_2.append(item)

if the_list_2 == []:
    print("Your Skill was not found")
    print("Ending Program")
    sys.exit()



#print(the_list_2)

print("""
You Extracted Skill ID """ + display_skill_extracted + """
press enter to finish program!""")
input()

output_file = 'Skill_' + display_skill_extracted + '.json'
#output_file = os.path.relpath(input_file.replace('battle_motion_player.json', 'Skill' + display_skill_extracted + '.json'), os.getcwd())
file_writer = open(output_file, 'w')
file_writer.write(json.dumps(the_list_2, indent=2))


