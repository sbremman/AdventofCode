
str_to_num = {
'one': '1',
'two': '2',
'three': '3',
'four': '4',
'five': '5',
'six': '6',
'seven': '7',
'eight': '8',
'nine': '9'
}

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


def convert_string_with_spelled_numbers(curr_str):

    return_number_list = []

    curr_str_list = list(curr_str)

    for i in range(len(curr_str)):
        curr_element = curr_str_list[i]
        if curr_element.isnumeric():
            return_number_list.append(curr_element)

        else:
            for number in list(str_to_num.keys()):
                number_list = list(number)
                number_equal = False
                if curr_element == number_list[0]:
                    number_equal = True
                    for j in range(len(number_list)):
                        try:
                            if curr_str_list[i+j] != number_list[j]:
                                number_equal = False
                        except:
                            number_equal = False
                if number_equal:
                    str_num = str_to_num[number]
                    return_number_list.append(str_to_num[number])
    number_list = ''.join(return_number_list)
    return number_list

def do_day_1_task_1(file_name):

    day_1_sum = 0

    file = open(file_name, 'r')

    Lines = file.readlines()

    for line in Lines:

        number = get_two_digit_num_from_string(line)
        day_1_sum += number

    return day_1_sum


def do_day_1_task_2(file_name):

    day_1_sum = 0

    file = open(file_name, 'r')

    Lines = file.readlines()

    for line in Lines:

        converted_line = convert_string_with_spelled_numbers(line)

        number = get_two_digit_num_from_string(converted_line)
        day_1_sum += number

    return day_1_sum
