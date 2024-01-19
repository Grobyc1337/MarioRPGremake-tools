




from enum import Enum
import os.path
import sys
import json
from typing import List
from json.decoder import JSONDecodeError

the_list_2 = []


if __name__ == "__main__":
    if len(sys.argv) < 1:
        raise Exception("Pass in an argument for input file")

    input_file2 = sys.argv[1]

with open(input_file2, 'r') as input_file:
    data = json.load(input_file)


enemy_to_extract = input("Which Enemy ID would you like to extract? : ")
display_enemy_extracted = enemy_to_extract  # Keep the str() to display it later
try:
    val = int(enemy_to_extract)
except ValueError:
    print("That's not an int!")
    print("Stop it....get some help")
    sys.exit()


skill_to_extract = input("Which Skill would you like to extract? : ")
display_skill_extracted = skill_to_extract  # Keep the str() to display it later
try:
    val = int(skill_to_extract)
except ValueError:
    print("That's not an int!")
    print("Stop it....get some help")
    sys.exit()

skill_to_extract = int(skill_to_extract)
enemy_to_extract = int(enemy_to_extract)

for item in data.values():
    item_class = item[0]

    if item_class == 'ClassWithId':
        enemy_id = item[1]['Values'][0][1]
        skill_id = item[1]['Values'][1][1]
        if skill_id == skill_to_extract:
            if enemy_id == enemy_to_extract:
                the_list_2.append(item)

if the_list_2 == []:
    print("Your Skill was not found")
    print("Ending Program")
    sys.exit()



#print(the_list_2)

print("""
You Extracted Skill ID """ + display_skill_extracted + """ with Enemy ID """ + display_enemy_extracted + """!""")

output_file = 'Skill_' + display_skill_extracted + '.json'
#output_file = os.path.relpath(input_file.replace('battle_motion_player.json', 'Skill' + display_skill_extracted + '.json'), os.getcwd())
file_writer = open(output_file, 'w')
file_writer.write(json.dumps(the_list_2, indent=2))


