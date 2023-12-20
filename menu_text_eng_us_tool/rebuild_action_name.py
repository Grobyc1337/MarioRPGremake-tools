import json
import os
import sys
import os.path
from typing import List


def add_member_reference(id):
    member_references.append([
        'MemberReference',
        {'IdRef': id}
    ]
    )
my_new_list2 = []
my_new_list = []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Pass in an argument for input file")
    input_file = sys.argv[1]
    if not '_added.json' in input_file:
        raise Exception("File pass in input does not contain _simplified.json which is probably wrong")

    output_file = os.path.relpath(input_file.replace('_added.json', '.json'), os.getcwd())
    output_dir = os.path.join('output', os.path.dirname(output_file))
    output_file = os.path.basename(output_file)

    output_data = {}
    member_references = []
    add_member_reference(3)
    classes_with_id = []

    with open(input_file, 'r') as input:
        data: List[List] = json.load(input)
        for index, elem in enumerate(data):
            elem_type = elem[0]
            #my_new_list = elem[0]

            my_new_list.append(elem)

            if elem_type == 'ClassWithId':
                add_member_reference(elem[1]['ObjectId'])
                classes_with_id.append(elem)
            if elem_type == 'SerializedStreamHeader':
                serialized_stream_header = elem
            if elem_type == 'BinaryLibrary':
                binary_library = elem
            if elem_type == 'MemberReference':
                member_reference = elem
            if elem_type == 'ObjectNullMultiple256':
                object_null_256 = elem
            if elem_type == 'ObjectNull':
                object_null = elem
            if elem_type == 'BinaryArray':
                binary_array = elem
            if elem_type == 'ClassWithMembersAndTypes':
                class_with_members_and_types = elem

    #print(my_new_list)
    number_class_with_id = len(classes_with_id)

    #binary_array[1]['Lengths'] = [number_class_with_id + 1]

    def create_new_number():
        return '%d'


    new_number = create_new_number()

   # for new_item, value in enumerate(my_new_list):
   #     my_new_list2.append(new_item, value)
   #     #my_new_list.append(new_item2)
    for index, value in enumerate(my_new_list):
        new_id = index
        output_data['%d' % new_id] = value

    #output_data = {
    #    '0': serialized_stream_header,
    #    '1': binary_library,
    #    '2': binary_array,
    #    '3': member_reference
    #}

    #output_data['%d' % my_new_list] = class_with_members_and_types

    #output_data['%d' % number_class_with_id] = class_with_members_and_types

    #for index, cwi in enumerate(classes_with_id):
    #    new_id = number_class_with_id + 5 + index
    #    output_data['%d' % new_id] = cwi

    #output_data['%d' % (number_class_with_id * 2 + 5)] = ["MessageEnd", None]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, output_file), "w") as output:
        output.write(json.dumps(output_data, indent=2))  # output_data