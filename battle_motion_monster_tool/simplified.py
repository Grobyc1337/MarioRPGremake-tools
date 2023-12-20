
# Made by Maxtoad & Grobyc

import json
import sys
from typing import Dict, List


if __name__ == "__main__":
  if len(sys.argv) < 1:
    raise Exception("Pass in an argument for input file")

  input_file = sys.argv[1]
  output_file = input_file.replace('.json','_simplified.json')

  objects = []
  with open(input_file, 'r') as actions_f:
      actions = json.load(actions_f)

      for value in actions.values():
          elem_type = value[0]
          if elem_type != 'MemberReference':
              objects.append(value)
  with open(output_file, 'w') as output:
      output.write(json.dumps(objects, indent=2))
