




def get_num_from_string_left(curr_str):

    for element in curr_str:
        if element.isnumeric():
            return element


def get_num_from_string_right(curr_str):

    for element in reversed(curr_str):
        if element.isnumeric():
            return element


def get_two_digit_num_from_string(curr_str):

    first_digit = get_num_from_string_left(curr_str)
    last_digit = get_num_from_string_right(curr_str)

    return int(first_digit+last_digit)



def do_day_1(file_name):

    day_1_sum = 0

    file = open(file_name, 'r')

    Lines = file.readlines()

    for line in Lines:

        number = get_two_digit_num_from_string(line)
        day_1_sum += number

    return day_1_sum
