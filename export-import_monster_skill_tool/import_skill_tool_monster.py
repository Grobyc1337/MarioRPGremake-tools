
# Made by Maxtoad & Grobyc

import json
import sys
from typing import Dict, List


if __name__ == "__main__":
    if len(sys.argv) < 1:
        raise Exception("Pass in an argument for input file")

    input_file = sys.argv[1]
    output_file = input_file.replace('.json','_imported.json')

    # Set Enemy ID to import
    enemy_to_import = input("Which Enemy ID would you like to import from? : ")
    display_enemy_imported = enemy_to_import  # Keep the str() to display it later
    try:
        val = int(enemy_to_import)
    except ValueError:
        print("That's not an int!")
        print("Stop it....get some help")
        sys.exit()

    enemy_to_import = int(enemy_to_import)

    # Set Skill ID to import
    skill_to_import = input("Which Skill would you like to import? : ")
    display_skill_imported = skill_to_import  # Keep the str() to display it later
    try:
        val = int(skill_to_import)
    except ValueError:
        print("That's not an int!")
        print("Stop it....get some help")
        sys.exit()

    skill_to_import = int(skill_to_import)

    with open('Skill_' + display_skill_imported + '.json', 'r') as input_file2:
        data2 = json.load(input_file2)

    objects = []
    list_data2 = []
    i = 0
    with open(input_file, 'r') as actions_f:
        actions = json.load(actions_f)

        for items in data2:
            item_type = items
            list_data2.append(items)

        for value in actions.values():
            elem_type = value[0]
            if elem_type != 'MemberReference':
                if elem_type == 'ClassWithId':
                    if value[1]['Values'][1][1] == skill_to_import:
                        if value[1]['Values'][0][1] == enemy_to_import:
                            objects.append(list_data2[i])
                            i += 1
                        else:
                            objects.append(value)
                    else:
                        objects.append(value)
                else:
                    objects.append(value)
    with open(output_file, 'w') as output:
        output.write(json.dumps(objects, indent=2))

    print("""
    You Succesfuly Imported Skill ID """ + display_skill_imported + """
    with Enemy ID """ + display_enemy_imported)




