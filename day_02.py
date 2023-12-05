
import re


NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14

color_to_pos_dict = {
    'red': 0,
    'green': 1,
    'blue': 2
}

def get_max_num_cubes_shown(input_string):
    # Return: [num_red, num_green, num_blue]

    list_of_strings = input_string.split(';')

    for string in list_of_strings:
        new_string = string.split(':')
        if len(new_string) == 2:
            list_of_strings[0] = new_string[1]

    max_colors_found = [0, 0, 0]

    for string in list_of_strings:

        num_color_list = take_in_string_of_colors_output_array(string)

        for i in range(len(max_colors_found)):
            if max_colors_found[i] < num_color_list[i]:
                max_colors_found[i] = num_color_list[i]

    return max_colors_found

def take_in_string_of_colors_output_array(input_string):
    # Takes in a string which describes how many of each color was found in a pull.
    # Assume max 99 balls of one color
    # Outputs on the form [num_red, num_green, num_blue]

    return_list = [0, 0, 0]

    numbers_in_string = re.findall(r'\d+', input_string)

    rgb_positions = [-1, -1, -1]

    for color in color_to_pos_dict.keys():
        color_pos = input_string.find(color)
        rgb_positions[color_to_pos_dict[color]] = color_pos

    sorted_rgb_positions = sorted(rgb_positions)

    number_index = 0
    for rgb_pos in sorted_rgb_positions:
        if rgb_pos != -1:
            index = rgb_positions.index(rgb_pos)
            return_list[index] = int(numbers_in_string[number_index])
            number_index += 1

    return return_list


    """input_string_list = list(input_string)

    for i in range(len(input_string_list)):
        curr_element = input_string_list[i]
        number_list = []
        if curr_element.isnumeric():
            number_list.append(curr_element)
            if input_string_list[i+1].isnumeric():
                number_list.append(curr_element)

        number = ''.join(number_list)
        number = int(number)"""


def get_id(input_string):

    list_of_strings = input_string.split(':')
    game_number = list_of_strings[0]

    number_list = []

    for element in game_number:
        if element.isnumeric():
            number_list.append(element)

    id = ''.join(number_list)
    id_int = int(id)

    return id_int




def do_task_1(file_name):


    file = open(file_name, 'r')

    Lines = file.readlines()

    id_sum = 0

    for line in Lines:
        line_id = get_id(line)
        cube_max_in_line = get_max_num_cubes_shown(line)

        max_exceeded = False

        if cube_max_in_line[0] > NUM_RED:
            max_exceeded = True
        if cube_max_in_line[1] > NUM_GREEN:
            max_exceeded = True
        if cube_max_in_line[2] > NUM_BLUE:
            max_exceeded = True

        if max_exceeded == False:
            id_sum += line_id

    return id_sum

def do_task_2(file_name):


    file = open(file_name, 'r')

    Lines = file.readlines()

    cube_power_sum = 0

    for line in Lines:
        line_id = get_id(line)
        cube_max_in_line = get_max_num_cubes_shown(line)

        cube_power = cube_max_in_line[0]*cube_max_in_line[1]*cube_max_in_line[2]

        cube_power_sum += cube_power

    return cube_power_sum